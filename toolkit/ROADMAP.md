# Toolkit Roadmap

Status: `DIRECTIONAL / NOT A RELEASE COMMITMENT`

The Toolkit roadmap follows the rule:

```text
governance first
contracts second
tooling third
```

Each stage should consume the semantics established by the previous stage rather than redefine them.

## P0 — Governance specification

Goal:

```text
define authority, ownership, scope, state, evidence, gates, boundaries, review, and execution-mode semantics
```

Current status:

```text
PRESENT
```

Primary artifacts:

```text
governance/
docs/
prompts/templates/
examples/
```

## P1 — Machine-readable contracts

Goal:

```text
represent the smallest reusable governance contracts without committing to a large orchestration architecture
```

Candidate contracts:

- Execution Envelope;
- Ownership / project boundary;
- Evidence record;
- State transition / gate;
- Authority Receipt;
- Result / handoff.

Current status:

```text
SEMANTIC CANDIDATES DOCUMENTED
SCHEMA NOT STABLE
```

See [`CONTRACTS.md`](CONTRACTS.md).

## P2 — Validators / doctor

Goal:

```text
detect governance and context defects before mutation
```

Candidate capabilities:

```text
validate envelope completeness
validate ownership routing
validate state/gate contract shape
check stale/missing evidence references
check contradictory authority declarations
doctor project configuration
explain stop conditions
```

Preferred initial behavior is read-only.

Exit criterion should be reproducible diagnostics against synthetic fixtures before any mutation automation depends on them.

## P3 — Evidence / gate tooling

Goal:

```text
collect or inspect evidence and evaluate gate preconditions without conflating readiness with authorization
```

Candidate capabilities:

```text
Git provenance inspection
CI/check evidence adapters
runtime evidence adapters
freshness/revalidation checks
gate readiness evaluation
authority-receipt validation
result/handoff rendering
```

Important:

```text
gate ready != transition authorized
```

A gate tool may say that evidence/preconditions are satisfied while still requiring an owning Human or authority decision.

## P4 — Agent / provider adapters

Goal:

```text
bind governance contracts to actual AI execution providers and developer tools
```

Potential concerns:

```text
provider session identity
prompt / envelope injection
capability declaration
preflight invocation
result capture
session ownership enforcement
```

Provider-specific behavior must not silently redefine core governance semantics.

## P5 — Optional multi-project orchestration

Goal:

```text
coordinate dependency routing, ownership handoff, and bounded execution across multiple projects without centralizing product authority
```

Candidate capabilities:

```text
project/owner routing
dependency request coordination
provider delivery provenance
consumer integration handoff
cross-project gate visibility
```

This stage is optional. Workspace Ops remains useful as a governance specification even if no centralized orchestrator is built.

## Explicitly deferred design decisions

The roadmap does not yet choose:

```text
programming language
CLI framework
schema language
local database
always-on coordinator
remote control plane
provider SDK
Git hosting assumptions
CI vendor
deployment platform
```

These should follow demonstrated contract needs.

## Promotion rule for Toolkit ideas

A tooling idea should advance when it provides at least one of:

```text
less repeated manual context
stronger authority clarity
reproducible evidence
safer stop behavior
detectable governance drift
useful provider-neutral enforcement
```

Avoid promoting tooling that mainly adds ceremony or creates a second source of truth.

## Non-goal

The roadmap is not a plan to maximize automation.

The target is:

```text
automate repeatable governance checks
without automating away the authority boundaries they protect
```
