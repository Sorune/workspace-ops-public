# State and Gates

## Do not flatten unlike states

Workspace Ops does not treat all progress labels as one executor-controlled enum.

State is separated into four layers because different authorities own different transitions.

### 1. Execution state

Executor-observable factual state:

```text
PLANNED
IN_PROGRESS
IMPLEMENTED
VERIFIED
BLOCKED
NO_CHANGE_REQUIRED
```

`VERIFIED` means the required executor-side checks completed successfully under the current verification contract. It does not mean the work is accepted.

### 2. Review state

Independent review result:

```text
HUMAN_REVIEW_REQUIRED
REVIEW_PASS
REPAIR_REQUIRED
INSUFFICIENT_EVIDENCE
REVIEW_REJECTED
```

`REVIEW_PASS` means the reviewer found the evidence acceptable under the review contract. It does not mean promotion or deployment occurred.

### 3. Decision state

Authority-owned project decision:

```text
ACCEPTED
DEFERRED
SUPERSEDED
PROMOTION_AUTHORIZED
DEPLOYMENT_AUTHORIZED
```

Projects may use their own acceptance vocabulary, but it must preserve the semantic separation between evidence, acceptance, promotion authorization, and deployment authorization.

### 4. Operational state

Observable external mutation:

```text
CANDIDATE_ONLY
PROMOTED
DEPLOYED
```

## Common successful path

```text
IMPLEMENTED
  -> VERIFIED
  -> REVIEW_PASS
  -> ACCEPTED
  -> PROMOTION_AUTHORIZED
  -> PROMOTED
  -> DEPLOYMENT_AUTHORIZED
  -> DEPLOYED
```

The arrows are gates, not automatic transitions.

## Mandatory distinctions

```text
VERIFIED != ACCEPTED
REVIEW_PASS != ACCEPTED
ACCEPTED != PROMOTION_AUTHORIZED
PROMOTION_AUTHORIZED != PROMOTED
PROMOTED != DEPLOYMENT_AUTHORIZED
DEPLOYMENT_AUTHORIZED != DEPLOYED
```

## Gate model

Each transition should resolve:

```text
FROM STATE
TO STATE
REQUIRED EVIDENCE
AUTHORITY OWNER
PRECONDITIONS
STOP / FAILURE RESULT
```

Example:

| Transition | Evidence owner | Decision/operation owner |
|---|---|---|
| `IMPLEMENTED -> VERIFIED` | executor / CI | verification contract |
| `VERIFIED -> REVIEW_PASS` | reviewer | review authority |
| `REVIEW_PASS -> ACCEPTED` | review evidence | project/human authority |
| `ACCEPTED -> PROMOTION_AUTHORIZED` | accepted candidate provenance | promotion authority |
| `PROMOTION_AUTHORIZED -> PROMOTED` | Git preflight / operation evidence | operational authority |
| `PROMOTED -> DEPLOYMENT_AUTHORIZED` | release/runtime readiness evidence | deployment authority |
| `DEPLOYMENT_AUTHORIZED -> DEPLOYED` | deployment preflight / health evidence | operational authority |

## Failure and hold states

A failed transition should preserve what is known rather than invent a stronger status.

Common outcomes include:

```text
VERIFICATION_FAILED
REPAIR_REQUIRED
INSUFFICIENT_EVIDENCE
BLOCKED
DEFERRED
SUPERSEDED
```

Repair ownership is classified separately. See [`FAILURE_AND_REPAIR.md`](FAILURE_AND_REPAIR.md).
