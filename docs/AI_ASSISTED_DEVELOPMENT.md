# AI-Assisted Development

## The problem

Modern coding agents can inspect large repositories, implement features, run tests, operate Git, and interact with deployment systems.

That creates a governance question:

```text
What is the agent allowed to decide?
```

Workspace Ops treats this as distinct from capability.

## Bounded execution

A strong execution agent can be given wide implementation freedom while remaining bounded by:

- project ownership;
- repository scope;
- track/subsystem scope;
- execution mode;
- required evidence;
- explicit stop conditions;
- promotion/deployment gates.

This avoids both extremes:

```text
approval required for every trivial edit
```

and:

```text
unrestricted autonomous roadmap expansion
```

`NONSTOP_BOUNDED` is the middle ground: finite continuation authorized in advance.

## Evidence before claims

The executor should report facts that can be reviewed:

```text
what changed
what did not change
what checks ran
what failed
what was preserved
which candidate was verified
what decision is still required
```

A useful system makes it difficult to confuse a green check with a broader authority decision.

## Multi-agent development

Parallel agents should have ownership boundaries, not just labels.

For example:

```text
frontend executor
backend executor
security reviewer
infra operator
independent reviewer
project orchestrator
```

Each can be highly capable while remaining unable to seize another role's authority.

## Human role

The human is not necessarily typing every command. Human authority is most valuable at semantic gates:

- intent;
- ownership;
- scope expansion;
- acceptance;
- architecture;
- risk acceptance;
- promotion;
- deployment;
- disclosure.

The operational surface can increasingly become machine-enforced while these decision boundaries remain explicit.

## Long-term direction

Workspace Ops can evolve from documentation into executable governance:

```text
documentation
-> governance
-> machine-readable contract
-> validation
-> evidence/gate tooling
-> agent adapters
-> orchestration
```

P0 intentionally stops at the governance/reference-contract layer.
