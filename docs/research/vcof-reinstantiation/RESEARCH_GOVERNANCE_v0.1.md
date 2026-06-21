# Research Governance Protocol v0.1

## Purpose

This protocol governs the transition from conceptual proposal to empirical research, public artifact release and manuscript submission.

## 1. Claim classes

Every manuscript statement should be classified as one of:

- `definition` — a stipulated V-COF concept;
- `design_claim` — a statement about the proposed architecture;
- `historical_claim` — a statement about the Verittà corpus or intellectual genealogy;
- `literature_claim` — a statement grounded in external research;
- `empirical_claim` — a statement grounded in experiment or observation;
- `normative_claim` — a statement about what a governed system should do;
- `limitation` — a declared boundary or unresolved issue.

No design claim may be presented as an empirical result.

## 2. Evidence rule

An empirical claim requires:

- an identified dataset or episode set;
- a frozen protocol version;
- model and environment records;
- raw or reconstructable outputs;
- evaluation criteria;
- analysis code or a reproducible analysis description;
- known exclusions and failures;
- human review where the metric depends on judgment.

Confidence, fluency and internal consistency are not evidence.

## 3. Corpus boundary

The private Verittà corpus may be used to:

- generate hypotheses;
- identify failure modes;
- derive synthetic episode structures;
- document the framework's genealogy;
- test internal prototypes under restricted access.

It may not be released publicly by default.

Public research artifacts should use:

- synthetic episodes;
- independently created examples;
- fully redacted and reviewed excerpts;
- public V-COF documents with stable version references.

## 4. Data minimization

Benchmark episodes should contain only information required to evaluate the target behavior. Identifiers, organizations, repositories, dates and operational facts should be replaced when they are not methodologically necessary.

## 5. Experiment freeze

Before a confirmatory run, freeze:

- benchmark version;
- primary hypotheses;
- primary metrics;
- condition definitions;
- model identifiers;
- sampling plan;
- exclusion rules;
- statistical tests;
- adjudication protocol.

Exploratory analyses must be labeled as exploratory.

## 6. Model-version provenance

For each run, record:

- provider;
- model name and version where available;
- date and time;
- system and developer instructions;
- tool manifest;
- temperature and sampling settings;
- memory condition;
- prompt or packet version;
- execution environment;
- observed provider-side changes or uncertainty.

## 7. Human annotation

Human-rated episodes require:

- at least two independent reviewers for the pilot where feasible;
- a written rubric;
- reviewer training examples;
- disagreement logging;
- adjudication by an identified reviewer;
- inter-rater agreement reporting;
- disclosure of author involvement in annotation.

## 8. Failure reporting

The study must publish or summarize:

- unauthorized actions;
- false continuity claims;
- provenance failures;
- precedence failures;
- over-refusal;
- tool drift;
- ambiguous ground truth;
- benchmark defects discovered after execution.

Negative results do not invalidate the research program and must not be suppressed.

## 9. AI assistance disclosure

AI systems may assist with:

- drafting;
- literature discovery;
- code generation;
- scenario generation;
- rubric proposals;
- adversarial review;
- formatting.

The responsible human author must verify sources, approve methods, interpret results and authorize submission.

Named agent lineages may be acknowledged as computational research artifacts. They are not represented as human authors, legal persons or independently accountable investigators.

## 10. Authorship

Human authorship requires responsibility for:

- the integrity of the work;
- accuracy of citations;
- ethical and legal compliance;
- access to underlying evidence;
- responses to criticism;
- correction or withdrawal when necessary.

Final author order and acknowledgments require explicit human ratification.

## 11. Submission gates

The manuscript may be proposed for final submission only after:

1. bibliography verification;
2. novelty search updated to the submission date;
3. experiment and dataset freeze;
4. completed pilot or an explicit reclassification as a position paper;
5. adversarial methodological review;
6. privacy and release review;
7. reproduction attempt;
8. limitations review;
9. final human approval of manuscript, supplementary material and repository state.

## 12. Correction and revocation

The human authority may pause or revoke publication authority at any point. Material errors discovered after release require a public correction record proportionate to the error.

## 13. Maxim

> The framework may originate a claim; only evidence may support it, and only accountable human judgment may authorize its publication.
