# Execution Envelope

The Execution Envelope carries volatile assignment state without turning reusable prompts into historical state dumps.

It is the **current bounded delegation layer** between durable governance and live execution.

## Layered context

Workspace Ops separates:

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

Their responsibilities differ:

- **Persistent governance** defines durable rules, invariants, and authority boundaries.
- **Reusable prompts** define stable role and behavior routing.
- **Execution Envelope** defines the current bounded assignment.
- **Live Git/runtime state** is factual authority for current observable state.
- **Current human instruction** supplies the current decision/authorization delta within legitimate scope.

These layers should not be collapsed into one large prompt.

## Preferred shape

```yaml
execution:
  id: STEP-EXAMPLE
  mode: HUMAN_GATED
  kind: implementation
  objective: implement feature X

target:
  project: example-app
  repository: example-app
  track: backend

canonical:
  branch: main
  expected_ref: observed-reference

ownership:
  owner: backend-track
  decision_owner: project-orch

scope:
  owns:
    - application-service
  observes:
    - public-api-contract
  prohibited:
    - infrastructure-redesign

verification:
  required:
    - unit-tests
    - integration-tests

authority:
  acceptance: human
  promotion: human
  deployment: human

stop:
  after_current_unit: true
```

The exact serialization is not the governance authority; the semantics are.

## Volatile fields belong here or in live state

Typical assignment fields include:

```text
current step / operation id
current candidate reference
expected base evidence
temporary worktree
runtime target
current blocker
current NONSTOP range
one-time exception
current required evidence
```

These facts should not be baked into reusable prompt templates.

A value that can be re-resolved reliably from live state does not need to be copied through every handoff merely for convenience.

## Scope and ownership semantics

Three scope concepts are especially useful:

```text
OWNS
OBSERVES
PROHIBITED
```

- `OWNS` grants bounded mutation authority for the assignment, subject to higher governance.
- `OBSERVES` allows read/inspection for integration or evidence.
- `PROHIBITED` makes exclusions explicit.

Ownership remains distinct from reachability:

```text
OBSERVE != OWN
repository access != ownership
consumer need != provider authority
```

See [`OWNERSHIP_AND_ROUTING.md`](OWNERSHIP_AND_ROUTING.md).

## Expected references are drift detectors

A previously observed commit/ref is evidence, not permanent authority.

Before mutation, the executor re-resolves live repository state according to the assignment's preflight rules. If canonical authority is ambiguous or the base changed in a way that invalidates the assignment, execution stops.

```text
expected ref != permanent authority
old prompt state != current preflight
```

See [`EVIDENCE_AND_PROVENANCE.md`](EVIDENCE_AND_PROVENANCE.md).

## Conflict resolution

If lower-level assignment text appears to conflict with higher governance or ownership boundaries:

```text
preserve the conflict
-> do not silently widen authority
-> stop or route the decision to the owning authority
```

A current Human instruction can authorize a bounded exception only where that Human/authority legitimately owns the decision.

## Result handoff

A useful result envelope should report at least:

```text
status
target identity
base/candidate/final provenance
scope executed / not executed
changes
verification
preservation state
canonical status
dependency/decision blockers
review requirement
next handoff
```

`NEXT` describes the handoff. It does not grant new authority.
