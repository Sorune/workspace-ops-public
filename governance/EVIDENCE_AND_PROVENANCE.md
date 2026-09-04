# Evidence and Provenance

## Principle

Evidence establishes facts. Evidence does not grant decision authority.

```text
tests passed != accepted
review evidence != promotion authorization
promotion evidence != deployment authorization
```

## What evidence should answer

Useful evidence should identify:

```text
what happened?
which candidate / target does it apply to?
how was it observed or reproduced?
when was it observed?
is it still current enough for the decision being made?
```

## Evidence classes

Common evidence classes include:

- unit and integration tests;
- lint and typecheck;
- browser or runtime acceptance;
- CI/check status;
- Git branch, commit, diff, ancestry, and working-tree state;
- artifact or package provenance;
- runtime health and deployment observations;
- manual inspection;
- independent review artifacts.

Projects may require stronger or domain-specific evidence.

## Provenance

Evidence is stronger when its provenance is explicit.

Useful provenance fields include:

```text
source
candidate / target
procedure or command
result
reference / commit / artifact
platform or environment when relevant
observed_at
```

A conclusion without enough provenance may still be useful as a lead, but it should not be silently treated as reproducible acceptance evidence.

## Freshness and revalidation

Previously observed facts may become stale.

```text
observed ref != permanent authority
old green check != proof of current state
old prompt state != current preflight
```

Before a sensitive mutation, re-read the live state that can materially change the authorization assumptions.

Examples:

```text
remote target ref
source candidate ref
branch ancestry
working-tree preservation state
runtime/deployment target
current required checks
```

If revalidation invalidates the assumptions under which an action was authorized, stop rather than improvising a new decision.

## Evidence conflict

When credible evidence sources disagree materially:

```text
preserve the conflict
-> classify what is known / unknown
-> avoid selecting the most convenient explanation
-> route the unresolved decision or repair scope
```

`INSUFFICIENT_EVIDENCE` and `BLOCKED` are safer than inventing a stronger state.

## Fact provenance vs decision provenance

Keep these separate.

```text
Fact provenance
= why do we believe the observed state?

Decision provenance
= who decided that the evidence was sufficient for a transition, under what scope and conditions?
```

An Authority Receipt is one possible artifact for decision provenance around a sensitive transition. It does not replace the underlying factual evidence.

## Evidence strength is scoped

Evidence must not be generalized beyond what it actually proves.

Examples:

```text
Linux runtime pass != Windows runtime pass
static inspection != runtime execution
one candidate pass != future candidate pass
local repository state != remote canonical state
```

Governance should preserve these limitations rather than flattening them into a single `PASS` label.
