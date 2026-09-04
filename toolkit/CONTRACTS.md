# Toolkit Contract Candidates

Status: `PROVISIONAL SEMANTIC CONTRACTS / SCHEMA NOT STABLE`

This document identifies the smallest machine-readable contracts that could support future Workspace Ops tooling.

The goal is not to freeze a serialization format early. The goal is to make the semantics explicit enough that future validators and adapters do not invent different meanings.

## Contract 1 — Execution Envelope

Purpose:

```text
represent the current bounded delegation
```

Minimum semantic fields should be able to resolve:

```text
execution id / operation id
mode
objective
target project / repository / track when relevant
ownership / decision owner
owned / observed / prohibited scope
required verification
stop condition
current bounded exceptions
```

Volatile references may be included for drift detection, but must not become permanent authority.

Source governance: [`../governance/EXECUTION_ENVELOPE.md`](../governance/EXECUTION_ENVELOPE.md).

## Contract 2 — Ownership / Project Boundary

Purpose:

```text
identify who owns which semantic or operational surface
```

Useful fields may include:

```text
project identity
repository identity
track / domain identity
owner
decision owner
review owner
promotion owner
deployment owner
observed dependencies / routing targets
explicit exclusions
```

The contract must preserve:

```text
visibility != ownership
routing != authorization
```

Source governance: [`../governance/OWNERSHIP_AND_ROUTING.md`](../governance/OWNERSHIP_AND_ROUTING.md).

## Contract 3 — Evidence Record

Purpose:

```text
represent a factual claim with enough provenance to evaluate its scope and freshness
```

Useful fields may include:

```text
evidence type
candidate / target
procedure / command
result
source / reference
platform / environment
observed_at
freshness / revalidation requirement
known limitations
```

The contract must not imply that evidence grants authority.

Source governance: [`../governance/EVIDENCE_AND_PROVENANCE.md`](../governance/EVIDENCE_AND_PROVENANCE.md).

## Contract 4 — State Transition / Gate

Purpose:

```text
evaluate whether a requested transition has the required evidence, ownership, authority, and preconditions
```

Useful fields may include:

```text
current state plane / condition
requested effect
required evidence
required authority class
ownership target
preconditions
revalidation checks
failure / stop result
```

A gate evaluator should be able to return a factual result such as:

```text
READY_FOR_AUTHORITY_DECISION
BLOCKED_MISSING_EVIDENCE
BLOCKED_STALE_EVIDENCE
BLOCKED_AUTHORITY_MISMATCH
BLOCKED_OWNERSHIP_MISMATCH
BLOCKED_PRECONDITION
```

These names are illustrative, not canonical public tokens yet.

Source governance: [`../governance/STATE_AND_GATES.md`](../governance/STATE_AND_GATES.md).

## Contract 5 — Authority Receipt

Purpose:

```text
record bounded decision provenance for a sensitive authorized action
```

Useful fields may include:

```text
action
target
authorized_by
authorized_scope
excluded_scope
preconditions / evidence references
issued_at
expiry / invalidation conditions
revocation reference
```

The receipt should answer why an operation is authorized, not replace the factual evidence or the authority source.

Source example: [`../examples/authority-receipt.yaml`](../examples/authority-receipt.yaml).

## Contract 6 — Result / Handoff

Purpose:

```text
return factual execution state and preserve ownership while handing control to the next authority
```

Useful fields may include:

```text
status
target identity
provenance
scope executed / not executed
verification
preservation state
known limitations
blockers / decision requests
review requirement
next handoff
```

Important:

```text
NEXT != new authority
handoff != ownership transfer unless explicitly authorized
```

## Later contract candidates

These should remain deferred until repeated implementation demand justifies them:

```text
provider capability contract
execution-session identity / lease contract
multi-project dependency graph
cross-machine coordination lease
runtime deployment adapter contract
```

The public Toolkit should not promote these merely because a private implementation exists somewhere. Public contracts should be generalized and independently justified.

## Validation rule

A machine-readable schema is useful only when its validator can explain semantic failures.

Prefer diagnostics such as:

```text
field is missing because target ownership cannot be resolved
observed evidence is stale for this transition
authority receipt excludes deployment
provider capability cannot enforce requested session isolation
```

over opaque `schema invalid` failures.

## Serialization

YAML, JSON, TOML, or another representation may be used later.

```text
serialization != semantics
```

Schema format should be selected after the contract stabilizes enough to justify compatibility commitments.
