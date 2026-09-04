# Execution Envelope

The Execution Envelope carries volatile assignment state without turning reusable prompts into historical state dumps.

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

- **Persistent governance** defines durable rules and invariants.
- **Reusable prompts** define role and behavior.
- **Execution Envelope** defines the current assignment.
- **Live Git/runtime state** is factual authority for current observable state.
- **Current human instruction** supplies current decision authority within legitimate scope.

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

## Volatile fields belong here

Typical envelope fields include:

```text
current step / operation id
current branch or candidate reference
expected base evidence
temporary worktree
runtime target
current blocker
current NONSTOP range
one-time exception
current required evidence
```

These facts should not be baked into reusable prompt templates.

## Scope semantics

Three scope concepts are especially useful:

```text
OWNS
OBSERVES
PROHIBITED
```

- `OWNS` grants bounded mutation authority for the assignment.
- `OBSERVES` allows read/inspection for integration or evidence.
- `PROHIBITED` makes exclusions explicit.

```text
OBSERVE != OWN
```

## Expected references are drift detectors

A previously observed commit/ref is evidence, not permanent authority.

Before mutation, the executor re-resolves live repository state according to the assignment's preflight rules. If canonical authority is ambiguous or the base changed in a way that invalidates the assignment, execution stops.

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
