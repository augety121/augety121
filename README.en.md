<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
    <img src="./assets/hero-light.svg" width="100%" alt="augety121 — Building reliable agent systems" />
  </picture>
</p>

<p align="center">
  <a href="README.md">简体中文</a>
  &nbsp;·&nbsp;
  <strong>English</strong>
</p>

<p align="center">
  <a href="#selected-work">Selected Work</a>
  &nbsp;·&nbsp;
  <a href="#engineering-radar">Engineering Radar</a>
  &nbsp;·&nbsp;
  <a href="#system-view">System View</a>
  &nbsp;·&nbsp;
  <a href="#tech-stack">Tech Stack</a>
  &nbsp;·&nbsp;
  <a href="#github-dynamics">GitHub Dynamics</a>
</p>

---

<table>
<tr>
<td width="25%" align="center"><strong>RETRIEVE</strong><br/><sub>Find evidence that actually matters</sub></td>
<td width="25%" align="center"><strong>CONTEXT</strong><br/><sub>Put the right information in the window</sub></td>
<td width="25%" align="center"><strong>ACT</strong><br/><sub>Keep tool use inside explicit boundaries</sub></td>
<td width="25%" align="center"><strong>EVALUATE</strong><br/><sub>Make outcomes reproducible and verifiable</sub></td>
</tr>
</table>

I focus on **RAG agents, context engineering, MCP, agent runtimes, and reproducible evaluation**.

Rather than optimizing for an agent that merely looks impressive in a one-off demo, I care about whether a real system can keep answering: **Where did the evidence come from? Why was this context selected? Why was this tool allowed to run? What state changed? How can the result be verified?**

> **Retrieval with evidence. Reasoning with grounding. Actions with boundaries. Evaluation with state.**

<a id="selected-work"></a>
## Selected Work

<p align="center">
  <a href="https://github.com/augety121/MCP-State-Twin">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="./assets/mcp-state-twin-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="./assets/mcp-state-twin-light.svg">
      <img src="./assets/mcp-state-twin-light.svg" width="100%" alt="MCP State Twin — reproducible AI agent evaluation environments" />
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://github.com/augety121/MCP-State-Twin"><strong>Repository</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin#readme">README</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin/tree/main/docs">Docs</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin/issues">Issues</a>
</p>

**MCP State Twin** is my current flagship open-source project: deterministic, forkable, stateful MCP test worlds for reproducible AI agent evaluation. Different agents or models can start from the same immutable snapshot, take different valid tool trajectories, and be compared by terminal state and declared invariants without writing test side effects into production services.

<details>
<summary><strong>Expand: why state should be a first-class evaluation primitive</strong></summary>
<br/>

A multi-step agent problem is not merely “what should the next message be?” Every tool call can change what later calls should observe. Reproducible evaluation therefore needs a stable environment identity, initial snapshot, tool contract, state-transition semantics, trace evidence, assertions, and terminal-state comparison — while still allowing models to take different valid trajectories.

That is why MCP State Twin centers its workflow on **snapshot → fork → act → assert → diff**.

</details>

<a id="engineering-radar"></a>
## Engineering Radar

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/focus-map-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/focus-map-light.svg">
    <img src="./assets/focus-map-light.svg" width="100%" alt="augety121 Engineering Radar" />
  </picture>
</p>

<table>
<tr>
<td width="33%" valign="top"><strong>Retrieval & Context</strong><br/><br/>Sparse / Dense / Hybrid Retrieval, reranking, knowledge graphs, memory, context budgets, evidence selection.</td>
<td width="33%" valign="top"><strong>Runtime & Tooling</strong><br/><br/>MCP, planning, routing, tool calling, state, permissions, checkpoints, rollback, failure recovery.</td>
<td width="33%" valign="top"><strong>Evaluation & Safety</strong><br/><br/>Tracing, terminal state, assertions, cost, latency, prompt injection, auditability, reproducibility.</td>
</tr>
</table>

<a id="system-view"></a>
## System View

I prefer to think of an agent as a **complete runtime system**, not an isolated prompt.

