<p align="center">
  <img src="./assets/hero-en-light.svg" width="100%" alt="augety121 — Reliable Agent Systems" />
</p>

<p align="center">
  <a href="README.md">简体中文</a>
  &nbsp;·&nbsp;
  <strong>English</strong>
</p>

<p align="center">
  <a href="#featured">Selected Work</a>
  &nbsp;·&nbsp;
  <a href="#focus">Focus</a>
  &nbsp;·&nbsp;
  <a href="#system">System View</a>
  &nbsp;·&nbsp;
  <a href="#stack">Tech Stack</a>
  &nbsp;·&nbsp;
  <a href="#activity">GitHub Activity</a>
</p>

<p align="center">
  I care less about one impressive demo and more about agent systems that can
  <strong>retrieve evidence, engineer context, bound tool use, trace state and be evaluated reproducibly</strong>.
</p>

<p align="center">
  <sub>RAG Agent · Context Engineering · MCP · Agent Runtime · Reproducible Evaluation</sub>
</p>

---

<a id="featured"></a>
<p><sub>SELECTED WORK</sub></p>

## Featured project

<p align="center">
  <a href="https://github.com/augety121/MCP-State-Twin">
    <img src="./assets/mcp-state-twin-light.svg" width="100%" alt="MCP State Twin" />
  </a>
</p>

**MCP State Twin** is my main open-source project: deterministic, forkable, stateful MCP test worlds for reproducible AI agent evaluation.

Different agents or models can start from the same immutable snapshot, take different valid tool trajectories, and be compared by terminal state and declared invariants without writing test side effects into production services.

<p align="center">
  <a href="https://github.com/augety121/MCP-State-Twin"><strong>Repository</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin#readme">README</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin/tree/main/docs">Docs</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/augety121/MCP-State-Twin/issues">Issues</a>
</p>

<details>
<summary><strong>Why I treat state as a first-class evaluation primitive</strong></summary>
<br/>

A multi-step agent problem is not just “what should the next message be?” Every tool call can change what later calls should observe. Reproducible evaluation therefore needs explicit environment identity, starting state, transitions, failure semantics, traces, assertions, and terminal state.

That is why MCP State Twin centers its workflow around **snapshot → fork → act → assert → diff**.

</details>

---

<a id="focus"></a>
<p><sub>ENGINEERING RADAR</sub></p>

## What I work on

<p align="center">
  <img src="./assets/focus-map-light.svg" width="100%" alt="Engineering focus map" />
</p>

My interests span the complete engineering path of agent systems:

- **Retrieval** — sparse / dense / hybrid retrieval, RRF, rerank, knowledge graphs;
- **Context Engineering** — evidence selection, memory, context budgets, query planning;
- **Agent Runtime** — planning, routing, state, checkpoints, rollback and recovery;
- **MCP & Tooling** — contracts, permissions, isolation, idempotency and failure semantics;
- **Evaluation** — traces, assertions, terminal state, cost, latency and reproducibility;
- **Safety** — prompt injection, least privilege, auditability and irreversible side effects.

---

<a id="system"></a>
<p><sub>SYSTEM VIEW</sub></p>

## From knowledge to verifiable action

<p align="center">
  <img src="./assets/system-map-light.svg" width="100%" alt="From knowledge to verifiable action" />
</p>

I think of an agent as an operating system rather than an isolated prompt: retrieval supplies evidence, context engineering selects what matters, runtime manages state and control, tools act, and evaluation verifies the result.

<details open>
<summary><strong>Engineering Principles</strong></summary>
<br/>

1. **Context quality > context length.** More context is not automatically better context.
2. **State is part of the problem.** Later behavior must be grounded in observable state changes.
3. **Tool calls need boundaries.** Permissions, budgets, idempotency, failure semantics and rollback belong in the system.
4. **Evaluation should be reproducible.** Fix the environment, starting state, contracts and evidence.
5. **Observability is a feature.** Traces, audit, cost, latency and terminal state should be inspectable.
6. **Safety belongs in architecture.** High-risk actions need real authorization boundaries, not only prompt instructions.

</details>

---

<a id="stack"></a>
<p><sub>TOOLBOX</sub></p>

## Tech stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,ts,go,kotlin,docker,postgres,redis,git,github&theme=light&perline=9" alt="Python, TypeScript, Go, Kotlin, Docker, PostgreSQL, Redis, Git and GitHub" />
</p>

<p align="center">
  <code>Python</code> · <code>TypeScript</code> · <code>Go</code> · <code>Kotlin</code> ·
  <code>Docker</code> · <code>PostgreSQL</code> · <code>Redis</code> · <code>GitHub Actions</code>
</p>

<details>
<summary><strong>Full engineering stack</strong></summary>
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

---

<a id="activity"></a>
<p><sub>PUBLIC ACTIVITY</sub></p>

## GitHub activity

<p align="center">
  <img src="./github-dynamics-light.svg" width="100%" alt="GitHub public activity overview" />
</p>

<details>
<summary><strong>Contribution Playground</strong></summary>
<br/>

<p align="center">
  <img src="./assets/contribution-snake.svg" width="100%" alt="GitHub contribution snake animation" />
</p>

<p align="center"><sub>Generated by GitHub Actions + Platane/snk and stored in this repository.</sub></p>

</details>

---

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

<p align="center">
  <img src="./assets/footer-light.svg" width="100%" alt="Evidence, Context, Action, State, Evaluation" />
</p>
