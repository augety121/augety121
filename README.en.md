<a id="top"></a>

<p align="right">
  <a href="./README.md">简体中文</a> &nbsp;/&nbsp; <strong>English</strong>
</p>

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/hero-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/hero-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/hero-mobile-en.svg" />
  <img src="./assets/profile/hero-en.svg" width="100%" alt="Building reliable agent systems. Grounded in evidence. Designed for verifiable action." />
</picture>

<p align="center">
  <a href="#about">About</a> &nbsp; · &nbsp; <a href="#work">Selected work</a> &nbsp; · &nbsp; <a href="#craft">How I build</a> &nbsp; · &nbsp; <a href="#stack">Toolbox</a> &nbsp; · &nbsp; <a href="#activity">Open-source activity</a>
</p>

<a id="about"></a>

## About

I'm a developer focused on **RAG and agent systems engineering**: how knowledge becomes context, and how context turns into reliable action.

This is where I share open-source work, from **MCP tool environments and reproducible evaluation** to local tools and browser extensions. Less repetitive work, with clearer boundaries for data and actions.

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/focus-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/focus-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/focus-mobile-en.svg" />
  <img src="./assets/profile/focus-en.svg" width="100%" alt="Engineering focus: context (retrieval, reranking, knowledge graphs), runtime (MCP, state, recovery), and evaluation (traces, assertions, reproducibility)." />
</picture>

### Currently exploring

- **Retrieval & memory** — relevant evidence and context that stays useful.
- **Tools & state** — multi-step execution that can be traced, isolated and recovered.
- **Evaluation & feedback** — the same starting point, with measurable improvements.

<details>
<summary>Engineering details I care about</summary>

- **Context quality**: relevance and evidence matter more than simply adding length.
- **Tool boundaries**: permissions, budgets and failure semantics belong in the architecture.
- **Visible state**: multi-step execution should be traceable, inspectable and recoverable.
- **Reproducible evaluation**: compare improvements by running again from the same starting point.

</details>

<a id="work"></a>

## Selected work

Some projects explore what agents can do and where their boundaries lie. Others take repetitive work out of everyday life.

<p align="center">
  <a href="#project-hashmm">Workspace</a> &nbsp; · &nbsp; <a href="#project-twin">Evaluation</a><br/>
  <a href="#project-resume">Form filling</a> &nbsp; · &nbsp; <a href="#project-applykit">Documents</a> &nbsp; · &nbsp; <a href="#project-autumn">Job posts</a>
</p>

### Agents & evaluation

From retrieval to action, and from execution back to verifiable evidence.

<a id="project-hashmm"></a>

<a href="https://github.com/augety121/HashMM-RAG-Agent">
<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/project-hashmm-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/project-hashmm-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/project-hashmm-mobile-en.svg" />
  <img src="./assets/profile/project-hashmm-en.svg" width="100%" alt="HashMM-RAG-Agent · A local-first agent workspace · Historical open-source edition" />
</picture>
</a>

A local workspace connecting **knowledge retrieval, cited evidence and recoverable tasks**. This links to the published historical edition.

