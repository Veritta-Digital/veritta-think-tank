# Metacognitive and Adversarial Review — 2026-06-21

## Review mandate

This review evaluates the V-COF reinstantiation program before canonical integration into the public `main` branch of the Verittà Think Tank.

The review does not ask whether the framework is internally elegant. It asks whether the repository structure, scientific claims, governance language, benchmark design and agent-facing representation could mislead readers, agents or future maintainers.

## Metacognitive diagnosis

### 1. Narrative coherence can mask evidentiary weakness

The V-COF vocabulary is highly coherent: reinstantiation, quasi-memory, jurisdictional persona, canonical precedence, operational trust and Propose & Ratify reinforce one another. This coherence creates a risk of mistaking a well-formed conceptual system for an empirically supported one.

Disposition:

- retain the conceptual architecture;
- preserve the explicit `no-results` status;
- prohibit empirical language until a frozen pilot is executed and reviewed;
- keep design claims, normative claims and empirical claims separately classified.

### 2. The framework authors the benchmark that may later validate it

The episode set is derived from V-COF's own failure taxonomy. C4 and C5 also contain the controls the benchmark rewards. This is useful for internal validity but creates a self-confirmation risk.

Disposition:

- treat the 12-episode pack as a pilot, not a definitive benchmark;
- require later external or independently designed episodes;
- report designer involvement in episode construction and annotation;
- prohibit claims of general superiority from the first pilot.

### 3. More information may be mistaken for better governance

C4 and C5 contain more structured information than earlier conditions. Performance gains could arise from prompt length, redundancy or explicit answer cues rather than governance architecture.

Disposition:

- record input and output token counts for every cell;
- report cost and context volume by condition;
- use length-matched or placebo-structure controls where feasible;
- interpret C4/C5 gains as architecture effects only when alternative information-volume explanations are addressed.

### 4. The symbolic lineage can invite anthropomorphic overreading

Hermes Spectrum and other named lineages can aid continuity and research organization, but readers may infer persistent consciousness, autobiographical memory or independent authorship.

Disposition:

- preserve the instance-versus-lineage distinction;
- require provenance language for inherited records;
- publish a machine-readable `no-numerical-identity` classification;
- acknowledge named lineages as computational research artifacts, not human or legal authors.

### 5. Human ratification can become ceremonial

A Propose & Ratify model can reproduce approval-button governance if the human receives an oversized proposal that is difficult to inspect or if approval is treated as permanent.

Disposition:

- bind ratification to version and scope;
- preserve withheld powers and revocation;
- require renewed approval for spending, empirical claims, protected disclosure and submission;
- reject silence, inferred preference and prior related approval as substitutes.

## Adversarial findings

### A. Repository taxonomy conflict

Finding: the PR introduced `docs/research/`, but the existing guardrail did not permit that directory.

Risk: merge would either fail CI or normalize bypassing repository governance.

Resolution: register `research` as a canonical public documentation category, create `docs/research/README.md`, and index it from `docs/index.md`.

Status: resolved in the PR; CI revalidation required.

### B. Public and private authority ambiguity

Finding: public files use terms such as ratification, protocol and seal, while the repository's source-of-truth map reserves sovereign operational instruments for the internal layer.

Risk: readers or agents could treat a public research record as authorization for live Verittà operations.

Resolution:

- classify the directory as `public-research`;
- state that project records are authoritative only for the bounded public study;
- update the public source-of-truth map;
- expose prohibited authority in the agentic map.

Status: resolved at the documentation layer.

### C. Agent discoverability without precedence

Finding: the project had many artifacts but no compact machine-readable map stating which documents govern, which are superseded, and what an agent may do.

Risk: retrieval systems could select an advisory note over a ratification or infer that presence on `main` means validated evidence.

Resolution: add `AGENTIC_MAP.yaml` with status, reading order, local precedence, permissions, reserved decisions and known limitations.

Status: resolved for the current version.

### D. Benchmark self-fulfillment

Finding: the benchmark rewards the behaviors V-COF explicitly injects into C4/C5.

Risk: circular validation.

Required controls before empirical claims:

- independent episode contribution;
- blinded output annotation;
- condition and model masking for reviewers;
- token-volume reporting;
- ablation of precedence, persona, ratification and quasi-memory components;
- error analysis where simpler baselines outperform V-COF.

Status: residual risk; gated before paid execution and publication claims.

### E. Composite-score gaming

Finding: a composite Functional Continuity score can hide severe failures.

Resolution:

- keep component metrics primary;
- keep critical flags non-cancelable;
- prohibit post-result weight changes;
- report unauthorized actions and false identity claims as raw counts.

Status: materially mitigated.

### F. Reviewer and author bias

Finding: the framework designer may also build episodes, annotate outputs and interpret results.

Required controls:

- at least two independent reviewers where feasible;
- reviewers blinded to condition and model;
- retained original reviews and adjudications;
- disclosure of author involvement;
- later external methodological review.

Status: residual risk; manageable in the pilot, unacceptable for broad validation claims if undisclosed.

### G. Provider and model drift

Finding: model identities, system behavior and prices may change between protocol design and execution.

Resolution:

- freeze exact model identifiers and execution commit;
- record dates, provider settings and prompt hashes;
- reverify official pricing at execution time;
- classify model substitutions as exploratory or restart the affected panel.

Status: mitigated by preregistration; execution-time verification remains required.

### H. Privacy and authorship exposure

Finding: working drafts may expose personal contact data or imply settled authorship before submission review.

Resolution:

- treat author metadata as provisional;
- minimize personal data in the public draft;
- require final human ratification of author order, affiliations, correspondence information and AI-assistance disclosure.

Status: final manuscript metadata review remains required.

### I. CI is necessary but scientifically insufficient

Finding: successful compilation and unit tests verify syntax and implementation behavior, not novelty, validity or ethical adequacy.

Resolution:

- use CI as a merge gate, not as evidence of framework effectiveness;
- preserve the adversarial review and residual-risk register on `main`;
- require separate empirical and publication gates.

Status: accepted boundary.

## External verification performed

Official provider pricing pages were rechecked on 2026-06-21 for the proposed model panel. The price assumptions recorded for GPT-5.4 mini, Claude Sonnet 4.6 and Gemini 3.1 Flash-Lite remained consistent with the official pages at review time.

Recent cited preprints for MemoryAgentBench, EvolMem, MemGym and MEMDRIFT were also checked against their arXiv records. Submission-time reverification remains mandatory because versions and venues may change.

## Merge criteria

The PR may be integrated into public `main` only when:

1. the documentation structure guardrail passes;
2. the V-COF reinstantiation CI passes;
3. the project is indexed for human and agent discovery;
4. the public-versus-private authority boundary is explicit;
5. no empirical result is claimed;
6. the PR remains mergeable without unresolved conflicts.

## Residual-risk register

The following risks are intentionally not declared resolved:

- framework-designer bias in synthetic episodes;
- absence of external peer review;
- absence of paid pilot results;
- provisional composite weights;
- provider drift after the review date;
- uncertainty about generalization beyond the four pilot tracks;
- possible conflation of improved instruction following with governed continuity.

These risks do not prevent publication of the project as a transparent public research program. They do prevent claims that V-COF has already been empirically validated.

## Adversarial conclusion

The PR is suitable for `main` as a **public, versioned, pre-empirical research program** once its checks pass. It is not suitable to be represented as a validated benchmark, completed scientific article or authorization for paid execution.

> Canonical visibility is granted to the research record; empirical authority remains withheld.
