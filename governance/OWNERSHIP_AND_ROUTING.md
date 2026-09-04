# Ownership and Routing

## Principle

Workspace Ops treats ownership as distinct from authority and technical reachability.

```text
visibility != ownership
observe != own
consumer need != provider authority
routing != authorization
```

## Authority vs ownership

These concepts answer different questions.

```text
Authority
= what decisions may this actor make?

Ownership
= which project, track, domain, artifact, or operational surface does that authority apply to?
```

An actor may have authority to request, review, route, or physically execute an action without owning the product semantics of the target.

Examples:

```text
review authority != implementation ownership
operational authority != product authority
consumer authority != provider implementation authority
promotion execution capability != promotion decision ownership
```

## Boundary types

Multi-agent work should distinguish at least:

- **execution boundary** — what this assignment may execute;
- **ownership boundary** — whose domain or artifact is being changed;
- **review boundary** — who may independently evaluate evidence;
- **promotion boundary** — who may authorize or execute canonical promotion;
- **deployment boundary** — who may authorize or execute runtime mutation.

These boundaries can overlap, but they must not be assumed to be identical.

## Ownership-preserving routing

When work discovers a need owned elsewhere, the safe pattern is:

```text
observe need
-> identify owner
-> preserve evidence and impact
-> route request / handoff
-> owning authority decides
```

Routing a request does not open implementation work automatically.

A handoff should preserve:

```text
source identity
target owner
observed need or decision
relevant evidence/reference
what the receiver owns
what the receiver must not assume
requested next action
stop/return condition
```

## Consumer / provider separation

A consumer owns its need and integration decision.

A provider owns provider-local design, sequencing, implementation, and delivery decisions.

```text
consumer decides need
provider decides provider work
consumer decides integration
```

Provider delivery does not force consumer adoption, and consumer urgency does not seize provider roadmap authority.

## Ownership is not a role list

A role name is useful only when it resolves an actual authority and ownership boundary.

```text
role label != authority by itself
session identity != ownership by itself
repository access != ownership by itself
```

Projects may define their own roles and tracks. Workspace-level governance should preserve those local ownership boundaries rather than flattening them into a universal agent hierarchy.
