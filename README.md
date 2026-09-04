# Workspace Ops

[한국어](./README.md) · [English](./README.en.md)

AI-assisted software development를 위한 **human-gated governance framework**입니다.

AI는 상당한 규모의 구현 작업을 수행할 수 있습니다. 하지만 그 실행 능력이 acceptance, promotion, deployment, scope expansion, 또는 인접 프로젝트의 ownership을 자동으로 부여하지는 않습니다.

핵심 원칙은 다음과 같습니다.

```text
execution ability != decision authority
```

Workspace Ops는 AI-assisted engineering을 **bounded execution, evidence, explicit state transitions, independent review, human-controlled authority**를 중심으로 구성하기 위한 opinionated reference governance model입니다.

## 무엇을 모델링하는가

Workspace Ops는 여섯 가지 primitive를 중심으로 합니다.

- **Authority** — 누가 결정할 수 있는가.
- **Scope** — executor가 무엇을 변경할 수 있는가.
- **State** — 작업이 실제로 어떤 상태에 도달했는가.
- **Evidence** — 해당 state claim을 무엇이 증명하는가.
- **Gate** — 다음 transition을 무엇이 승인하는가.
- **Boundary** — 어디에서 실행을 멈추고 escalate 또는 handoff해야 하는가.

이 구분은 다음과 같은 category error를 방지합니다.

```text
can implement != can accept
verified != accepted
review pass != promoted
promotion authorized != promoted
promoted != deployed
```

## Execution Modes

Public baseline은 다섯 가지 reusable execution mode를 정의합니다.

- `ANALYSIS_ONLY`
- `HUMAN_GATED`
- `NONSTOP_BOUNDED`
- `REVIEW_ONLY`
- `OPERATION_ONLY`

`NONSTOP_BOUNDED`는 **pre-authorized bounded continuation**을 의미합니다. unrestricted autonomous development를 의미하지 않습니다.

실행 범위는 유한해야 하며 다음 boundary는 계속 유효합니다.

- scope expansion
- ownership / authority boundary
- destructive operation
- evidence conflict
- architecture or human judgment requirement
- promotion / deployment authorization

## State와 Gate

일반적인 successful path는 다음과 같이 표현할 수 있습니다.

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

하지만 이것은 하나의 self-advancing state machine이 아닙니다.

각 transition은 서로 다른 authority와 gate에 의해 결정될 수 있습니다. Evidence는 transition을 뒷받침할 수 있지만, 그 자체로 authorization이 되지는 않습니다.

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

Reusable prompt에는 role과 behavior contract를 두고, 현재 SHA, branch, worktree, runtime target, current blocker 같은 값은 Execution Envelope 또는 live state에서 주입합니다.

## Multi-project / Multi-agent Boundary

다른 프로젝트나 track을 볼 수 있다는 사실은 mutation authority를 의미하지 않습니다.

```text
observe != own
consumer need != provider authority
dependency discovery != provider implementation authorization
```

Frontend, backend, infrastructure, security, review, operations 등 여러 agent가 병렬로 동작하더라도 각자의 execution boundary와 ownership boundary는 독립적으로 유지됩니다.

## Repository Guide

처음 읽는다면 다음 순서를 권장합니다.

- [Concepts](docs/CONCEPTS.md)
- [Quickstart](docs/QUICKSTART.md)
- [Authority Model](governance/AUTHORITY_MODEL.md)
- [State and Gates](governance/STATE_AND_GATES.md)
- [Execution Modes](governance/EXECUTION_MODES.md)
- [Human Review](governance/HUMAN_REVIEW.md)
- [Execution Envelope](governance/EXECUTION_ENVELOPE.md)
- [Boundaries and Stop Conditions](governance/BOUNDARIES_AND_STOP_CONDITIONS.md)
- [Prompt Governance](governance/PROMPT_GOVERNANCE.md)
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

현재 `toolkit/`은 provisional surface만 문서화합니다. CLI나 orchestration engine이 governance를 먼저 정의하게 하지 않습니다.

## Positioning

Workspace Ops는 AI-assisted SDLC governance를 위한 **one practical approach / reference governance model**입니다.

다음과 같이 주장하지 않습니다.

```text
industry standard
universal framework
fully autonomous development
```

실제 private AI-assisted development workflow에서 얻은 운영 경험을 일반화한 것이지만, 이 repository는 private workspace의 공개본이나 mirror가 아닙니다. 자세한 내용은 [Public Disclosure](docs/PUBLIC_DISCLOSURE.md)를 참고하세요.

## License

Apache License 2.0. 자세한 내용은 [LICENSE](./LICENSE)를 참고하세요.
