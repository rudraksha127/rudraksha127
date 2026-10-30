# Finance AI — Reproducible Time-Series Research Pipeline

> Status: Repository documents an MVP integration and QA run dated 2026-09-08  
> Repository: [rudraksha127/Finance-Ai](https://github.com/rudraksha127/Finance-Ai)  
> QA report: [MVP integration and QA report](https://github.com/rudraksha127/Finance-Ai/blob/main/docs/MVP_INTEGRATION_QA_REPORT.md)

## Problem space

A financial time-series research workflow can produce misleading results when data leakage, inconsistent timestamps, mutable datasets, or optimistic evaluation are allowed. The repository is organised around reproducibility and chronological evaluation rather than live execution.

## Repository-documented pipeline

~~~mermaid
flowchart LR
    A[Historical OHLCV ingestion] --> B[Validation and cleaning]
    B --> C[Feature generation]
    B --> D[Label generation]
    C --> E[Versioned dataset builder]
    D --> E
    E --> F[Baseline model training]
    F --> G[Static / walk-forward backtesting]
    G --> H[Research inference API]
    H --> I[Read-only dashboard]
~~~

The project README describes the following implementation areas:

1. Typed configuration, domain models, structured logging, validation primitives, and separate raw/interim/processed data tiers.
2. Historical OHLCV ingestion through a source adapter, including duplicate/conflict handling and bounded retry behaviour.
3. Cleaning and quality checks with explicit validation reasons and an audit trail.
4. A registry of 52 approved MVP features with versioned Parquet output.
5. Direction labels with a five-trading-day horizon and explicit invalid-window handling.
6. Immutable dataset snapshots, exact ticker/timestamp alignment, chronological train/validation/test splits, and walk-forward purge/embargo handling.
7. Baseline logistic-regression and random-forest training with train-only scaling where applicable.
8. Static and expanding-window walk-forward evaluation with transaction-cost scenarios.
9. A FastAPI research inference service with health/readiness and model/version information endpoints.
10. A React/TypeScript/Vite research dashboard with a typed API client.

## Important scope boundaries

- The project is explicitly research-only. It does not connect to a broker or place live trades.
- The MVP is documented as file-based; PostgreSQL is identified as a later phase, not as the current MVP database.
- Yahoo Finance is described as an unofficial historical data source whose availability and response shape may change.
- Results from small samples can be dominated by feature warm-up and should not be treated as robust financial evidence.

## Testing and evidence

The repository QA report is dated **2026-09-08**. The README at the time of review reports 514 backend and 35 dashboard tests passing. Those are historical repository-reported results, not tests rerun during the profile update. A current claim should link to a fresh CI run tied to the exact commit being discussed.

## Interview discussion points

- Why preserve raw data and write cleaned/intermediate outputs separately?
- How do chronological splits prevent future information from entering model selection?
- Why should transformations be fitted on the training partition only?
- How are duplicate rows and conflicting observations handled?
- What do walk-forward folds reveal that a single static split may not?
- Why is research inference separated from execution?

## Next evidence to add

Record the exact commit used for a fresh test run, publish the test command/output in the repository's CI, and include one reproducible experiment with dataset version, date range, baseline, cost assumptions, and limitations.
