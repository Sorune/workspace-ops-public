# Repository Validation

Workspace Ops uses repository-level validation to reduce accidental public disclosure and broken documentation without embedding private workspace data into the public repository.

## Principle

```text
PUBLIC VALIDATOR
!=
PRIVATE DATA LIST
```

Validators must use generic, explainable rules. They must not contain private project names, machine names, local paths, internal hosts, private commit identifiers, or other values copied from a private environment.

## Checks

### Public safety

`scripts/validate_public_safety.py` scans UTF-8 text files for high-confidence classes of accidental disclosure, including:

- private-key material markers;
- common high-confidence token formats;
- credential-bearing URLs;
- credential-like assignments with non-placeholder values;
- absolute per-user filesystem paths;
- RFC1918/link-local IPv4 literals.

The validator intentionally reports the category and location without echoing the matched secret value.

It is a guardrail, not a complete secret-management system. Human review remains required for ambiguous disclosure, customer data, topology, proprietary identifiers, or context that cannot be recognized reliably by a generic pattern.

### Markdown local links

`scripts/validate_markdown_links.py` validates repository-local Markdown links and rejects links that:

- resolve outside the repository;
- point to a missing file or directory.

External URLs and fragment-only anchors are outside this check.

## Run locally

```bash
python scripts/validate_public_safety.py
python scripts/validate_markdown_links.py
```

Both validators use the Python standard library only.

## CI

`.github/workflows/public-validation.yml` runs both checks for pull requests and pushes to `main`.

The workflow is read-only:

```text
permissions:
  contents: read
```

No validator authorizes publication, acceptance, promotion, or deployment. A green validation result is repository hygiene evidence only.

## False positives and exceptions

Do not solve a false positive by inserting the real private value into an allowlist or denylist.

Preferred responses are:

1. make synthetic examples visibly synthetic;
2. generalize the published artifact;
3. improve the generic validator rule when it is objectively over-broad;
4. use Human Review when disclosure meaning depends on context.

```text
validator pass != disclosure authorization
```
