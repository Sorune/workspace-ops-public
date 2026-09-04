# Authority Model

## Principle

Workspace Ops separates **capability** from **authority**.

A system may be technically capable of performing an action without being authorized to decide that the action should occur.

```text
can implement != can accept
can verify != can promote
can promote != can deploy
visibility != ownership
```

## Authority classes

The baseline distinguishes these authority classes.

### Human authority

May make decisions that require human judgment, including acceptance, architecture changes, scope expansion, promotion authorization, deployment authorization, and governance changes.

Human authority may be delegated explicitly, but delegation must be bounded and discoverable.

### Project authority

Owns product semantics, project roadmap decisions, project-local ownership, project acceptance criteria, and project-specific exceptions to non-invariant defaults.

### Review authority

Owns the independent evaluation of evidence against the review contract. Review authority does not automatically include implementation ownership or promotion authority.

### Promotion authority

May authorize a candidate to become canonical project state. Promotion authorization and the physical promotion operation are separate concerns.

### Deployment authority

May authorize mutation of a runtime or production environment. Promotion does not imply deployment authorization.

### Operational authority

May execute authorized repository, workspace, promotion, deployment, cleanup, or runtime operations. Operational authority does not become product authority by performing those actions.

## Execution authority

An execution agent receives bounded authority through the current assignment.

Typical executor-owned actions:

```text
inspect current state
implement within owned scope
repair implementation-local defects within scope
run required verification
preserve authorized work
produce factual evidence
report blockers and decision requirements
```

Typical executor-prohibited decisions unless separately authorized:

```text
self-acceptance
scope expansion
architecture ownership changes
cross-project implementation
canonical promotion
deployment
destructive cleanup
governance promotion
```

## Authority must be explicit

Authorization should answer:

```text
who authorized the action?
what action was authorized?
what target does it apply to?
what scope is included?
what is excluded?
what evidence or preconditions are required?
when does the authorization expire or stop applying?
```

For sensitive transitions, this information can be represented as an **Authority Receipt**. See [`../examples/authority-receipt.yaml`](../examples/authority-receipt.yaml).

## Observation is not ownership

An executor may need to inspect adjacent systems for integration evidence.

```text
OBSERVE != OWN
```

A missing capability in another project, a visible defect in another track, or repository access does not grant mutation authority over that owner.

The correct response is to report the dependency or decision gap and route it to the owning authority.
