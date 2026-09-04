# Workspace Ops

A human-gated governance framework for AI-assisted software development.

AI can perform substantial implementation work. That capability does not automatically grant authority to accept, promote, deploy, expand scope, or take ownership of adjacent projects.

The central rule is:

```text
execution ability != decision authority
```

Workspace Ops is an opinionated reference governance model for organizing AI-assisted engineering around bounded execution, evidence, explicit state transitions, independent review, and human-controlled authority.

## What it models

Workspace Ops uses six primitives:

- **Authority** — who may decide.
- **Scope** — what the executor may change.
- **State** — what the work has actually reached.
- **Evidence** — what supports a state claim.
- **Gate** — what authorizes the next transition.
- **Boundary** — where execution must stop, escalate, or hand off.

These primitives prevent common category errors:

```text
can implement != can accept
verified != accepted
review pass != promoted
promotion authorized != promoted
promoted != deployed
```

## Execution modes

The baseline defines five reusable modes:

- `ANALYSIS_ONLY`
- `HUMAN_GATED`
- `NONSTOP_BOUNDED`
- `REVIEW_ONLY`
- `OPERATION_ONLY`

`NONSTOP_BOUNDED` means **pre-authorized bounded continuation**. It does not mean unrestricted autonomous development. The range must be finite, and authority, ownership, destructive-operation, evidence-conflict, and human-judgment boundaries remain binding.

## State and gates

A typical successful path is:

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

This is not a single self-advancing state machine. Different transitions belong to different authorities. Evidence can support a transition without authorizing it.

## Human review

Human Review is not reduced to an approval button. Depending on the project, it can include:

- evidence inspection;
- acceptance-criteria verification;
- semantic correctness judgment;
- scope and ownership review;
- repair classification;
- architecture decisions;
- promotion authorization;
- deployment authorization.

Agent-generated evidence and human acceptance are intentionally distinct.

## Repository guide

Start here:

- [Concepts](docs/CONCEPTS.md)
- [Quickstart](docs/QUICKSTART.md)
- [Authority model](governance/AUTHORITY_MODEL.md)
- [State and gates](governance/STATE_AND_GATES.md)
- [Execution modes](governance/EXECUTION_MODES.md)
- [Human Review](governance/HUMAN_REVIEW.md)
- [Execution Envelope](governance/EXECUTION_ENVELOPE.md)
- [Boundaries and stop conditions](governance/BOUNDARIES_AND_STOP_CONDITIONS.md)
- [Prompt governance](governance/PROMPT_GOVERNANCE.md)
- [Public disclosure](docs/PUBLIC_DISCLOSURE.md)

Reusable prompt templates live under [`prompts/templates`](prompts/templates/). Synthetic examples live under [`examples`](examples/).

## Contracts before tooling

The implementation direction is deliberately staged:

```text
governance
-> machine-readable contracts
-> validators / doctor
-> evidence and gate tooling
-> agent adapters
-> multi-project orchestration
```

The `toolkit/` directory currently documents a provisional surface only. The governance contract comes first.

## Positioning

Workspace Ops is one practical approach to AI-assisted SDLC governance. It is not presented as an industry standard, a universal process, or a fully autonomous development framework.
