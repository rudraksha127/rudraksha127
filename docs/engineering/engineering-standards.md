# Engineering Standards & Working Checklist

This document describes the practices I aim to apply while building software. It is a practical checklist, not a blanket claim that every listed control is implemented in every repository. Each project case study identifies relevant evidence and known gaps.

## 1. Problem framing and scope

- Identify users, primary jobs-to-be-done, constraints, assumptions, and non-goals.
- Convert ambiguous requirements into observable acceptance criteria.
- Identify failure states and edge cases before implementation.
- Keep a clear distinction between a prototype, an MVP, a deployed application, and a maintained production service.
- Record significant scope changes rather than silently expanding the feature set.

## 2. Architecture and design

- Separate presentation, application/domain logic, and persistence concerns where that separation improves clarity.
- Define module boundaries around cohesive responsibilities.
- Use explicit contracts between frontend, backend, and external services.
- Keep domain rules out of UI-only state and avoid trusting client-side authorization.
- Prefer composition and small interfaces over unnecessary inheritance.
- Record important design decisions with context, options, trade-offs, and consequences.

## 3. API and backend design

- Validate untrusted input at the boundary.
- Use appropriate HTTP methods and status codes.
- Return predictable error shapes without leaking secrets or stack traces.
- Add pagination and filtering for collections that can grow.
- Consider authentication, authorization, rate limiting, idempotency, and API versioning according to risk.
- Document request/response contracts and backward-compatibility expectations.

## 4. Data and database engineering

- Model entities, relationships, ownership, and lifecycle before creating tables or collections.
- Use constraints and transactions to protect invariants.
- Add indexes in response to query patterns and verify them with query plans.
- Treat migrations as versioned application changes.
- Make ingestion pipelines reproducible and preserve source provenance where required.
- Define backup, restore, retention, and deletion expectations for sensitive data.

## 5. Testing and quality

Use the lowest-cost test that gives meaningful confidence, then add broader coverage for high-risk flows.

| Test level | Main purpose |
|---|---|
| Unit | Verify isolated business rules and edge cases |
| Integration | Verify boundaries between modules, storage, and external services |
| API / contract | Verify request validation, responses, and compatibility |
| End-to-end | Verify critical user journeys through the running application |
| Regression | Prevent known defects from returning |
| Performance | Measure behaviour under a defined workload |

Quality checks may include formatting, linting, type checking, dependency review, production builds, and automated tests. Test counts should always be tied to a dated run and an exact commit.

## 6. Security and privacy

- Keep secrets in environment configuration or a dedicated secret manager; never commit them.
- Enforce authorization on the server for every protected operation.
- Apply least privilege to application identities, database roles, and CI permissions.
- Validate and normalize untrusted inputs; use parameterized database operations.
- Protect authentication flows, sessions, tokens, and account recovery.
- Redact credentials and personal data from logs.
- Review dependencies, file upload handling, CORS, security headers, and error responses.
- Define data minimization, retention, consent, and deletion behaviour for personal information.
- Rotate any credential that may have entered repository history; deleting the visible file alone is not enough.

## 7. Reliability and operations

- Use bounded timeouts and retries with backoff for transient failures.
- Avoid retrying non-idempotent operations without an idempotency strategy.
- Provide health/readiness checks where services need operational monitoring.
- Make failures visible through structured logs and actionable error states.
- Design graceful degradation for optional external services.
- Document deployment, rollback, backup, and restore procedures.
- Monitor operational signals where a project is actually deployed and maintained.

## 8. Performance engineering

- Establish a baseline before changing performance-sensitive code.
- Profile the real bottleneck instead of optimizing by intuition.
- Measure database queries, payload size, rendering, CPU, memory, and network latency as relevant.
- Include workload, hardware/runtime, sample size, and date with benchmark results.
- Avoid quoting synthetic benchmarks as real-world user impact.

## 9. Delivery and collaboration

- Use focused commits and descriptive pull requests.
- Keep setup instructions reproducible and environment variables documented without publishing values.
- Run checks before merge and keep workflows limited to the permissions they need.
- Review code for correctness, clarity, security, and maintainability.
- Capture non-obvious decisions and handoff information so another developer can continue the work.

## 10. Decision record template

For important technical choices, record:

1. **Context:** What problem or constraint forced a decision?
2. **Options:** Which viable alternatives were considered?
3. **Decision:** What was selected and why?
4. **Trade-offs:** What became easier, harder, cheaper, or riskier?
5. **Verification:** How will the decision be tested or measured?
6. **Revisit trigger:** What evidence would cause the choice to change?
