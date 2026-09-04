# Public Disclosure

Workspace Ops was derived from practical experience operating a private AI-assisted development workspace.

This repository is **not** a publication, fork, mirror, export, or history continuation of that private workspace.

## What this repository contains

It contains newly written public artifacts that generalize governance concepts such as:

- human/AI authority separation;
- bounded execution;
- evidence-based verification;
- review and acceptance gates;
- promotion/deployment separation;
- multi-project ownership boundaries;
- repair attribution;
- prompt and execution-envelope separation.

## What this repository does not contain

It is intentionally not a record of private operational state.

It does not publish:

```text
credentials or secrets
private keys
private machine identifiers or local OS user identifiers
private network topology
live deployment targets
private project registries
private worktree state
private acceptance reports
private runtime evidence
private commit provenance
customer/client data
unpublished private roadmaps
private dependency graphs
private Git history
```

Public GitHub account identity and repository ownership are naturally visible as part of this public repository and are not considered private operational identifiers under this disclosure.

## Examples

Examples in this repository are sanitized, generalized, or synthetic.

Names such as `example-app`, `example-api`, and `example-infra` are illustrative. Example branches, references, decisions, and state transitions do not represent the current state of any private project.

## Historical independence

The public repository uses independent Git history. Private commits are not transplanted as public provenance.

## Product authority independence

The private workspace is an origin and operational proving ground, not a permanent hidden authority over the public product.

During early extraction, private operational experience may inform candidate public contracts through explicit review and generalization.

As the public implementation matures, the public repository's own documented contracts, accepted implementation, and releases should become authoritative for public product behavior.

A private operational environment may then consume the public product with private governance overlays, project state, machine state, or adapters that are intentionally not published.

New private experience may produce a candidate improvement, but it does not silently change public semantics.

```text
PRIVATE EXPERIENCE
!= AUTOMATIC PUBLIC AUTHORITY
```

This preserves both directions:

```text
early:
private proving ground
-> extraction / generalization
-> public product

mature:
public product authority
-> consumed by private environment

private new friction
-> explicit candidate / review
-> possible public evolution
```

## Publication model

Publication is allowlist-based:

```text
private operational experience
-> concept extraction
-> generalization
-> newly authored public artifact
```

The default is not to copy private artifacts and remove a denylist of sensitive fields.
