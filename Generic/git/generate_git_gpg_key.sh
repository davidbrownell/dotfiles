#!/usr/bin/env bash
#
# Creates a non-expiring GPG key for signing commits, using the name and email
# already configured in git, and configures git to sign with it.
# Idempotent: exits without changes if git already has a signing key configured.
#
set -euo pipefail

KEY_TYPE="${GIT_GPG_ALGO:-ed25519}"

if ! command -v gpg > /dev/null 2>&1; then
    echo "error: gpg is not installed" >&2
    exit 1
fi

# --with-colons output is the only stable machine-readable form; field 10 of an
# fpr record holds the fingerprint.
FindKey() {
    gpg --list-secret-keys --with-colons "$1" 2> /dev/null \
        | awk -F: '/^fpr:/ { print $10; exit }'
}

configured_key="$(git config --get user.signingkey || true)"

if [[ -n "${configured_key}" ]]; then
    # A configured key that is absent from the keyring cannot sign, so treat that
    # as an error rather than silently replacing the user's configuration.
    fingerprint="$(FindKey "${configured_key}")"

    if [[ -z "${fingerprint}" ]]; then
        echo "error: git is configured to sign with '${configured_key}'," \
             "but no matching secret key exists" >&2
        exit 1
    fi

    echo "signing key already configured: ${fingerprint}"
    exit 0
fi

key_name="${GIT_GPG_NAME:-$(git config --get user.name || true)}"
key_email="${GIT_GPG_EMAIL:-$(git config --get user.email || true)}"

if [[ -z "${key_name}" ]]; then
    echo "error: no name available; set git config user.name or GIT_GPG_NAME" >&2
    exit 1
fi

if [[ -z "${key_email}" ]]; then
    echo "error: no email available; set git config user.email or GIT_GPG_EMAIL" >&2
    exit 1
fi

key_uid="${key_name} <${key_email}>"

echo "generating ${KEY_TYPE} key for ${key_uid}"

# --quick-generate-key avoids the interactive dialog. An empty passphrase
# argument requires --batch and disables the pinentry prompt, which keeps
# non-interactive signing (CI, hooks) working. An expiration of 0 means never.
gpg --batch --quiet --passphrase '' \
    --quick-generate-key "${key_uid}" \
    "${KEY_TYPE}" sign 0

fingerprint="$(FindKey "${key_uid}")"

if [[ -z "${fingerprint}" ]]; then
    echo "error: key generation reported success but no key was found" >&2
    exit 1
fi

echo "generated key: ${fingerprint}"

git config --global user.signingkey "${fingerprint}"
git config --global commit.gpgsign true
git config --global tag.gpgsign true

echo
echo "public key to upload to your git host:"
echo
gpg --armor --export "${fingerprint}"
