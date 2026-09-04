# Quickstart

This quickstart applies the governance model manually. No CLI is required.

## 1. Define authority and ownership

For each project, record:

```text
project authority
track/subsystem owners
review authority
promotion authority
deployment authority
important exclusions
```

Keep authority and ownership distinct:

```text
who may decide?
!=
which project / track / domain does that decision apply to?
```

See [`../governance/OWNERSHIP_AND_ROUTING.md`](../governance/OWNERSHIP_AND_ROUTING.md) and use [`../examples/project-registry.yaml`](../examples/project-registry.yaml) as a synthetic reference.

## 2. Select an execution mode

Default to:

```text
HUMAN_GATED
```

Use `NONSTOP_BOUNDED` only when a finite sequence is explicitly pre-authorized.

Remember:

```text
NONSTOP_BOUNDED
= different review cadence
!= weaker authority boundaries
```

See [`../governance/EXECUTION_MODES.md`](../governance/EXECUTION_MODES.md).

## 3. Build an Execution Envelope

Keep volatile assignment data in the envelope rather than in reusable prompt templates.

Resolve at least:

```text
target identity
current objective
execution mode
owner / decision owner
owned / observed / prohibited scope
required evidence
stop condition
```

Start from [`../examples/execution-envelope.yaml`](../examples/execution-envelope.yaml).

## 4. Execute and collect evidence

The executor implements only owned scope, runs required verification, preserves work, and reports factual state.

Prefer:

```text
STATUS: VERIFIED
REVIEW: HUMAN_REVIEW_REQUIRED
```

over an implementation agent declaring project acceptance.

Evidence should identify the candidate/target and be fresh enough for the decision it supports. See [`../governance/EVIDENCE_AND_PROVENANCE.md`](../governance/EVIDENCE_AND_PROVENANCE.md).

## 5. Review independently

Use the [`INDEPENDENT_REVIEW`](../prompts/templates/INDEPENDENT_REVIEW.md) template when independent review is required.

```text
self-verification != independent review
review authority != implementation ownership
```

Classify defects before repairing them.

## 6. Make authority-owned decisions

Keep these separate unless the owning Human/authority explicitly combines them:

```text
ACCEPTED
PROMOTION_AUTHORIZED
DEPLOYMENT_AUTHORIZED
```

Evidence may establish readiness. It does not grant the decision authority.

## 7. Execute sensitive operations with fresh preflight

Before promotion, deployment, or destructive cleanup, re-check the relevant live Git/runtime state.

```text
old observed state != current authority assumption
```

If assumptions changed, stop and re-authorize rather than extending stale authority.

## 8. Route cross-owner needs instead of seizing scope

When execution discovers a need owned elsewhere:

```text
observe
-> preserve evidence
-> identify owner
-> route request / handoff
-> owning authority decides
```

Do not mutate another owner's scope merely to make the current check green.

## 9. Improve governance deliberately

When a project discovers a reusable rule, submit a governance candidate instead of copying it everywhere.

Use [`../prompts/templates/UPSTREAM_GOVERNANCE_REQUEST.md`](../prompts/templates/UPSTREAM_GOVERNANCE_REQUEST.md).

## 10. Add tooling only after the contract is clear

The public Toolkit is intentionally contract-first.

See [`../toolkit/README.md`](../toolkit/README.md) before implementing validators, adapters, or orchestration commands.
