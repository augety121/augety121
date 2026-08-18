<p align="center">
  <img src="./assets/rag-agent-banner.webp" width="100%" alt="RAG agents, context engineering, and reliable agent infrastructure" />
</p>

<h1 align="center">augety121</h1>

<p align="center">
  <strong>RAG Agent · Context Engineering · Reliable Agent Infrastructure</strong>
</p>

<p align="center">
  Building agent systems that are retrievable, traceable, controllable, and evaluable.
</p>

<p align="center">
  <a href="README.md">简体中文</a> · <strong>English</strong>
</p>

<p align="center">
  <a href="#selected-work">Selected Work</a> ·
  <a href="#engineering-focus">Focus</a> ·
  <a href="#system-view">System View</a> ·
  <a href="#tech-stack">Tech Stack</a> ·
  <a href="#github-dynamics">GitHub Dynamics</a>
</p>

---

## About

I focus on **RAG agents, context engineering, and reliable agent infrastructure**.

Rather than treating larger models or longer context windows as the whole solution, I care about whether an agent system can behave reliably on real tasks: **did retrieval find the right evidence, is the context clean, are tool calls bounded, are state transitions observable, can failures be recovered, and can outcomes be evaluated reproducibly?**

Current areas of interest include:

- intelligent retrieval, hybrid search, reranking, and knowledge graphs;
- agentic RAG, query planning, tool retrieval, and memory;
- MCP, agent runtimes, state management, and security boundaries;
- agent evaluation, observability, replay, and reproducible test environments.

> **The goal is not only to make agents look smarter, but to make them more reliable across evidence, tools, state, and evaluation.**

<a id="selected-work"></a>
## Selected Work

### [MCP State Twin](https://github.com/augety121/MCP-State-Twin)

**Deterministic, forkable, stateful MCP test worlds for reproducible AI agent evaluation — without production side effects.**

MCP State Twin provides isolated, stateful test worlds behind MCP tools. Multiple agent or model runs can start from the same immutable snapshot, take different valid tool trajectories, and be compared by terminal state and declared invariants without writing test side effects to production services.

<p>
  <a href="https://github.com/augety121/MCP-State-Twin"><strong>Repository</strong></a>
  ·
  <a href="https://github.com/augety121/MCP-State-Twin#readme">README</a>
  ·
  <a href="https://github.com/augety121/MCP-State-Twin/tree/main/docs">Docs</a>
</p>

`MCP` · `Agent Evaluation` · `Deterministic Runtime` · `Stateful Simulation` · `Go` · `SQLite`

---

<a id="engineering-focus"></a>
## Engineering Focus

| Area | Questions I care about |
| :--- | :--- |
| **Retrieval** | How do sparse, dense, hybrid retrieval, reranking, and graph structure find evidence that is actually relevant? |
| **Context Engineering** | How should knowledge, memory, tools, task state, and budgets be organized so the model sees only what matters now? |
| **Agent Runtime** | How do planning, tool calling, permissions, checkpoints, rollback, and failure recovery become a stable runtime? |
| **MCP & Tooling** | How can tool surfaces stay composable, verifiable, isolated, and free from hidden test controls exposed to the agent? |
| **Evaluation** | How should retrieval, answers, trajectories, terminal state, cost, and latency be evaluated together? |
| **Safety** | How should prompt injection, high-risk tool calls, privilege escalation, and irreversible side effects be constrained? |

<a id="system-view"></a>
## System View

I prefer to treat an agent as a complete system rather than an isolated prompt:

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

For important decisions, I want the system to answer three questions: **what evidence supported it, what changed, and how was the outcome verified?**

## Engineering Principles

1. **Context quality > context length.** More context is not automatically better; relevance and evidence matter more.
2. **State is part of the problem.** Multi-step agents must act on real, observable state transitions.
3. **Tool calls need boundaries.** Permissions, budgets, idempotency, failure semantics, and rollback belong to the tool system.
4. **Evaluation should be reproducible.** Environment identity, initial state, tool contracts, and evidence should be controlled.
5. **Observability is a feature.** Traces, audits, cost, latency, and terminal state should be inspectable and comparable.

<a id="tech-stack"></a>
## Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,ts,go,kotlin,docker,postgres,redis,git,github&theme=light&perline=9" alt="Python, TypeScript, Go, Kotlin, Docker, PostgreSQL, Redis, Git and GitHub" />
</p>

| Layer | Tools / Concepts |
| :--- | :--- |
| **Languages** | Python · TypeScript · Go · Kotlin |
| **Retrieval** | Sparse · Dense · Hybrid · RRF · Rerank · Knowledge Graph |
| **Agent** | Planning · Routing · Tool Calling · Memory · Multi-Agent · MCP |
| **Runtime** | State · Permission · Checkpoint · Rollback · Audit · Failure Recovery |
| **Evaluation** | Retrieval / Answer / Agent Evaluation · Tracing · Cost · Latency · Safety |
| **Infra** | Docker · PostgreSQL · Redis · GitHub Actions |

<a id="github-dynamics"></a>
## GitHub Dynamics

<p align="center">
  <img src="./github-dynamics.svg" width="100%" alt="Public GitHub activity overview" />
</p>

<p align="center"><sub>Updated daily by a repository-local GitHub Actions workflow from public GitHub activity.</sub></p>

## Connect

If you are working on **RAG, agents, context engineering, MCP, agent evaluation, or reliable AI infrastructure**, feel free to connect through GitHub:

- [GitHub Profile](https://github.com/augety121)
- [MCP State Twin Issues](https://github.com/augety121/MCP-State-Twin/issues)
- [Profile Repository Issues](https://github.com/augety121/augety121/issues)

<p align="center">
  <strong>Retrieval with evidence. Actions with boundaries. Evaluation with state.</strong><br/>
  <sub>让知识可检索，让推理有依据，让行动可验证。</sub>
</p>
