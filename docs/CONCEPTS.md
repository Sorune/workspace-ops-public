# Concepts

## Workspace Ops in one sentence

Workspace Ops is a reference governance model for allowing substantial AI-assisted execution without automatically transferring decision authority or ownership to the executor.

## The seven primitives

### Authority

Who may decide?

### Ownership

Whose project, track, domain, artifact, or operational surface does that authority apply to?

### Scope

What may this execution change, inspect, or explicitly not touch?

### State

What has the work factually reached, and on which state plane?

### Evidence

What reproducible information supports the state claim, with what provenance and freshness?

### Gate

What evidence, authority, and preconditions are required for the next transition?

### Boundary

Where must execution stop, escalate, or hand off?

## Why ownership is separate

Authority and ownership answer different questions.

```text
can decide this kind of action
!= owns every target where that action is technically possible
```

Examples:

```text
visibility != ownership
review authority != implementation ownership
operational authority != product authority
consumer need != provider authority
```

See [`../governance/OWNERSHIP_AND_ROUTING.md`](../governance/OWNERSHIP_AND_ROUTING.md).

## Orthogonal state planes

Workspace Ops does not model progress as one executor-controlled enum.

A typical system needs distinct planes such as:

```text
execution state
review state
decision / acceptance state
operational state
```

A common successful narrative may look linear, but each transition can belong to a different authority and gate.

```text
VERIFIED != ACCEPTED
REVIEW_PASS != ACCEPTED
ACCEPTED != PROMOTION_AUTHORIZED
PROMOTION_AUTHORIZED != PROMOTED
PROMOTED != DEPLOYED
```

See [`../governance/STATE_AND_GATES.md`](../governance/STATE_AND_GATES.md).

## The control loop

```text
human intent / authority
-> ownership + bounded assignment
-> execution agent
-> Git / CI / runtime
-> evidence
-> factual state
-> review
-> authority gate
-> authorized transition
```

This can be understood as a possible future AI-assisted SDLC control layer, but the current public baseline is governance specification rather than a finished control-plane product.

## Bounded autonomy

`NONSTOP_BOUNDED` is not a weaker safety mode.

```text
HUMAN_GATED
vs
NONSTOP_BOUNDED
= different review cadence
!= different authority model
```

`NONSTOP_BOUNDED` means a Human or owning authority has pre-authorized a finite continuation range. The same ownership, destructive-action, promotion, deployment, and stop boundaries still apply.

## Evidence model

Evidence should answer both **what happened** and **what state it applies to**.

Examples include:

- tests;
- lint/typecheck;
- browser/runtime acceptance;
- CI status;
- repository provenance;
- diff inspection;
- review artifacts;
- deployment health.

Evidence is strongest when tied to an identifiable candidate, reproducible procedure, and sufficiently fresh observation.

```text
Evidence establishes facts.
Evidence does not grant authority.
```

See [`../governance/EVIDENCE_AND_PROVENANCE.md`](../governance/EVIDENCE_AND_PROVENANCE.md).

## Execution Envelope

The Execution Envelope is the current bounded delegation layer between durable governance and live execution.

```text
persistent governance
+
reusable prompt
+
execution envelope
+
live repository/runtime state
+
current human instruction
```

Stable policy should not be copied into every prompt, and volatile state should not be baked into reusable prompts.

## Decision provenance and Authority Receipt

Fact provenance explains why an observed state is believed.

Decision provenance explains who authorized a transition and under what scope or conditions.

An Authority Receipt is a provisional contract candidate for recording bounded decision provenance around a sensitive action.

It can answer:

```text
Why was this action authorized?
For which target and scope?
What is excluded?
What preconditions or evidence were assumed?
What invalidates the authorization?
```

See [`../examples/authority-receipt.yaml`](../examples/authority-receipt.yaml).
