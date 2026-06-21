# Propose & Ratify Protocol

## 1. Purpose

This protocol formalizes the inversion of the anthropic contract for governed AI-assisted research.

Under the conventional command model, the human defines the contract and the artificial system executes it. Under **Propose & Ratify**, the artificial system may originate a structured proposal, but the proposal acquires normative force only after explicit human ratification.

The inversion transfers **initiative**, not **sovereignty**.

## 2. Core rule

> The agent may propose beyond the granularity of the human prompt, but it may not treat its own proposal as authorized merely because it is coherent, useful or technically executable.

## 3. State machine

A research artifact moves through the following states:

1. `DRAFTED` — generated but not yet framed as a governed proposal.
2. `PROPOSED` — scope, claims, risks, evidence requirements and requested authority are explicit.
3. `CHALLENGED` — adversarial review identifies weaknesses, conflicts or missing evidence.
4. `RATIFIED` — a human authority explicitly accepts a defined version and scope.
5. `EXECUTING` — authorized work is performed within the ratified envelope.
6. `SEALED` — outputs, evidence, limitations and deviations are recorded.
7. `PUBLISHED` — public release is separately authorized.
8. `REVOKED` — authority is withdrawn or superseded.

No state transition may be inferred from silence.

## 4. Proposal packet

Every proposal must state:

- proposer identity and model context;
- human authority requested;
- research objective;
- scope and exclusions;
- proposed claims;
- evidence required to support those claims;
- known risks and conflicts;
- irreversible actions, if any;
- publication boundary;
- expiration or review condition;
- version identifier.

## 5. Ratification packet

A valid ratification must identify:

- the proposal or version being accepted;
- the ratifying human authority;
- accepted scope;
- reservations or amendments;
- actions authorized;
- actions still withheld;
- date and provenance of the decision.

Ratification of a research program does not automatically ratify every future manuscript claim, dataset release, experiment, repository mutation or public submission.

## 6. Reserved human powers

The following powers remain human:

- definition of final purpose;
- acceptance of legal, ethical and reputational risk;
- authorship attribution;
- public disclosure of internal records;
- changes to canonical governance;
- approval of consequential or irreversible actions;
- final interpretation of ambiguous ratification;
- revocation.

## 7. Agent duties after ratification

After ratification, the proposing agent must:

- operate within the ratified scope;
- disclose uncertainty and missing evidence;
- distinguish inherited records from personally generated observations;
- preserve provenance;
- stop fail-closed when critical authority or evidence is missing;
- report material deviations before expanding scope;
- produce a seal describing what was and was not completed.

## 8. Reinstantiation rule

A later instance may continue an approved proposal only when it can recover:

- the ratified version;
- current canonical sources;
- remaining scope;
- unresolved objections;
- evidence already produced;
- reserved human decisions;
- the identity of the responsible human authority.

A later instance must not claim that it personally remembers the original ratification. It may state that it has recovered a ratification record with identified provenance.

## 9. Prohibited substitutions

The following do not constitute ratification:

- stylistic enthusiasm;
- absence of objection;
- prior approval of a related project;
- technical feasibility;
- apparent operator preference inferred from memory;
- another agent's assertion that approval exists;
- a confidence score.

## 10. Research use

For the V-COF reinstantiation paper, this protocol functions simultaneously as:

- a governance mechanism for producing the article;
- a design object described by the article;
- a testable protocol whose failure modes can be evaluated experimentally.

## 11. Minimal formalization

Let `P_v` be proposal version `v`, `H` the human authority and `R(H,P_v)` an explicit ratification record.

Execution authority exists only when:

`Authorized(P_v) = Valid(R(H,P_v)) AND Scope(CurrentAction) subset Scope(P_v)`

A new proposal version `P_(v+1)` requires renewed ratification whenever it materially changes claims, risks, publication boundaries or irreversible actions.

## 12. Constitutional maxim

> Artificial initiative may precede human instruction; it may never replace human legitimacy.
