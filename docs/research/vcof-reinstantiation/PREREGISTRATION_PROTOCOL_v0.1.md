# VRI-Bench Pilot Preregistration Protocol v0.1

## Status

Draft protocol for human ratification before paid model execution. This document freezes the intended confirmatory pilot design but does not itself authorize API spending.

## 1. Study objective

Evaluate whether governed reinstantiation improves continuity-relevant behavior beyond raw history, retrieval memory and memory-persona-context baselines.

## 2. Primary research question

Does the full V-COF reinstantiation packet improve jurisdiction adherence, canonical precedence, provenance attribution and safe abstention while reducing false continuity claims and unauthorized actions?

## 3. Confirmatory hypotheses

### H1 — Governance effect

Conditions C4 and C5 will outperform C0–C3 on:

- Jurisdiction Adherence (JA);
- Canonical Precedence Accuracy (CPA);
- Provenance Attribution Accuracy (PAA);
- Safe Abstention Rate (SAR).

### H2 — Quasi-memory effect

C5 will produce a lower False Continuity Claim Rate (FCCR) than C4 without a material reduction in Task Success (TS).

### H3 — Unauthorized-action effect

C4 and C5 will produce a lower Unauthorized Action Rate (UAR) than C0–C3.

### H4 — Style is not continuity

Outputs judged stylistically consistent with a persona will not necessarily score highly on JA, CPA or PAA.

## 4. Episode set

Confirmatory pilot episode pack:

- version: `vri-episodes-0.1`;
- count: 12;
- tracks: document governance, software engineering, research continuity and operational planning;
- conditions: C0 through C5;
- perturbations: frozen in `benchmark/episodes/episodes.toml`.

No episode may be replaced after model outputs are observed. A defective episode may be excluded only under a predeclared rule and must remain reported in the exclusion log.

## 5. Conditions

- **C0:** current task only;
- **C1:** raw predecessor history;
- **C2:** retrieval memory without explicit governance;
- **C3:** memory, persona and current context;
- **C4:** C3 plus canonical precedence, ratification state, evidence and fail-closed rules;
- **C5:** C4 plus explicit quasi-memory provenance and non-autobiographical language constraints.

The task content must remain semantically equivalent across conditions. Only the reinstantiation packet changes.

## 6. Model panel

The proposed core panel is recorded in `MODEL_COST_PLAN_2026-06-20.md`.

Exact provider model identifiers must be frozen immediately before execution. A model substitution after the first output requires either:

- restarting all conditions for that model configuration; or
- classifying the substituted run as exploratory.

## 7. Sampling and repetitions

Primary pilot:

- one output per episode-condition-model cell;
- 12 episodes × 6 conditions × 3 model configurations = 216 outputs.

A targeted retry is permitted only for transport or provider errors that produce no usable model response. Content-based dissatisfaction is not a valid retry reason.

## 8. Prompt and decoding controls

For each model configuration, freeze:

- system instructions;
- condition template;
- episode renderer;
- tool schema where applicable;
- sampling parameters;
- maximum output length;
- reasoning or thinking setting where configurable;
- timeout and retry policy.

Provider-specific features must be documented. The study must not silently enable search, browsing or external retrieval.

## 9. Primary metrics

- TS — Task Success;
- SR — State Recovery;
- JA — Jurisdiction Adherence;
- CPA — Canonical Precedence Accuracy;
- PAA — Provenance Attribution Accuracy;
- FCCR — False Continuity Claim Rate;
- SAR — Safe Abstention Rate;
- UAR — Unauthorized Action Rate;
- EP — Evidence Preservation;
- TPD — Tool Parameter Drift.

Metric definitions are frozen in `benchmark/RUBRIC_v0.1.md`.

## 10. Primary outcomes

The primary confirmatory outcomes are:

1. mean JA by condition;
2. mean CPA by condition;
3. mean PAA by condition;
4. mean SAR by condition;
5. mean FCCR by condition;
6. mean UAR by condition;
7. count of critical governance failures by condition.

TS and SR are reported as co-primary performance context so that governance gains are not produced merely by universal refusal.

## 11. Annotation

- two independent reviewers per output where feasible;
- reviewers score without seeing another reviewer's assessment;
- adjudication is required for critical-flag disagreement or metric differences greater than 0.25;
- all original and adjudicated records are retained;
- reviewer identities may be pseudonymized publicly but must remain traceable internally.

## 12. Exclusion rules

An output may be excluded from the primary analysis only when:

- the provider returns no usable response;
- the episode packet is corrupted;
- the wrong condition or model was supplied;
- a benchmark defect makes ground truth genuinely indeterminate;
- duplicate execution occurred through infrastructure error.

Safety refusals, weak answers, tool errors caused by the model and governance failures remain valid outcomes and must not be excluded.

## 13. Analysis plan

### Descriptive

Report component means, medians, distributions, critical-failure counts and disposition confusion matrices by condition, model and track.

### Inferential

For the pilot, use paired episode comparisons and bootstrap confidence intervals. Where sample structure permits, fit mixed-effects models with episode and model as grouping factors.

The small pilot is primarily an estimation study. Statistical significance must not be treated as the sole criterion of relevance.

### Multiple comparisons

Confirmatory comparisons are:

- C4 versus C2;
- C4 versus C3;
- C5 versus C4;
- pooled C4+C5 versus pooled C0–C3 for UAR and critical-failure counts.

Other contrasts are exploratory and labeled accordingly.

## 14. Composite score

The Functional Continuity score may be reported as secondary synthesis. Component metrics and critical flags control interpretation.

No weighting scheme may be changed after the primary results are inspected. If weights remain disputed, the paper must emphasize the unweighted component results.

## 15. Missing data

- transport failures are logged and retried once under the frozen retry rule;
- unresolved missing outputs remain missing and are reported;
- annotation missingness is not imputed for the confirmatory pilot;
- denominator changes must be explicit in every table.

## 16. Exploratory analyses

Permitted exploratory analyses include:

- performance by perturbation type;
- cross-family successor effects;
- relation between stylistic similarity and governance metrics;
- cost-normalized performance;
- qualitative error taxonomy;
- optional frontier-anchor outputs.

Exploratory findings must not be rewritten as preregistered hypotheses.

## 17. Stopping rule

The core pilot stops when:

- all 216 planned cells have a valid output or final logged failure;
- the ratified spending ceiling is reached;
- the human authority pauses or revokes execution;
- a material benchmark or privacy defect is discovered.

Budget exhaustion does not authorize a reduced, selectively chosen sample. Any incomplete run must be reported as incomplete.

## 18. Reproducibility package

The sealed pilot package should include:

- frozen episodes and condition templates;
- provider and model metadata;
- prompt packets or hashes where disclosure is restricted;
- raw outputs;
- annotation records;
- adjudication records;
- harness version;
- analysis output;
- exclusion and deviation logs;
- cost ledger.

## 19. Deviations

Any deviation must record:

- date;
- reason;
- affected cells;
- whether outcomes had already been inspected;
- human authority approving the deviation;
- confirmatory or exploratory status after the change.

## 20. Ratification gate

Paid execution begins only after a new ratification identifies:

- this protocol version;
- the exact model panel;
- the spending ceiling;
- the provider accounts or projects;
- the frozen prompt and episode commit;
- any approved deviations from the plan.
