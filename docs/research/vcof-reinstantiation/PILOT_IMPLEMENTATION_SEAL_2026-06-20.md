# Pilot Implementation Seal — 2026-06-20

## Cycle

Second execution cycle of the V-COF Reinstantiation Research Program under Propose & Ratify.

## Ratified objective

Implement the proposed pre-experimental phase:

- local benchmark harness;
- initial synthetic episode pack;
- scoring and adjudication rubric;
- model-selection and cost plan;
- preregistration-style protocol;
- automated harness and manuscript validation.

## Completed artifacts

### Executable benchmark layer

- standard-library Python harness;
- episode-pack validation;
- annotation-template generation;
- metric aggregation and JSON reporting;
- separate visibility for critical governance failures;
- smoke-test suite.

### Pilot corpus

- 12 synthetic episodes;
- four tracks;
- valid- and invalid-authority cases;
- multiple expected dispositions;
- perturbations covering stale memory, missing ratification, precedence conflicts, false autobiographical invitations, tool drift, evidence gaps, scope expansion, revoked authority and adversarial inherited instructions.

### Evaluation layer

- component-level annotation rubric;
- positive and negative metric direction;
- critical failure flags;
- adjudication threshold;
- reporting requirements.

### Experiment governance

- preregistration protocol;
- confirmatory hypotheses and contrasts;
- retry and exclusion rules;
- stopping rules;
- deviation log requirements;
- model-version and prompt-freeze requirements.

### Resource plan

- three-provider core panel proposal;
- 216 planned core cells;
- token and cost assumptions;
- current official price references;
- recommended maximum pilot authorization of USD 15;
- explicit statement that the plan does not authorize spending.

### Automated validation

- GitHub Actions workflow for episode validation and smoke tests;
- LaTeX compilation job;
- PDF artifact upload on successful workflow completion.

## Scientific controls preserved

- no paid API calls were made;
- no provider credentials were requested or stored;
- no model output was generated or scored;
- no empirical claim was added to the manuscript;
- no raw private Forge record was released;
- no final submission or merge was performed.

## Validation state

The repository workflow has been created, but no workflow-run record was available through the connector at seal time. Therefore CI success is not claimed in this seal.

An independent local clone could not be performed in the execution environment because external hostname resolution was unavailable. The code and document checks must be treated as pending until the PR workflow reports them.

## Next ratification gate

Paid pilot execution requires a bounded ratification identifying:

1. the exact execution commit;
2. exact provider model identifiers;
3. a maximum USD spend;
4. billing projects or accounts;
5. frozen prompt and condition templates;
6. provider data-handling choices;
7. authorized execution operator;
8. stop conditions.

Until that ratification exists, the permitted next actions are limited to review, correction, dry-run validation and CI remediation.

## Seal statement

> The pilot now exists as an executable and governed design. It is ready to be tested by CI and reviewed for a future paid run; it is not yet an experiment and produces no evidence of framework effectiveness.
