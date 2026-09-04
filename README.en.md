# Workspace Ops

[한국어](./README.md) · [English](./README.en.md)

A **human-gated governance framework** for AI-assisted software development.

AI can perform substantial implementation work. That execution capability does not automatically grant authority to accept, promote, deploy, expand scope, or take ownership of adjacent projects.

The central rule is:

```text
execution ability != decision authority
```

Workspace Ops is an opinionated reference governance model for organizing AI-assisted engineering around **bounded execution, evidence, explicit state transitions, independent review, and human-controlled authority**.

## What It Models

Workspace Ops is built around six primitives:

- **Authority** — who may decide.
- **Scope** — what the executor may change.
- **State** — what state the work has actually reached.
- **Evidence** — what proves a state claim.
- **Gate** — what authorizes the next transition.
- **Boundary** — where execution must stop, escalate, or hand off.

These distinctions prevent category errors such as:

```text
can implement != can accept
verified != accepted
review pass != promoted
promotion authorized != promoted
promoted != deployed
```

## Execution Modes

The public baseline defines five reusable execution modes:

- `ANALYSIS_ONLY`
- `HUMAN_GATED`
- `NONSTOP_BOUNDED`
- `REVIEW_ONLY`
- `OPERATION_ONLY`

`NONSTOP_BOUNDED` means **pre-authorized bounded continuation**. It does not mean unrestricted autonomous development.

The authorized range must be finite, and these boundaries remain binding:

- scope expansion
- ownership / authority boundaries
- destructive operations
- evidence conflicts
- architecture or human-judgment requirements
- promotion / deployment authorization

## State and Gates

A typical successful path can be represented as:

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

This is not a single self-advancing state machine.

Different transitions may belong to different authorities and gates. Evidence can support a transition, but evidence alone does not authorize it.

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

Reusable prompts define role and behavior contracts. Current SHAs, branches, worktrees, runtime targets, blockers, and similar volatile values belong in the Execution Envelope or live state.

## Multi-project / Multi-agent Boundaries

Visibility into another project or track does not imply mutation authority.

```text
observe != own
consumer need != provider authority
dependency discovery != provider implementation authorization
```

Frontend, backend, infrastructure, security, review, and operations agents may work in parallel while retaining separate execution and ownership boundaries.

## Repository Guide

For a first read, start here:

- [Concepts](docs/CONCEPTS.md)
- [Quickstart](docs/QUICKSTART.md)
- [Authority Model](governance/AUTHORITY_MODEL.md)
- [State and Gates](governance/STATE_AND_GATES.md)
- [Execution Modes](governance/EXECUTION_MODES.md)
- [Human Review](governance/HUMAN_REVIEW.md)
- [Execution Envelope](governance/EXECUTION_ENVELOPE.md)
- [Boundaries and Stop Conditions](governance/BOUNDARIES_AND_STOP_CONDITIONS.md)
- [Prompt Governance](governance/PROMPT_GOVERNANCE.md)
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

The current `toolkit/` directory documents only a provisional surface. A CLI or orchestration engine should not define governance before the governance contract exists.

## Positioning

Workspace Ops is **one practical approach / reference governance model** for AI-assisted SDLC governance.

It is not presented as an:

```text
industry standard
universal framework
fully autonomous development framework
```

It is generalized from operating experience in a private AI-assisted development workflow, but this repository is not a public copy or mirror of that private workspace. See [Public Disclosure](docs/PUBLIC_DISCLOSURE.md) for details.

## License

Apache License 2.0. See [LICENSE](./LICENSE) for details.
