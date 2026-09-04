# Failure and Repair Attribution

## Principle

```text
FAILURE != IMPLEMENTATION FAILURE
```

A failing check is evidence that something is wrong. It is not yet a root-cause or ownership classification.

## Failure attribution

Projects should classify failure narrowly enough to route repair to the correct owner.

Useful classes may include:

```text
implementation defect
test defect
environment defect
baseline defect
integration defect
review defect
operations defect
governance defect
unknown / needs investigation
```

This list is illustrative rather than a mandatory universal taxonomy. Projects may add domain-specific classes or use a smaller set when the evidence does not justify finer attribution.

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
route the repair or dependency to the owning authority
```

The current executor may continue unrelated work already inside its authorization if the blocker is scoped and the execution mode allows it.

See [`OWNERSHIP_AND_ROUTING.md`](OWNERSHIP_AND_ROUTING.md).

## Evidence conflict

When tests, runtime observations, review evidence, and repository state disagree materially, do not select the most convenient explanation.

```text
preserve conflicting evidence
-> classify known / unknown
-> avoid stronger state claims
-> route the unresolved repair or decision scope
```

See [`EVIDENCE_AND_PROVENANCE.md`](EVIDENCE_AND_PROVENANCE.md).
