# Human Review

Human Review is a decision surface, not merely an approval button.

## Responsibilities

Depending on the project and gate, Human Review may include:

```text
evidence inspection
acceptance-criteria verification
semantic correctness judgment
scope adherence
ownership review
repair classification
architecture decisions
promotion authorization
deployment authorization
hold / defer / supersede decisions
```

## Review is separate from execution

Agent-generated evidence can be useful and extensive, but:

```text
agent evidence != human acceptance
implementation != acceptance
verification != acceptance
```

The implementation agent should normally return factual status and evidence rather than claiming authority-owned acceptance.

## Independent review

A project can require a separate `REVIEW_ONLY` session or reviewer. Independence means the reviewer is evaluating the subject under a review contract rather than acting as its implementation owner.

Independent review can re-run verification, inspect diffs, compare acceptance criteria, and classify findings.

It must not hide defects to preserve schedule or silently repair the subject unless the review assignment explicitly changes scope.

## Review outcomes

Recommended outcomes:

```text
REVIEW_PASS
REPAIR_REQUIRED
INSUFFICIENT_EVIDENCE
BLOCKED
```

Human/project authority can then decide:

```text
ACCEPTED
DEFERRED
SUPERSEDED
PROMOTION_AUTHORIZED
DEPLOYMENT_AUTHORIZED
```

These decisions may be combined only when the human explicitly intends the combined authority.

## Evidence quality

Review should prefer evidence that is:

- reproducible;
- scoped to the candidate;
- tied to identifiable repository/runtime state;
- sufficient for the acceptance criteria;
- explicit about checks not run;
- explicit about unexpected side effects.

A green test suite is evidence. It is not a substitute for semantic or authority review when those are required.

## Repair handoff

When review finds a defect, the finding should identify:

```text
what failed
which evidence proves it
who owns the defect
what scope may be repaired
whether the current accepted baseline is reopened
what must be re-verified
```

See [`FAILURE_AND_REPAIR.md`](FAILURE_AND_REPAIR.md).