[Source →](https://github.com/augety121/HashMM-RAG-Agent) &nbsp; [Overview](https://github.com/augety121/HashMM-RAG-Agent#readme) &nbsp; [Contribute](https://github.com/augety121/HashMM-RAG-Agent/blob/main/COMMUNITY.md)

<br/>

<a id="project-twin"></a>

<a href="https://github.com/augety121/MCP-State-Twin">
<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/project-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/project-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/project-mobile-en.svg" />
  <img src="./assets/profile/project-en.svg" width="100%" alt="MCP State Twin · Development preview. See the project documentation for implemented capabilities and limitations." />
</picture>
</a>

A **reproducible MCP test environment** for agents: fork runs from the same snapshot, use tools in isolation, and compare final states.

[Source →](https://github.com/augety121/MCP-State-Twin) &nbsp; [Docs](https://github.com/augety121/MCP-State-Twin/tree/main/docs) &nbsp; [Issues](https://github.com/augety121/MCP-State-Twin/issues)

### Practical tools

Organize information, prepare documents, and automate repetitive steps—while keeping the final decision with the person.

<a id="project-resume"></a>

<a href="https://github.com/augety121/jianlitianxie">
<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/project-resume-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/project-resume-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/project-resume-mobile-en.svg" />
  <img src="./assets/profile/project-resume-en.svg" width="100%" alt="Resume Fill Assistant · Local profile management, reviewed form filling and optional MCP collaboration" />
</picture>
</a>

A **local form-filling assistant** for Chrome / Edge. Review facts and field mappings before filling selected content. No model calls by default; it never submits applications automatically.

[Source →](https://github.com/augety121/jianlitianxie) &nbsp; [Install guide](https://github.com/augety121/jianlitianxie/blob/main/docs/INSTALL-0.4.3.md) &nbsp; [Privacy](https://github.com/augety121/jianlitianxie/blob/main/docs/PRIVACY-0.4.3.md)

<br/>

<a id="project-applykit"></a>

<a href="https://github.com/augety121/ApplyKit">
<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/project-applykit-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/project-applykit-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/project-applykit-mobile-en.svg" />
  <img src="./assets/profile/project-applykit-en.svg" width="100%" alt="ApplyKit · A local PDF and image toolkit for application documents" />
</picture>
</a>

**Crop images, convert PDFs and compress files locally** to meet document requirements. Keeps originals and does not upload documents to the internet.

[Source →](https://github.com/augety121/ApplyKit) &nbsp; [Download](https://github.com/augety121/ApplyKit/releases) &nbsp; [User guide](https://github.com/augety121/ApplyKit#readme)

<br/>

<a id="project-autumn"></a>

<a href="https://github.com/augety121/autumn-jobs-crawler">
<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/project-autumn-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/project-autumn-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/project-autumn-mobile-en.svg" />
  <img src="./assets/profile/project-autumn-en.svg" width="100%" alt="autumn-jobs-crawler · Safety-first campus hiring aggregation and Excel export" />
</picture>
</a>

Turns **official company campus hiring announcements** into filterable Excel records, preserving sources and human review. No automatic login, verification bypass or applications.

[Source →](https://github.com/augety121/autumn-jobs-crawler) &nbsp; [User guide](https://github.com/augety121/autumn-jobs-crawler#readme) &nbsp; [Safety](https://github.com/augety121/autumn-jobs-crawler/blob/main/SECURITY.md)

<details>
<summary>Reading guide & project boundaries</summary>

- **Start with the overview**: each README explains the use case and setup; documentation covers design and limitations.
- **HashMM** is a historical open-source edition; **MCP State Twin** remains a development preview. Roadmaps are not implemented features.
- **Resume Fill Assistant** uses explicitly selected facts and never submits applications automatically; **ApplyKit** preserves originals; **Autumn Jobs Crawler** routes restricted or uncertain sources to manual review.
- Resume Fill Assistant offers optional temporary MCP collaboration. See the docs for supported sites and controls, and review the filled form.
- The historical HashMM edition includes desktop, Android and tool extensions. Job aggregation includes rate limits, deduplication and source checks. Each project's docs define its supported capabilities.
- Explore MCP State Twin through its [overview](https://github.com/augety121/MCP-State-Twin#readme), [design docs](https://github.com/augety121/MCP-State-Twin/tree/main/docs) and [Issues](https://github.com/augety121/MCP-State-Twin/issues).

</details>

<p align="right"><a href="https://github.com/augety121?tab=repositories&amp;type=public">Browse all public repositories →</a></p>

<a id="craft"></a>

## How I build

I prefer to start with a concrete problem and a small, verifiable loop, then gradually add state management, boundaries and observability.

<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/craft-mobile-en-static.svg" />
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/craft-en-static.svg" />
  <source media="(max-width: 600px)" srcset="./assets/profile/craft-mobile-en.svg" />
  <img src="./assets/profile/craft-en.svg" width="100%" alt="An engineering feedback loop: define, build, verify and iterate." />
</picture>

- **Small, complete implementations**: give each change a clear goal, inputs, outputs and scope.
- **Reviewable results**: document successful paths, failure cases and important trade-offs together.
- **Evolving designs**: understand real constraints before choosing abstractions, interfaces and extension points.

<a id="stack"></a>

## Toolbox

<p>
  <a href="https://github.com/tandpfun/skill-icons">
    <img src="https://skillicons.dev/icons?i=py,ts,go,kotlin,docker,postgres,redis,git,github&amp;theme=light&amp;perline=9" width="440" alt="Python, TypeScript, Go, Kotlin, Docker, PostgreSQL, Redis, Git, GitHub" />
  </a>
</p>

**Languages** &nbsp; Python · TypeScript · Go · Kotlin<br/>
**Engineering tools** &nbsp; Docker · PostgreSQL · Redis · Git · GitHub Actions

<details>
<summary>Beyond the technology stack</summary>

Interfaces and data contracts, testing and continuous integration, logs and execution traces, resource budgets, permission boundaries, and documentation that helps the next reader understand the system.

Tools change. What I want to keep improving is the ability to analyze problems, test assumptions and build dependable systems.

</details>

<a id="activity"></a>

## Open-source activity

<p>
<picture>
  <source media="(max-width: 600px)" srcset="./assets/profile/stats-mobile-en.svg" />
  <img src="./assets/profile/stats-en.svg" width="100%" alt="Public GitHub repositories, stars received, contributions in the last year, and followers. See the card for the update date." />
</picture>
</p>

<p>
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/contributions-static.svg" />
    <source media="(max-width: 600px)" srcset="./assets/profile/contribution-mobile-en.svg" />
    <img src="./assets/profile/contribution-en.svg" width="100%" alt="Mint-colored snake animation generated from the real GitHub contribution calendar" />
  </picture>
</p>

<sub>Stats and contribution animation update daily through GitHub Actions; the card shows the update date. This is not a live online indicator. Animation powered by <a href="https://github.com/Platane/snk">Platane/snk</a>.</sub>

---

### Let's connect

Interested in **RAG, context engineering, MCP or agent evaluation**? Let's start with a specific question, a piece of code or a reproducible experiment.

[My repositories](https://github.com/augety121?tab=repositories) &nbsp; · &nbsp; [Project discussions](https://github.com/augety121/MCP-State-Twin/issues) &nbsp; · &nbsp; [Profile feedback](https://github.com/augety121/augety121/issues)

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/footer-en-static.svg" />
  <img src="./assets/profile/footer-en.svg" width="100%" alt="Stay curious. Keep building." />
</picture>

<p align="right"><a href="#top">Back to top ↑</a></p>
