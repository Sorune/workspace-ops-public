# Prompt Governance

## Principle

Prompts should carry current intent, not duplicate the entire governance system.

```text
prompt
= role + execution pointer + dynamic context
!= complete policy copy
!= complete project history
!= canonical repository evidence
```

## Context layers

A practical resolution model is:

```text
1. current human instruction
2. persistent workspace governance
3. project governance
4. project current state
5. track/ownership governance
6. current step specification
7. execution envelope / temporary constraints
8. live repository/runtime evidence for factual state
```

This ordering is semantic, not a claim that every AI runtime automatically discovers every file.

A lower layer may specialize a default only within legitimate authority. It must not silently override a higher-level invariant.

## Decision authority vs factual authority

Two dimensions must not be confused:

```text
human instruction -> current decision authority
Git/runtime state -> current factual authority
```

A prompt-supplied commit string does not make that commit current. A chat transcript does not prove repository state. Conversely, current Git state does not grant a project decision that no authority made.

## Reusable prompt families

The baseline provides:

- `PROJECT_ORCH`
- `PROJECT_OPS`
- `TRACK_IMPLEMENTATION`
- `INDEPENDENT_REVIEW`
- `UPSTREAM_GOVERNANCE_REQUEST`

Templates define role, boundaries, expected input, and result shape. They intentionally omit volatile references.

## When repetition is acceptable

A stable rule may be repeated when:

- the canonical authority is not reliably reachable by the executor;
- emergency safety emphasis is necessary;
- the current assignment explicitly specializes a default;
- repetition resolves a known ambiguity;
- the text itself is under review.

Repeated prose does not become a second independent authority.

## Governance promotion

An implementation or review session may discover a reusable rule.

Recommended lifecycle:

```text
observed
-> proposed
-> reviewed
-> classified
-> promotion authorized
-> promoted
```

The discovering executor may propose and provide evidence. It does not automatically gain authority to make the rule global.

## Context compression goal

Good prompt governance makes mature handoffs smaller while preserving stronger authority:

```text
stable rules -> canonical governance
project facts -> project governance/current state
volatile assignment -> execution envelope
live facts -> Git/runtime preflight
```
