# Quickstart

This quickstart uses the governance model manually. No CLI is required.

## 1. Define durable ownership

For each project, record:

```text
project authority
track/subsystem owners
review authority
promotion authority
deployment authority
important exclusions
```

Use [`../examples/project-registry.yaml`](../examples/project-registry.yaml) as a synthetic reference.

## 2. Select an execution mode

Default to:

```text
HUMAN_GATED
```

Use `NONSTOP_BOUNDED` only when a finite sequence is explicitly pre-authorized.

See [`../governance/EXECUTION_MODES.md`](../governance/EXECUTION_MODES.md).

## 3. Build an Execution Envelope

Keep volatile assignment data in the envelope rather than in reusable prompt templates.

Start from [`../examples/execution-envelope.yaml`](../examples/execution-envelope.yaml).

## 4. Execute and collect evidence

The executor implements only owned scope, runs required verification, preserves work, and reports factual state.

Prefer:

```text
STATUS: VERIFIED
REVIEW: HUMAN_REVIEW_REQUIRED
```

over an implementation agent declaring project acceptance.

## 5. Review independently

Use the [`INDEPENDENT_REVIEW`](../prompts/templates/INDEPENDENT_REVIEW.md) template when independent review is required.

Classify defects before repairing them.

## 6. Make authority-owned decisions

Keep these separate unless the human explicitly combines them:

```text
ACCEPTED
PROMOTION_AUTHORIZED
DEPLOYMENT_AUTHORIZED
```

## 7. Execute sensitive operations with fresh preflight

Before promotion, deployment, or destructive cleanup, re-check the relevant live Git/runtime state.

If assumptions changed, stop and re-authorize rather than extending stale authority.

## 8. Improve governance deliberately

When a project discovers a reusable rule, submit a governance candidate instead of copying it everywhere.

Use [`../prompts/templates/UPSTREAM_GOVERNANCE_REQUEST.md`](../prompts/templates/UPSTREAM_GOVERNANCE_REQUEST.md).
