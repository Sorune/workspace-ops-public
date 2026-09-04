# Toolkit Direction

Status: `CONTRACT ONLY / DEFERRED`

The P0 baseline defines governance first. It intentionally does not implement a large CLI or orchestration engine.

## Candidate future surface

Provisional ideas:

```text
workspace init
workspace status
workspace inventory
workspace doctor
workspace project add
workspace project status
workspace prompt render
workspace prompt validate
workspace gate check
workspace review
workspace evidence collect
workspace authority receipt
```

Names and interfaces are not stable contracts.

## Implementation order

```text
P0  governance specification
P1  machine-readable contracts
P2  validators / doctor
P3  evidence / gate tooling
P4  agent adapters
P5  multi-project orchestration
```

## P1 contract candidates

- Execution Envelope schema;
- Authority Receipt schema;
- state-transition contract;
- evidence contract;
- project-boundary contract.

## Design constraint

The CLI must implement governance; it must not invent governance accidentally through command behavior.

Sensitive commands should eventually be able to answer:

```text
what authority allows this action?
what target is bound to that authority?
what evidence/preconditions are required?
what invalidates the authorization?
```
