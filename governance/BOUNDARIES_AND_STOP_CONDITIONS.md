# Boundaries and Stop Conditions

Execution is bounded not only by files but by authority.

## Boundary types

### Ownership boundary

Another project, track, subsystem, or authority owns the decision or mutation.

### Project boundary

A dependency or adjacent defect belongs to another project.

### Repository boundary

The assignment does not authorize mutation of another repository.

### Architecture boundary

Progress requires a product/architecture decision not already settled by authority.

### Operational boundary

Progress requires promotion, deployment, runtime mutation, credentials, or infrastructure action outside the current authorization.

### Destructive-operation boundary

Progress requires deletion, reset, force push, data destruction, irreversible cleanup, or another destructive action not explicitly authorized.

### Human-judgment boundary

Acceptance, exception handling, disclosure, risk acceptance, architecture, or other semantic judgment requires a human/project decision.

### Public/private disclosure boundary

Publication may expose sensitive operational state, credentials, private identifiers, topology, customer information, or history that was not explicitly allowlisted.

## Stop conditions

The executor stops and reports when:

```text
scope expansion is required
ownership is ambiguous
authority sources conflict
a destructive operation is required but unauthorized
private/public disclosure is uncertain
credentials or secrets may be involved
live state invalidates the authorized base
unknown dirty/unpreserved work creates risk
required evidence cannot be produced within scope
a cross-project dependency becomes blocking
architecture authority is required
acceptance/promotion/deployment decisions are required but absent
the explicit bounded terminal condition is reached
the human changes or revokes the instruction
```

## Stop does not mean failure

A correct stop can be the successful enforcement of governance.

Recommended handoff:

```text
BOUNDARY REACHED
TYPE:
OBSERVED STATE:
EVIDENCE:
WHY CURRENT AUTHORITY IS INSUFFICIENT:
OWNER / DECISION REQUIRED:
SAFE STATE PRESERVED:
```

## Preservation first

When existing work is dirty, unpushed, or uncertain:

```text
unknown work must not be discarded
```

Preserve or escalate before cleanup. A clean local tree and a pushed branch are different preservation facts; neither by itself proves promotion.

## Boundary crossing requires new authority

A next action may be obvious, useful, or technically easy and still require a new authorization. Convenience does not expand the execution envelope.
