---
name: understand-code
description: Guides an agent to systematically explore an unfamiliar codebase and produce a structured Markdown overview covering architecture, data/control flow, coding conventions, key components, and entry points, with Mermaid diagrams where helpful, then prompts the user to save the result to a file.
metadata:
    version: 0.1.0
---

### Skill: Codebase Understanding

**Trigger / When to use**
Use this skill whenever the user asks to understand, explore, onboard to, or document a new or unfamiliar codebase.

**Goal**
Produce a clear, structured Markdown document that explains the architecture, data flow, coding conventions, key components, and how to navigate the project. Include Mermaid diagrams wherever they improve clarity.

**Process**

1. **Initial Exploration**
   - Identify the project root, primary language(s), build system, and package manager.
   - Locate README, CONTRIBUTING, docs/, architecture docs, ADRs, and configuration files.
   - Detect entry points (main, app, index, server, CLI, etc.).
   - Map the top-level directory structure.

2. **Architecture Analysis**
   - Determine the overall architectural style (monolith, modular monolith, microservices, layered, hexagonal, event-driven, etc.).
   - Identify major layers or modules (presentation, application, domain, infrastructure, etc.).
   - List key components, services, packages, or bounded contexts and their responsibilities.
   - Note external dependencies, third-party services, and infrastructure (databases, message brokers, caches, APIs).

3. **Data Flow & Control Flow**
   - Trace the main request/response or event paths from entry points to persistence or external systems.
   - Describe how data moves between layers/components.
   - Document important state management, caching, or messaging patterns.
   - Highlight critical sequences (authentication, data processing pipelines, background jobs, etc.).

4. **Coding Conventions & Patterns**
   - Observe naming conventions, file/folder organization, and module boundaries.
   - Identify common design patterns, error-handling style, logging approach, and testing strategy.
   - Note configuration management, environment handling, and dependency injection / inversion of control practices.
   - Flag any notable anti-patterns or areas of technical debt if they affect understanding.

5. **Diagrams (use Mermaid)**
   Create diagrams when they add value. Preferred types:
   - High-level architecture / component diagram
   - Sequence diagrams for key flows
   - Data-flow or pipeline diagrams
   - Entity-relationship or domain model sketches (when relevant)
   - Deployment or infrastructure overview (if clear from the repo)

6. **Output Format**
   Generate a single coherent Markdown document with these sections (adapt as needed):

   ```markdown
   # Codebase Overview: [Project Name]

   ## 1. Quick Summary
   [2–4 sentence high-level description]

   ## 2. Tech Stack & Tooling
   - Languages, frameworks, runtimes
   - Build / package / test tools
   - Key libraries and services

   ## 3. Directory Structure
   [Annotated tree or description of important folders]

   ## 4. Architecture
   [Description + Mermaid component/architecture diagram]

   ## 5. Key Components & Responsibilities
   [Bullet list or table]

   ## 6. Data & Control Flow
   [Description + Mermaid sequence or flowchart diagrams for the most important paths]

   ## 7. Coding Conventions & Patterns
   [Naming, structure, patterns, error handling, testing, etc.]

   ## 8. Entry Points & How to Run
   [How the application starts, main commands, environment setup]

   ## 9. Important Files & Where to Look First
   [Curated list of the most valuable files for newcomers]

   ## 10. Open Questions / Areas Needing Clarification
   [Anything still unclear that would benefit from human input]
   ```

7. **Final Instruction to the User**
   Once the markdown is generated, offer to save it to a file for future reference and updates.

**Style Guidelines**
- Be precise and concrete; reference actual file paths, class/module names, and function names when possible.
- Prefer clarity over completeness — focus on what a new engineer needs most.
- Keep diagrams simple and readable.
- If the codebase is very large, prioritize the core application paths and note that peripheral areas were only skimmed.

**Success Criteria**
A new engineer reading the output should be able to:
- Understand the big picture in under 5 minutes.
- Know where to look for the most important code.
- Follow the main data/request flows.
- Recognize the project’s coding style and architectural decisions.
