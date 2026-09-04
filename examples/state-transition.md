# State Transition Example

A feature implementation completes and all required local checks pass.

```text
STATUS: VERIFIED
```

Evidence:

```text
unit tests: PASS
integration tests: PASS
lint: PASS
```

This does **not** make the feature accepted.

An independent reviewer evaluates the candidate:

```text
REVIEW_PASS
```

The project authority then decides:

```text
ACCEPTED
```

The accepted candidate still remains non-canonical until promotion is separately authorized:

```text
PROMOTION_AUTHORIZED
```

An operator re-checks Git state and performs the authorized promotion:

```text
PROMOTED
```

Production is unchanged. Deployment requires another decision:

```text
DEPLOYMENT_AUTHORIZED
```

Only after the bounded deployment operation and health evidence does the runtime become:

```text
DEPLOYED
```

The important point is that successful evidence supports transitions; it does not collapse the gates.
