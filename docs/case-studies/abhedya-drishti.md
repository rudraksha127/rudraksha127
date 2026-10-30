# Abhedya-Drishti / FraudLens AI — Transaction Analysis Prototype

> Status: Public prototype repository  
> Repository: [rudraksha127/Abhedya-Drishti](https://github.com/rudraksha127/Abhedya-Drishti)

## Problem space

Large transaction datasets can be difficult to inspect through flat tables alone. This prototype explores structured ingestion, fast analytical processing, graph-based relationship exploration, and investigator-oriented triage views.

## Repository-documented components

The project README describes:

- A Next.js and React frontend for an investigative workspace.
- A FastAPI backend for pipeline and analysis operations.
- Polars and DuckDB for columnar processing and analytical queries.
- NumPy compressed sparse row (CSR) arrays for graph representation and traversal.
- Typed API contracts and frontend interfaces for graph, ledger, and money-trail data.
- Regression and end-to-end test suites for selected workflows.
- Documentation covering product requirements, technical architecture, data profiling, security, QA, and performance experiments.

## Conceptual data flow

~~~mermaid
flowchart TD
    A[Transaction data] --> B[Ingestion and validation]
    B --> C[Columnar processing]
    C --> D[Relationship / graph construction]
    D --> E[Subgraph and money-trail analysis]
    E --> F[Investigator workspace]
    F --> H[Human review and independent checks]
~~~

This is a conceptual summary of the repository's documented workflow. It is not a statement that every deployment has completed legal, operational, or forensic certification.

## Engineering discussion

- **Columnar processing:** use vectorized operations for analytical workloads and avoid unnecessary row-by-row processing.
- **Graph representation:** CSR arrays provide compact adjacency storage for traversal-oriented operations.
- **Data provenance:** retain links between aggregate views and underlying transaction-level records.
- **Truncation visibility:** make result limits explicit so the UI does not imply that a partial subgraph is complete.
- **Frontend/backend contract:** typed interfaces reduce ambiguity between API responses and rendered investigation views.
- **Human review:** automated outputs should support prioritisation, not replace qualified investigation.

## Safety, legal, and evidentiary boundary

This profile describes a software prototype for analytical triage. It does **not** claim that its outputs establish guilt, satisfy statutory admissibility requirements, replace qualified investigation, or constitute legal advice. The legal and compliance statements in the project repository require independent expert review before being repeated as verified claims.

## Verification

The repository README reports a 271-test backend suite and documents additional frontend and end-to-end checks. These counts were not rerun during this profile update. Any current test claim should link to a fresh workflow run and the exact commit tested.

## Next evidence to add

- A short, synthetic-data demo that contains no personal or real financial information.
- A reproducible benchmark with dataset characteristics, hardware/runtime, commands, and raw results.
- A security review that clearly distinguishes implemented controls from planned controls.
- A documented personal-contribution summary and team attribution.
