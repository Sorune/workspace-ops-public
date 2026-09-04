# Workspace Ops

[한국어](./README.md) · [English](./README.en.md)

AI-assisted software development를 위한 **human-gated governance framework**입니다.

AI는 상당한 규모의 구현 작업을 수행할 수 있습니다. 하지만 그 실행 능력이 acceptance, promotion, deployment, scope expansion, 또는 인접 프로젝트의 ownership을 자동으로 부여하지는 않습니다.

핵심 원칙은 다음과 같습니다.

```text
execution ability != decision authority
```

Workspace Ops는 AI-assisted engineering을 **bounded execution, ownership-aware scope, evidence-backed state, explicit gates, independent review, human-controlled authority**를 중심으로 구성하기 위한 opinionated reference governance model입니다.

## 무엇을 모델링하는가

Workspace Ops는 일곱 가지 primitive를 중심으로 합니다.

- **Authority** — 누가 결정할 수 있는가.
- **Ownership** — 그 권한이 어느 project/track/domain에 적용되는가.
- **Scope** — executor가 무엇을 변경하거나 관찰할 수 있는가.
- **State** — 작업이 실제로 어떤 상태에 도달했는가.
- **Evidence** — 해당 state claim을 무엇이 증명하는가.
- **Gate** — 다음 transition에 어떤 evidence와 authority가 필요한가.
- **Boundary** — 어디에서 실행을 멈추고 escalate 또는 handoff해야 하는가.

이 구분은 다음과 같은 category error를 방지합니다.

```text
can implement != can accept
observe != own
verified != accepted
review pass != promoted
promotion authorized != promoted
promoted != deployed
```

## Ownership과 Routing

다른 project나 track을 볼 수 있다는 사실은 mutation authority를 의미하지 않습니다.

```text
visibility != ownership
observe != own
consumer need != provider authority
routing != authorization
```

Workspace Ops는 multi-agent work를 단순 role list가 아니라 **ownership-preserving routing problem**으로 봅니다. Consumer는 자신의 필요를 결정하고, provider는 provider-local work를 결정하며, delivery가 발생해도 consumer integration은 다시 consumer authority가 결정합니다.

## Execution Modes

Public baseline은 다섯 가지 reusable execution mode를 정의합니다.

- `ANALYSIS_ONLY`
- `HUMAN_GATED`
- `NONSTOP_BOUNDED`
- `REVIEW_ONLY`
- `OPERATION_ONLY`

`NONSTOP_BOUNDED`는 **pre-authorized bounded continuation**을 의미합니다. unrestricted autonomous development를 의미하지 않습니다.

```text
HUMAN_GATED vs NONSTOP_BOUNDED
= review cadence difference
!= safety / authority model difference
```

실행 범위는 유한해야 하며 scope expansion, ownership/authority boundary, destructive operation, evidence conflict, architecture/human judgment, promotion/deployment authorization 같은 stop condition은 계속 유효합니다.

## State와 Gate

Workspace Ops는 progress label을 하나의 executor-controlled enum으로 다루지 않습니다.

최소한 다음과 같은 orthogonal state plane을 구분합니다.

```text
Execution state
Review state
Decision / acceptance state
Operational state
```

일반적인 successful narrative는 다음과 같이 표현할 수 있습니다.

```text
IMPLEMENTED
  -> VERIFIED
  -> REVIEW_PASS
  -> ACCEPTED
  -> PROMOTION_AUTHORIZED
  -> PROMOTED
  -> DEPLOYMENT_AUTHORIZED
  -> DEPLOYED
```

하지만 이것은 하나의 self-advancing state machine이 아닙니다. 각 transition은 서로 다른 authority와 gate에 의해 결정될 수 있습니다.

## Evidence와 Provenance

Evidence는 사실을 확립할 수 있지만 authorization을 만들지는 않습니다.

```text
Evidence establishes facts.
Evidence does not grant authority.
```

Tests, CI, Git provenance, browser/runtime acceptance, review artifacts, deployment health 같은 evidence는 **candidate/target, procedure, freshness, environment**와 함께 해석해야 합니다.

```text
old observed ref != permanent authority
static inspection != runtime execution
Linux pass != Windows pass
```

Sensitive mutation 전에는 authorization assumption에 영향을 주는 live state를 다시 확인하는 것이 기본입니다.

## Human Review

Human Review는 단순한 approval button이 아닙니다.

프로젝트에 따라 다음을 포함할 수 있습니다.

- evidence inspection
- acceptance criteria verification
- semantic correctness judgment
- scope / ownership review
- repair classification
- architecture decision
- promotion authorization
- deployment authorization

Agent-generated evidence와 Human acceptance는 의도적으로 분리됩니다.

## Execution Envelope

Stable governance와 현재 작업의 volatile state를 분리합니다.

```text
Persistent governance
        +
Reusable prompt
        +
Execution envelope
        +
Live repository/runtime state
        +
Current human instruction
```

Reusable prompt에는 role과 behavior contract를 두고, 현재 SHA, branch, worktree, runtime target, current blocker 같은 값은 Execution Envelope 또는 live state에서 resolve합니다.

## Repository Guide

처음 읽는다면 다음 순서를 권장합니다.

- [Concepts](docs/CONCEPTS.md)
- [Quickstart](docs/QUICKSTART.md)
- [Authority Model](governance/AUTHORITY_MODEL.md)
- [Ownership and Routing](governance/OWNERSHIP_AND_ROUTING.md)
- [State and Gates](governance/STATE_AND_GATES.md)
- [Evidence and Provenance](governance/EVIDENCE_AND_PROVENANCE.md)
- [Execution Modes](governance/EXECUTION_MODES.md)
- [Human Review](governance/HUMAN_REVIEW.md)
- [Execution Envelope](governance/EXECUTION_ENVELOPE.md)
- [Failure and Repair](governance/FAILURE_AND_REPAIR.md)
- [Boundaries and Stop Conditions](governance/BOUNDARIES_AND_STOP_CONDITIONS.md)
- [Prompt Governance](governance/PROMPT_GOVERNANCE.md)
- [Toolkit Direction](toolkit/README.md)
- [Public Disclosure](docs/PUBLIC_DISCLOSURE.md)

Reusable prompt template은 [`prompts/templates`](prompts/templates/)에 있습니다.

Synthetic example은 [`examples`](examples/)에 있습니다.

## Contracts Before Tooling

Workspace Ops의 구현 순서는 의도적으로 다음과 같이 잡습니다.

```text
governance
-> machine-readable contracts
-> validators / doctor
-> evidence and gate tooling
-> agent adapters
-> multi-project orchestration
```

`toolkit/`은 이 governance를 **소비하고 검증하는 future reference tooling surface**입니다. CLI나 orchestration engine이 governance를 먼저 정의하게 하지 않습니다.

## Positioning

Workspace Ops는 AI-assisted SDLC governance를 위한 **one practical approach / reference governance model**입니다.

이를 가장 압축하면:

```text
It governs not what an AI can technically do,
but what it is authorized to decide, mutate, and advance.
```

다음과 같이 주장하지 않습니다.

```text
industry standard
universal framework
fully autonomous development
```

실제 private AI-assisted development workflow에서 얻은 운영 경험을 일반화한 것이지만, 이 repository는 private workspace의 공개본이나 mirror가 아닙니다. 자세한 내용은 [Public Disclosure](docs/PUBLIC_DISCLOSURE.md)를 참고하세요.

## License

Apache License 2.0. 자세한 내용은 [LICENSE](./LICENSE)를 참고하세요.