<details open>
<summary><strong>Expand / collapse: a context engine from knowledge to reliable action</strong></summary>
<br/>

<p align="center">
  <img src="./assets/context-engine-flow.webp" width="100%" alt="System flow from retrieval and context construction to reliable action and evaluation" />
</p>

```text
Knowledge
   ↓
Retrieval → Rerank → Evidence
   ↓
Context Engine
   ↓
Reasoning / Planning
   ↓
Tools + Memory + State
   ↓
Action
   ↓
Trace / Assertion / Evaluation
```

For important system decisions, I want to be able to answer three questions: **What was the evidence? What happened? How was the result verified?**

</details>

<details>
<summary><strong>Expand: Engineering Principles</strong></summary>
<br/>

1. **Context quality > context length.** More context is not automatically better; relevant, grounded context is.
2. **State is part of the problem.** Later steps must depend on real, observable state transitions.
3. **Tool calls need boundaries.** Permissions, budgets, idempotency, failure semantics, and rollback are part of the tool system.
4. **Evaluation should be reproducible.** Fix environment identity, initial state, tool contracts, and evidence instead of relying on one lucky run.
5. **Observability is a feature.** Traces, audits, cost, latency, and terminal state should be inspectable and comparable.
6. **Safety belongs in architecture.** High-risk actions should not rely on prompt instructions alone; control boundaries belong in system design.

</details>

<a id="tech-stack"></a>
## Tech Stack

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=py,ts,go,kotlin,docker,postgres,redis,git,github&theme=dark&perline=9">
    <source media="(prefers-color-scheme: light)" srcset="https://skillicons.dev/icons?i=py,ts,go,kotlin,docker,postgres,redis,git,github&theme=light&perline=9">
    <img src="https://skillicons.dev/icons?i=py,ts,go,kotlin,docker,postgres,redis,git,github&theme=light&perline=9" alt="Python, TypeScript, Go, Kotlin, Docker, PostgreSQL, Redis, Git and GitHub" />
  </picture>
</p>

<details>
<summary><strong>Expand: full technical focus</strong></summary>
<br/>

| Layer | Tools / Concepts |
| :--- | :--- |
| **Languages** | Python · TypeScript · Go · Kotlin |
| **Retrieval** | Sparse · Dense · Hybrid · RRF · Rerank · Knowledge Graph |
| **Context** | Evidence Selection · Memory · Context Budget · Query Planning |
| **Agent** | Planning · Routing · Tool Calling · Multi-Agent · MCP |
| **Runtime** | State · Permission · Checkpoint · Rollback · Audit · Failure Recovery |
| **Evaluation** | Retrieval / Answer / Agent Evaluation · Trace · Assertions · Terminal State · Cost · Latency |
| **Safety** | Prompt Injection · Tool Boundary · Least Privilege · Auditability |
| **Infra** | Docker · PostgreSQL · Redis · GitHub Actions |

</details>

<a id="github-dynamics"></a>
## GitHub Dynamics

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./github-dynamics-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./github-dynamics-light.svg">
    <img src="./github-dynamics-light.svg" width="100%" alt="GitHub public activity overview" />
  </picture>
</p>

<p align="center"><sub>Updated daily by this repository's own GitHub Actions workflow · no third-party stats-card service required</sub></p>

<details>
<summary><strong>How is this card generated?</strong></summary>
<br/>

`scripts/generate_github_stats.py` reads public activity through the GitHub GraphQL API. `.github/workflows/update-profile-stats.yml` generates both light and dark SVG cards every day, and the README selects the appropriate version based on the visitor's GitHub theme.

</details>

## Connect

<p align="center">
  <a href="https://github.com/augety121"><strong>GitHub</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin"><strong>MCP State Twin</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin/issues"><strong>Project Issues</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/augety121/issues"><strong>Profile Issues</strong></a>
</p>

<br/>

<p align="center"><strong>Retrieval with evidence. Context with intent. Actions with boundaries. Evaluation with state.</strong></p>
<p align="center"><sub>augety121 · RAG Agent · Context Engineering · MCP · Reliable Agent Systems</sub></p>
