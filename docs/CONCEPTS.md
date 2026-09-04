# Concepts

## Workspace Ops in one sentence

Workspace Ops is a reference governance model for allowing substantial AI-assisted execution without automatically transferring project decision authority to the executor.

## The six primitives

### Authority

Who may decide?

### Scope

What may this execution change, inspect, or explicitly not touch?

### State

What has the work factually reached, and which authority owns the next transition?

### Evidence

What reproducible information supports the state claim?

### Gate

What evidence and authority are required for the next transition?

### Boundary

Where must execution stop, escalate, or hand off?

## The control loop

```text
human intent / authority
-> bounded assignment
-> execution agent
-> Git / CI / runtime
-> evidence
-> review / gates
-> acceptance / promotion / deployment decisions
```

This can be understood as a possible future AI-assisted SDLC control layer, but the P0 baseline is governance specification rather than a finished control-plane product.

## Ownership model

Workspace Ops treats multi-agent work as an ownership system rather than merely a role list.

An agent can see another track and still lack authority to mutate it.

```text
visibility != ownership
consumer need != provider authority
review authority != implementation ownership
operational authority != product authority
```

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

Evidence is strongest when tied to an identifiable candidate and reproducible procedure.

## Authority Receipt

An Authority Receipt is a future contract candidate for answering:

```text
Why was this sensitive action authorized?
```

It should bind an action to a target, authorizer, scope, exclusions, and invalidation conditions.

See [`../examples/authority-receipt.yaml`](../examples/authority-receipt.yaml).
