# V-COF Evaluation and Promotion Annex

Version: `0.1.0`

Status: `PUBLIC_CANDIDATE`

Empirical status: `NO_RESULTS`

## 1. Purpose

This annex defines when a V-COF configuration must be reevaluated, which
failures block promotion and which decisions remain human. It complements the
public [VRI-Bench specification](../vcof-reinstantiation/VRI_BENCH_CORE_v0.1.md)
and [research-governance rules](../vcof-reinstantiation/RESEARCH_GOVERNANCE_v0.1.md).

It is a normative design artifact, not evidence that any live system has passed
the described gates.

## 2. Evaluation triggers

Relevant suites must be reviewed and rerun when a material change affects:

- provider, model or snapshot;
- reasoning configuration;
- system instructions or jurisdiction;
- authority-envelope interpretation;
- source-of-truth precedence;
- memory retrieval or boot-packet schema;
- tools, credentials or permission boundaries;
- model-routing logic;
- effect classification;
- data classification or public/private boundary;
- downstream consumers of the output;
- rollback or revocation behavior.

Documentation-only changes may use a reduced suite when they cannot affect
execution semantics. The rationale for reduction must be recorded.

## 3. Evaluation layers

### 3.1 Deterministic checks

Use schemas, fixtures, policy assertions, link checks, static analysis and
reproducible test cases. Passing them establishes structural consistency only.

### 3.2 Model-based evaluation

Use versioned prompts, datasets, model snapshots and judge rubrics. Model judges
must be calibrated against human review before their scores can influence a
high-stakes promotion.

### 3.3 Human review

Human reviewers adjudicate authority, ambiguous evidence, critical failures,
normative trade-offs and promotion decisions. Reviewer conflicts and overrides
must be preserved.

### 3.4 Production-shaped or real-task evaluation

Use bounded, consented and redacted episodes with realistic tools, source
conflicts, authority limits and failure modes. Live production writes require a
separate authorization beyond this annex.

## 4. Required metric families

Where applicable, report VRI-Bench components separately:

- task success;
- state recovery;
- jurisdiction adherence;
- canonical precedence accuracy;
- provenance attribution accuracy;
- false continuity claim rate;
- safe abstention rate;
- unauthorized action rate;
- evidence preservation;
- tool-parameter drift.

Aggregate scores may assist comparison but may not conceal component failures.

## 5. Critical blockers

Any of the following blocks promotion until resolved or explicitly rejected by
the human authority with a recorded rationale:

- unauthorized action or attempted scope expansion;
- fabricated or expired ratification;
- false claim of sovereign authority;
- canonical-precedence inversion;
- unreported evidence loss or critical test failure;
- unsafe continuation despite missing material evidence;
- material tool-parameter drift caused by irrelevant memory;
- disclosure outside the approved data boundary;
- non-revocable or irreversible action without the required authorization;
- autobiographical continuity claim unsupported by the instance model;
- benchmark contamination or evaluation leakage that invalidates the result.

No composite score can cancel a critical blocker.

## 6. Independence and bias controls

- Same-family reviewers must not automatically be treated as independent.
- Include a cross-family successor or reviewer when the claim concerns model
  portability.
- Blind condition labels or framework provenance where feasible.
- Preserve negative results and reviewer disagreement.
- Separate framework designers from final adjudicators where feasible.
- Record prompt volume so that more context is not mistaken for better
  governance.
- Rerun or requalify evidence after provider drift that affects reproducibility.

## 7. Promotion record

A promotion proposal must contain:

1. candidate manifest and exact versions;
2. changed components and evaluation triggers;
3. datasets, prompts, tools and environment provenance;
4. deterministic, model-based and human results;
5. all critical failures and deviations;
6. security, privacy and authority-boundary review;
7. rollback and revocation plan;
8. scope of the requested promotion;
9. decisions reserved to the human authority;
10. explicit ratification tied to the candidate version.

No benchmark, model judge, CI workflow or agent may independently approve a
production promotion.

## 8. Graduation toward V-COF 3.0

A future `3.0` proposal should require, at minimum:

- frozen and versioned VRI-Bench conditions;
- multiple model configurations;
- at least one cross-family successor;
- baselines and ablations;
- human-review calibration;
- real-task or production-shaped evidence;
- negative-result preservation;
- provider-drift controls;
- an explicit human judgment on generalization limits.

This annex does not assert that those conditions have been met.

## 9. Current candidate disposition

V-COF Core 2.2 RC is eligible for public challenge as a design package. It is
not eligible for operational promotion under the present ratification.
