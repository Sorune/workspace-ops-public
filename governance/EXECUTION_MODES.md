# Execution Modes

The default mode is `HUMAN_GATED` unless project governance selects a stricter default.

## ANALYSIS_ONLY

Purpose:

```text
inspect
audit
classify
compare
plan
recommend
```

Product/source mutation, promotion, deployment, and destructive cleanup are prohibited unless a narrower non-product artifact exception is explicitly stated.

Terminal behavior:

```text
analyze -> report -> stop
```

The executor must not silently turn an obvious recommendation into implementation.

## HUMAN_GATED

Purpose: execute the current authorized unit, verify it, report it, and return control to Human Review.

Normal flow:

```text
preflight
-> execute current unit
-> verify
-> preserve authorized work
-> report
-> stop
```

The executor may fix ordinary implementation-local defects while remaining inside the same authorized unit.

It must not self-accept, start the next project unit, expand scope, promote, deploy, or implement another owner's dependency unless separately authorized.

## NONSTOP_BOUNDED

Purpose: continue across a finite pre-authorized sequence without asking for approval between every successful internal unit.

```text
NONSTOP_BOUNDED
= pre-authorized bounded continuation
!= unrestricted autonomous development
```

The authorization must define at least one finite boundary:

- explicit step list;
- step range;
- deliverable list;
- repository/track scope;
- terminal condition.

The executor stops when:

```text
scope expansion is required
ownership or authority becomes ambiguous
the required base changes in a way that invalidates the assignment
unknown dirty/unpreserved work creates risk
required verification cannot be made green within scope
a semantic conflict requires a project decision
a dependency owned elsewhere blocks progress
an unauthorized destructive action becomes necessary
promotion or deployment is required but not authorized
the bounded terminal condition is reached
the human changes or interrupts the instruction
```

`NONSTOP_BOUNDED` does not automatically authorize cross-project implementation, canonical promotion, deployment, branch deletion, destructive cleanup, or force push.

## REVIEW_ONLY

Purpose: independently inspect an implementation, artifact, operation, or evidence package without becoming its implementation owner.

Default prohibitions:

```text
subject repair
canonical promotion
deployment
```

Recommended review outcomes:

```text
REVIEW_PASS
REPAIR_REQUIRED
BLOCKED
INSUFFICIENT_EVIDENCE
```

A reviewer may produce review evidence when authorized, but should not silently fix the reviewed implementation.

## OPERATION_ONLY

Purpose: execute a bounded operation that the correct authority has already authorized.

Typical operations:

- canonical promotion;
- deployment;
- worktree cleanup;
- runtime restart/recovery;
- inventory/bootstrap;
- observability verification.

Before mutation, the operator re-checks relevant live state. If the real state no longer matches the authorization assumptions, the operator stops rather than improvising a new decision.
