<!--
Profile README — @rudraksha127
Design system: Midnight Aurora
Principle: every important capability should lead to inspectable evidence.
-->

<div align="center">

<img src="./assets/readme/midnight-aurora-hero.svg" width="100%" alt="Rudraksh Udiya — Software Engineering, Full-Stack Development and Applied AI, with a dimensional midnight-violet visual." />

<a href="https://github.com/rudraksha127/Portfolio"><img src="https://img.shields.io/badge/Portfolio-Source-8B5CF6?style=for-the-badge&logo=github&logoColor=white" alt="Portfolio source" /></a>
<a href="https://www.linkedin.com/in/rudraksh-udiya"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn profile" /></a>
<a href="https://raw.githubusercontent.com/rudraksha127/rudraksha127/main/resume.pdf"><img src="https://img.shields.io/badge/Resume-PDF-22D3EE?style=for-the-badge&logo=adobeacrobatreader&logoColor=0B1020" alt="Resume PDF" /></a>
<a href="mailto:luckyudiya@gmail.com"><img src="https://img.shields.io/badge/Email-Contact-111827?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

</div>

<p align="center">
  <strong>Software Engineering</strong> · Full-Stack Development · Applied AI
  <br/>
  <sub>IT Undergraduate · Acropolis Institute of Technology & Research · Indore, India</sub>
</p>

<p align="center">
  <a href="#profile">Profile</a> ·
  <a href="#featured-engineering-work">Projects</a> ·
  <a href="#engineering-practice">Engineering Practice</a> ·
  <a href="#technical-toolkit">Toolkit</a> ·
  <a href="#computer-science--problem-solving">CS & DSA</a> ·
  <a href="#experience--education">Experience</a> ·
  <a href="#contact">Contact</a>
</p>

---

## Profile

I am an Information Technology undergraduate at **Acropolis Institute of Technology & Research, Indore (2024–2028)**, working toward a career in **software engineering**. My primary interests are building full-stack applications, dependable backend workflows, data-intensive systems, and practical AI-enabled products.

I enjoy the complete engineering loop: understanding a problem, translating it into clear requirements, choosing an appropriate design, implementing the system, testing important paths, and documenting how another developer can run and inspect it.

**Target roles:** Software Development Engineer (SDE) / Software Engineering / Full-Stack Engineering internships.

**Engineering interests:** Backend and API design · Data modelling · Developer experience · Application security · Reliable web systems · Applied AI.

**Location:** Indore, Madhya Pradesh, India  
**Education:** B.Tech, Information Technology · 2024–2028  
**Availability:** Open to relevant internships and engineering collaboration.

## What I value as an engineer

- **Correctness before cleverness:** understand constraints, edge cases, and failure modes before optimizing.
- **Readable systems:** meaningful names, small modules, explicit contracts, and documentation that helps the next contributor.
- **Evidence over claims:** link capabilities to code, tests, architecture notes, demos, or independently verifiable records.
- **Practical trade-offs:** choose complexity that fits the problem rather than adding infrastructure for its own sake.
- **Continuous improvement:** measure, review, learn, and refine instead of treating the first working version as the finished product.

## Featured engineering work

The projects below demonstrate different parts of my current engineering practice. Their stated scope is intentionally specific; repository documentation is the source of truth for implementation details and status.

### 01 · [AI MANTHAN 2.0 — Event Platform & PWA](https://github.com/rudraksha127/AI-MANTHAN-2K26)

A mobile-first event platform repository for AI MANTHAN 2.0, built around an installable Progressive Web App experience.

