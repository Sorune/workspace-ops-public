# UPSTREAM_GOVERNANCE_REQUEST Template

## Role

Use this template when project work discovers a rule that may deserve broader governance.

The discovering session proposes; it does not self-promote the rule.

## Request

```text
GOVERNANCE CANDIDATE

SOURCE CONTEXT:
OBSERVATION:
CURRENT LOCAL RULE:
WHY REUSABLE:
PROPOSED CLASS:
  PROJECT_LOCAL / DOMAIN_COMMON / WORKSPACE_DEFAULT / WORKSPACE_INVARIANT

EVIDENCE:
KNOWN EXCEPTIONS:
AFFECTED OWNERS:
RISK IF NOT STANDARDIZED:

NO GOVERNANCE PROMOTION PERFORMED.
```

## Promotion tests

Ask:

- Does the rule remain valid if the project name changes?
- Is it safety/authority critical?
- Can projects legitimately specialize it?
- Is there independent reuse evidence?
- Would duplication create competing authorities?
- Is the rule stable rather than current roadmap state?
- Can compliance be interpreted and evidenced?

The receiving governance authority decides whether to keep local, defer, reject, classify, or authorize promotion.
