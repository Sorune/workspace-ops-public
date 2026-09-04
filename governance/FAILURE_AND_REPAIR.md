# Failure and Repair Attribution

## Principle

```text
FAILURE != IMPLEMENTATION FAILURE
```

A failing check is evidence that something is wrong. It is not yet an ownership classification.

## Failure ownership classes

Workspace Ops uses explicit attribution such as:

```text
implementation defect
test defect
environment defect
baseline defect
integration defect
review defect
operations defect
unknown / needs investigation
```

Projects may add domain-specific classes.

## Routing flow

```text
failure
-> evidence inspection
-> ownership classification
-> repair routing
-> bounded repair
-> re-verification
-> review
```

## Why attribution matters

Without attribution, an execution agent can accidentally cross ownership boundaries by repairing whichever adjacent component makes the check green.

That can produce:

- unauthorized product changes;
- concealed baseline defects;
- invalid tests changed to match implementation;
- infrastructure changes made by an application owner;
- repair history hidden inside later unrelated work.

## Repair lineage

If a unit reaches a terminal result and later review finds a defect attributable to it, the repair should remain visibly attached to the original unit.

Conceptually:

```text
STEP N
-> review finds defect
-> N repair
-> re-verification
-> N accepted
-> descendant work
```

Projects may use different naming schemes. The invariant is semantic:

```text
do not hide a repair for earlier work inside unrelated descendant work
```

## Cross-owner failure

If evidence points to another owner:

```text
report the defect
identify the evidence
identify the likely owner
state the current impact
do not mutate the other owner's scope
```

The current executor may continue unrelated work already inside its authorization if the blocker is scoped and the execution mode allows it.

## Evidence conflict

When tests, runtime observations, review evidence, and repository state disagree materially, do not select the most convenient explanation. Classify the conflict as unresolved and escalate to the authority that can decide the next repair scope.
