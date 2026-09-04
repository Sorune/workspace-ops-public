# Toolkit

Status: `CONTRACT-FIRST / PROVISIONAL / NO STABLE CLI`

The Toolkit is the future **reference tooling layer that consumes, validates, and partially enforces Workspace Ops governance**.

It is not the source of governance authority.

```text
tooling implements governance
governance is not inferred from tooling
```

## Purpose

The Toolkit should reduce manual governance drift and make important checks reproducible without turning Workspace Ops into a mandatory orchestration platform.

Candidate responsibilities include:

```text
contract validation
configuration / governance doctor checks
live-state preflight
provenance-aware evidence checks
gate precondition evaluation
authority-receipt inspection
project / ownership boundary validation
provider / agent adapter checks
optional multi-project coordination
```

## Design principles

### 1. Contracts before commands

A command must implement a documented semantic contract.

Do not invent governance through CLI side effects.

### 2. Read-only first

Inspection and validation should generally mature before mutation automation.

```text
inspect
-> explain
-> validate
-> only then automate bounded mutation
```

### 3. Evidence is scoped and fresh

Tool output should identify the target, source, procedure, and relevant freshness limitations.

```text
old observation != permanent authority
static validation != runtime validation
```

### 4. Sensitive transitions fail closed

If required authority, ownership, preconditions, or live state cannot be established, sensitive mutation should stop rather than silently downgrade protection.

### 5. Tool capability != decision authority

A tool may technically be able to merge, deploy, or change state without owning the decision to do so.

```text
can execute transition
!= can authorize transition
```

### 6. Adapters are not the semantic architecture

Git providers, CI systems, AI agents, or deployment platforms are adapters. Core contracts should remain provider-neutral where practical.

## Capability layers

```text
Governance specification
        ↓
Machine-readable contracts
        ↓
Validators / doctor
        ↓
Evidence / gate tooling
        ↓
Agent / provider adapters
        ↓
Optional multi-project orchestration
```

See [`CONTRACTS.md`](CONTRACTS.md) and [`ROADMAP.md`](ROADMAP.md).

## Provisional command surface

The following names illustrate possible capabilities only. They are not stable CLI contracts.

### Inspection / validation

```text
workspace status
workspace doctor
workspace validate
workspace project inspect
workspace envelope validate
workspace evidence inspect
workspace gate check
workspace authority inspect
```

### Later bounded mutation / adapters

```text
workspace project reconcile
workspace authority receipt
workspace agent inspect
workspace agent reconcile
workspace session inspect
```

Exact verbs, flags, storage formats, and command grouping remain intentionally open until the underlying contracts stabilize.

## What should not become implicit state

The Toolkit should avoid becoming an opaque authority database.

Durable project decisions should remain in the appropriate governance/project systems, while live facts should be read from their factual sources where practical.

Examples:

```text
Git history / refs
project governance and current control state
CI/runtime evidence
explicit authority artifacts
provider runtime state
```

A local cache may improve performance or support bounded runtime guards, but cache state must not silently replace its authoritative source.

## Non-goals

The public Toolkit is not currently intended to be:

```text
a mandatory always-on daemon
a universal project manager
an autonomous roadmap planner
a hidden approval database
a replacement for Git/CI/runtime truth
a framework that automatically merges or deploys successful agent work
```

## Current maturity

```text
Governance specification: PRESENT
Synthetic examples: PRESENT
Reusable prompt templates: PRESENT
Machine-readable stable schemas: NOT YET STABLE
Validators / doctor: NOT IMPLEMENTED
Evidence / gate engine: NOT IMPLEMENTED
Agent adapters: NOT IMPLEMENTED
Multi-project orchestration: NOT IMPLEMENTED
```

The absence of implementation is deliberate: the public repository is still defining the smallest reusable governance contract before committing to a tooling architecture.
