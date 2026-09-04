# State and Gates

## State is not one executor-controlled enum

Workspace Ops models progress as several **orthogonal state planes** because different facts and transitions belong to different authorities.

A linear success path is useful for explanation, but it must not imply that one actor may self-advance the whole lifecycle.

## 1. Execution state

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

## 2. Review state

Independent review result:

```text
HUMAN_REVIEW_REQUIRED
REVIEW_PASS
REPAIR_REQUIRED
INSUFFICIENT_EVIDENCE
REVIEW_REJECTED
```

`REVIEW_PASS` means the reviewer found the evidence acceptable under the review contract. It does not itself grant project acceptance, promotion, or deployment authority.

## 3. Decision / acceptance state

Authority-owned project or governance decision:

```text
ACCEPTED
DEFERRED
SUPERSEDED
PROMOTION_AUTHORIZED
DEPLOYMENT_AUTHORIZED
```

Projects may use their own acceptance vocabulary, such as `PASS` or `FROZEN`, provided they preserve the semantic separation between verification, review, acceptance, promotion authorization, and deployment authorization.

## 4. Operational state

Observable external mutation:

```text
CANDIDATE_ONLY
PROMOTED
DEPLOYED
```

Operational state records what actually happened, not merely what was authorized.

## Common successful narrative

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

The narrative crosses several state planes; it is not one self-advancing state machine.

## Mandatory distinctions

```text
IMPLEMENTED != VERIFIED
VERIFIED != ACCEPTED
REVIEW_PASS != ACCEPTED
ACCEPTED != PROMOTION_AUTHORIZED
PROMOTION_AUTHORIZED != PROMOTED
PROMOTED != DEPLOYMENT_AUTHORIZED
DEPLOYMENT_AUTHORIZED != DEPLOYED
```

## Gate model

Each sensitive transition should resolve:

```text
FROM STATE / OBSERVED CONDITION
TO STATE / REQUESTED EFFECT
REQUIRED EVIDENCE
EVIDENCE FRESHNESS / REVALIDATION
AUTHORITY OWNER
OWNERSHIP BOUNDARY
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
| `PROMOTION_AUTHORIZED -> PROMOTED` | fresh Git preflight / operation evidence | operational authority |
| `PROMOTED -> DEPLOYMENT_AUTHORIZED` | release/runtime readiness evidence | deployment authority |
| `DEPLOYMENT_AUTHORIZED -> DEPLOYED` | deployment preflight / health evidence | operational authority |

Evidence may satisfy transition preconditions. Evidence does not create the authority to approve the transition.

## Failure and hold outcomes

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

A failure outcome is not yet a root-cause classification. Repair ownership is classified separately. See [`FAILURE_AND_REPAIR.md`](FAILURE_AND_REPAIR.md).

For evidence provenance and freshness, see [`EVIDENCE_AND_PROVENANCE.md`](EVIDENCE_AND_PROVENANCE.md).
