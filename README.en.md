# Workspace Ops

[한국어](./README.md) · [English](./README.en.md)

A **human-gated governance framework** for AI-assisted software development.

AI can perform substantial implementation work. That execution capability does not automatically grant authority to accept, promote, deploy, expand scope, or take ownership of adjacent projects.

The central rule is:

```text
execution ability != decision authority
```

Workspace Ops is an opinionated reference governance model for organizing AI-assisted engineering around **bounded execution, ownership-aware scope, evidence-backed state, explicit gates, independent review, and human-controlled authority**.

## What It Models

Workspace Ops is built around seven primitives:

- **Authority** — who may decide.
- **Ownership** — which project, track, domain, or artifact that authority applies to.
- **Scope** — what the executor may change or observe.
- **State** — what state the work has actually reached.
- **Evidence** — what proves a state claim.
- **Gate** — what evidence and authority are required for the next transition.
- **Boundary** — where execution must stop, escalate, or hand off.

These distinctions prevent category errors such as:

```text
can implement != can accept
observe != own
verified != accepted
review pass != promoted
promotion authorized != promoted
promoted != deployed
```

## Ownership and Routing

Visibility into another project or track does not imply mutation authority.

```text
visibility != ownership
observe != own
consumer need != provider authority
routing != authorization
```

Workspace Ops treats multi-agent work as an **ownership-preserving routing problem**, not merely as a list of roles. A consumer owns its need, a provider owns provider-local work, and provider delivery still does not authorize consumer integration automatically.

## Execution Modes

The public baseline defines five reusable execution modes:

- `ANALYSIS_ONLY`
- `HUMAN_GATED`
- `NONSTOP_BOUNDED`
- `REVIEW_ONLY`
- `OPERATION_ONLY`

`NONSTOP_BOUNDED` means **pre-authorized bounded continuation**. It does not mean unrestricted autonomous development.

```text
HUMAN_GATED vs NONSTOP_BOUNDED
= different review cadence
!= different safety / authority model
```

The authorized range must remain finite, and stop conditions such as scope expansion, ownership or authority boundaries, destructive actions, evidence conflicts, architecture or human-judgment requirements, and promotion/deployment authorization remain binding.

## State and Gates

Workspace Ops does not flatten all progress labels into one executor-controlled enum.

At minimum it distinguishes orthogonal planes such as:

```text
Execution state
Review state
Decision / acceptance state
Operational state
```

A typical successful narrative can be represented as:

```text
IMPLEMENTED
  -> VERIFIED
  -> REVIEW_PASS
  -> ACCEPTED
  -> PROMOTION_AUTHORIZED
  -> PROMOTED
  -> DEPLOYMENT_AUTHORIZED
  -> DEPLOYED
```

This is not a single self-advancing state machine. Different transitions may belong to different authorities and gates.

## Evidence and Provenance

Evidence can establish facts, but it does not create authorization.

```text
Evidence establishes facts.
Evidence does not grant authority.
```

Tests, CI, Git provenance, browser/runtime acceptance, review artifacts, and deployment health should be interpreted together with their candidate/target, procedure, freshness, and environment.

```text
old observed ref != permanent authority
static inspection != runtime execution
Linux pass != Windows pass
```

Before sensitive mutation, the live state that materially affects the authorization assumptions should be revalidated.

## Human Review

Human Review is not reduced to an approval button.

Depending on the project, it can include:

- evidence inspection
- acceptance-criteria verification
- semantic-correctness judgment
- scope / ownership review
- repair classification
- architecture decisions
- promotion authorization
- deployment authorization

Agent-generated evidence and Human acceptance are intentionally distinct.

## Execution Envelope

Stable governance is separated from volatile execution state.

```text
Persistent governance
        +
Reusable prompt
        +
Execution envelope
        +
Live repository/runtime state
        +
Current human instruction
```

Reusable prompts define stable role and behavior routing. Current SHAs, branches, worktrees, runtime targets, blockers, and similar volatile values belong in the Execution Envelope or are resolved from live state.

## Repository Guide

For a first read, start here:

- [Concepts](docs/CONCEPTS.md)
- [Quickstart](docs/QUICKSTART.md)
- [Authority Model](governance/AUTHORITY_MODEL.md)
- [Ownership and Routing](governance/OWNERSHIP_AND_ROUTING.md)
- [State and Gates](governance/STATE_AND_GATES.md)
- [Evidence and Provenance](governance/EVIDENCE_AND_PROVENANCE.md)
- [Execution Modes](governance/EXECUTION_MODES.md)
- [Human Review](governance/HUMAN_REVIEW.md)
- [Execution Envelope](governance/EXECUTION_ENVELOPE.md)
- [Failure and Repair](governance/FAILURE_AND_REPAIR.md)
- [Boundaries and Stop Conditions](governance/BOUNDARIES_AND_STOP_CONDITIONS.md)
- [Prompt Governance](governance/PROMPT_GOVERNANCE.md)
- [Toolkit Direction](toolkit/README.md)
- [Public Disclosure](docs/PUBLIC_DISCLOSURE.md)

Reusable prompt templates live under [`prompts/templates`](prompts/templates/).

Synthetic examples live under [`examples`](examples/).

## Contracts Before Tooling

Workspace Ops deliberately follows this implementation order:

```text
governance
-> machine-readable contracts
-> validators / doctor
-> evidence and gate tooling
-> agent adapters
-> multi-project orchestration
```

The `toolkit/` directory describes the future **reference tooling surface that consumes and validates the governance model**. A CLI or orchestration engine should not define governance before the governance contract exists.

## Positioning

Workspace Ops is **one practical approach / reference governance model** for AI-assisted SDLC governance.

The thesis can be summarized as:

```text
It governs not what an AI can technically do,
but what it is authorized to decide, mutate, and advance.
```

It is not presented as an:

```text
industry standard
universal framework
fully autonomous development framework
```

It is generalized from operating experience in a private AI-assisted development workflow, but this repository is not a public copy or mirror of that private workspace. See [Public Disclosure](docs/PUBLIC_DISCLOSURE.md) for details.

## License

Apache License 2.0. See [LICENSE](./LICENSE) for details.