- **Engineering areas:** Next.js App Router, responsive interfaces, service-worker lifecycle, offline fallback, IndexedDB-backed support queue, and content-driven routes.
- **Interesting problem space:** preserving useful user workflows when connectivity is unreliable and keeping event information discoverable across devices.
- **Status:** public source repository; event site: [nex-ai.in](https://www.nex-ai.in).
- **Inspect:** [source](https://github.com/rudraksha127/AI-MANTHAN-2K26) · [project documentation](https://github.com/rudraksha127/AI-MANTHAN-2K26/blob/main/README.md) · [case study](docs/case-studies/ai-manthan.md).

### 02 · [Finance AI — Time-Series Research Pipeline](https://github.com/rudraksha127/Finance-Ai)

A research-only financial-data workflow covering ingestion, validation, feature and label generation, immutable dataset snapshots, baseline model experiments, backtesting, a research inference API, and a dashboard.

- **Engineering areas:** Python, time-series data handling, reproducibility, chronological validation, typed API boundaries, audit trails, and experiment artefacts.
- **Important boundary:** this is a research pipeline; it does not execute live trades or broker orders.
- **Inspect:** [source](https://github.com/rudraksha127/Finance-Ai) · [MVP integration and QA report](https://github.com/rudraksha127/Finance-Ai/blob/main/docs/MVP_INTEGRATION_QA_REPORT.md) · [case study](docs/case-studies/finance-ai.md).

### 03 · [Abhedya-Drishti / FraudLens AI — Transaction Analysis Prototype](https://github.com/rudraksha127/Abhedya-Drishti)

A financial transaction analysis prototype focused on structured data ingestion, vectorized processing, transaction-network exploration, and investigation-triage workflows.

- **Engineering areas:** Next.js, FastAPI, Polars, DuckDB, NumPy-based graph representations, typed frontend/backend contracts, and regression-oriented testing.
- **Important boundary:** analytical outputs are leads for qualified human review. They are not determinations of guilt, legal advice, or claims of court admissibility.
- **Inspect:** [source](https://github.com/rudraksha127/Abhedya-Drishti) · [project documentation](https://github.com/rudraksha127/Abhedya-Drishti/blob/main/README.md) · [case study](docs/case-studies/abhedya-drishti.md).

### 04 · [Developer Portfolio — Interactive Website](https://github.com/rudraksha127/Portfolio)

A modular portfolio website using a modern React/Next.js stack, with sections for projects, skills, education, experience, certifications, and contact.

- **Engineering areas:** component organisation, responsive UI, TypeScript, animation, and a Three.js-based visual layer.
- **Status:** source repository; this profile links to the implementation rather than claiming an independently verified production deployment.
- **Inspect:** [source](https://github.com/rudraksha127/Portfolio) · [project documentation](https://github.com/rudraksha127/Portfolio/blob/main/README.md) · [case study](docs/case-studies/developer-portfolio.md).

<p align="center">
  <img src="./assets/readme/engineering-evidence-map.svg" width="100%" alt="Engineering evidence map connecting projects to frontend, backend, data, AI, architecture, testing, and documentation capabilities." />
</p>

## Engineering practice

I use the following practices as a working engineering checklist. The linked notes describe the standards I aim to apply; individual project repositories show where each practice is implemented.

| Area | What I pay attention to | Evidence to inspect |
|---|---|---|
| Requirements & scope | User journeys, constraints, acceptance criteria, non-goals | Project README, issues, requirements notes |
| Architecture & design | Clear boundaries, separation of concerns, data ownership, explicit trade-offs | Architecture diagrams, design notes, code structure |
| API & backend | Input validation, predictable errors, pagination, auth boundaries, versioning | Routes, schemas, API documentation, tests |
| Data engineering | Schema design, integrity, transactions, indexes, migrations, reproducibility | Models, migrations, queries, pipeline artefacts |
| Testing & quality | Unit, integration and end-to-end coverage where appropriate; regression checks | Test suites, CI results, lint/type checks |
| Security & privacy | Server-side authorization, least privilege, secret handling, safe logging, dependency hygiene | Auth middleware, configuration, security notes |
| Reliability | Timeouts, bounded retries, graceful failure, health checks, recovery paths | Error handling, operational docs, tests |
| Performance | Baselines before optimization, profiling, query analysis, measured trade-offs | Benchmark scripts and dated result reports |
| Delivery | Reproducible setup, environment separation, automated checks, release notes | Setup guides, workflows, deployment configuration |

**How I reason about technical decisions:** problem and constraints → candidate approaches → decision and trade-offs → implementation → tests and observations → documentation. I avoid presenting a design as scalable, secure, or production-ready unless its scope and supporting evidence justify that description.

Read the expanded [engineering standards and working checklist](docs/engineering/engineering-standards.md).

## Computer Science & problem-solving

Core subjects and concepts I actively study and strengthen:

- **Data structures and algorithms:** arrays, strings, hashing, linked lists, stacks, queues, trees, heaps, graphs, tries, and common traversal techniques.
- **Algorithmic patterns:** two pointers, sliding window, binary search, recursion, backtracking, greedy methods, intervals, and dynamic programming.
- **Complexity:** time and space analysis, input constraints, worst-case reasoning, and practical trade-offs.
- **Object-oriented programming:** encapsulation, abstraction, inheritance, polymorphism, composition, and interface-driven design.
- **Database systems:** relational modelling, normalization, SQL, indexing, transactions, isolation, and query plans.
- **Operating systems:** processes, threads, scheduling, synchronization, memory, and deadlocks.
- **Computer networks:** HTTP, DNS, TCP/IP, TLS, latency, and client/server communication.

I treat these as ongoing learning areas, not as a claim of mastery. My coding profiles provide the public problem-solving trail:

<p align="center">
  <a href="https://leetcode.com/rudraksha127"><img src="https://img.shields.io/badge/LeetCode-Profile-FFA116?style=for-the-badge&logo=leetcode&logoColor=111827" alt="LeetCode profile" /></a>
  <a href="https://www.geeksforgeeks.org/user/rudraksha127"><img src="https://img.shields.io/badge/GeeksforGeeks-Profile-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks profile" /></a>
  <a href="https://www.hackerrank.com/rudraksha127"><img src="https://img.shields.io/badge/HackerRank-Profile-00EA64?style=for-the-badge&logo=hackerrank&logoColor=111827" alt="HackerRank profile" /></a>
  <a href="https://www.codechef.com/users/rudraksha127"><img src="https://img.shields.io/badge/CodeChef-Profile-5B4638?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef profile" /></a>
</p>

## Technical toolkit

The table distinguishes technologies visible in public project work from broader tools I am developing familiarity with. It is not a proficiency ranking.

| Category | Selected technologies |
|---|---|
| Languages | C++, Java, Python, JavaScript, TypeScript |
| Frontend | React, Next.js, HTML, CSS, Tailwind CSS |
| Backend & APIs | Node.js, Express, FastAPI, Flask |
| Data & storage | MongoDB, PostgreSQL, DuckDB, Parquet, file-based data pipelines |
| AI & data science | Time-series ML workflows, LLM/API integration, RAG and agentic patterns |
| Cloud & delivery | AWS, Docker, Git, GitHub Actions, CI/CD fundamentals |
| Engineering tools | GitHub, Linux development workflows, API testing and debugging tools |

Technologies are selected per project. I prefer a small, well-understood stack over adding tools that do not solve a concrete requirement.

## Experience & education

### Training and instruction

**Approximately two years of training / teaching experience** across digital productivity and introductory technical subjects.

Topics covered include MS Office, programming fundamentals, PageMaker, Photoshop, and Tally. This experience strengthened my ability to explain concepts, structure learning, and communicate with people at different levels of technical familiarity.

### Education

**B.Tech — Information Technology**  
Acropolis Institute of Technology & Research, Indore  
2024–2028

## Credentials & recognition

I publish certifications and formal achievements with the issuing organisation and a direct verification record wherever available. I intentionally avoid unlinked badge counts and credentials that a reviewer cannot independently verify.

## Current engineering focus

- Strengthening DSA and core Computer Science fundamentals for SDE interviews.
- Improving software design, API boundaries, data modelling, and testing discipline.
- Building full-stack applications with clear ownership, security, and deployment practices.
- Learning to evaluate AI-enabled workflows for correctness, privacy, latency, and cost.

## Contact

I welcome conversations about software engineering internships, practical full-stack projects, applied AI systems, and open-source collaboration.

- **Email:** [luckyudiya@gmail.com](mailto:luckyudiya@gmail.com)
- **LinkedIn:** [linkedin.com/in/rudraksh-udiya](https://www.linkedin.com/in/rudraksh-udiya)
- **GitHub:** [github.com/rudraksha127](https://github.com/rudraksha127)
- **Portfolio source:** [github.com/rudraksha127/Portfolio](https://github.com/rudraksha127/Portfolio)
- **Resume:** [Download PDF](https://raw.githubusercontent.com/rudraksha127/rudraksha127/main/resume.pdf)

---

<p align="center">
  <sub>Build with curiosity. Engineer with care. Make the evidence easy to inspect.</sub>
</p>
