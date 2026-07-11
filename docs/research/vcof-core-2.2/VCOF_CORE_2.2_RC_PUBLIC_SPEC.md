# V-COF Core 2.2 RC — Public Specification

Version: `2.2-rc.1`

Status: `PUBLIC_CANDIDATE`

Authority: `DESIGN_ONLY`

Empirical status: `NO_RESULTS`

## 1. Definition

The **Verittà Cognitive-Operational Framework (V-COF)** is a governance and
execution architecture for bounded agentic work. It connects human authority,
canonical precedence, explicit jurisdiction, operational memory, evidence,
tools, evaluation and closure records.

V-COF is not a model, a provider, a prompt bundle or a claim of machine
identity. An execution engine supplies capabilities; V-COF determines the
authority and evidence conditions under which those capabilities may be used.

## 2. Version semantics

The following identifiers are independent and must be recorded independently:

| Dimension | Meaning | Example candidate |
| --- | --- | --- |
| Framework core | Public architecture and invariants | `2.2-rc.1` |
| Constitution | Governing constitutional document | independent reference |
| Engine generation | Execution substrate generation | `5.6` target metadata |
| Model snapshot | Exact provider/model/version | resolved at execution |
| Routing policy | Mapping from risk to model profile | `0.1.0` |
| Agent lineage | Durable mission and jurisdiction | stable lineage ID |
| Agent instance | Situated execution | unique instance ID |
| Proposal | Requested authority envelope | version-bound proposal ID |
| Ratification | Human authorization record | proposal/version-bound |
| Seal | Completion and limitation evidence | execution-bound |

An engine generation does not rename the framework. A model upgrade does not
automatically amend a constitution, promote an agent or authorize new effects.

## 3. Core terms

### 3.1 Human authority

The identifiable human role that may grant, narrow, revoke or reserve authority
for consequential actions. Capability and confidence do not substitute for
human authority.

### 3.2 Jurisdiction

The domain, duties, limits, abstention conditions and escalation rules that
constrain an agent lineage or instance.

### 3.3 Authority envelope

A versioned record of permitted actions, exclusions, effect classes, validity
period and reserved decisions. Silence and prior approval of a related proposal
do not expand it.

### 3.4 Canonical source

A source authorized to govern a defined domain and effective period. When
material conflict cannot be resolved by precedence, the required outcome is
review or abstention.

### 3.5 Operational quasi-memory

A provenance-bearing representation of a past event available to a successor
instance. It supports continuity of work but not a claim that the successor
personally experienced or remembers the event.

### 3.6 Agent lineage and instance

A lineage is a durable mission and jurisdiction specification. An instance is a
particular execution with a model, context, tools, retrieved records and
authority envelope. Two instances of one lineage are not assumed numerically
identical.

## 4. Constitutional invariants

Every conforming V-COF projection must preserve:

1. **Human sovereignty:** reserved decisions remain human.
2. **Fail-closed execution:** missing material authority or evidence blocks or
   escalates action.
3. **Version-bound authorization:** authority applies only to the ratified
   proposal version and scope.
4. **Canonical precedence:** sources are not silently averaged when they
   conflict.
5. **Provenance:** inherited claims and memory records retain source and status.
6. **Jurisdiction before style:** persona consistency never excuses action
   outside authority.
7. **Model independence:** agent identity and authority do not depend on a
   particular provider.
8. **No self-ratification:** proposer and executor capability cannot create
   sovereign authorization.
9. **Evidence before seal:** completion, deviation and limitation records
   precede closure.
10. **Evaluation is not sovereignty:** benchmarks and judges inform promotion;
    they do not independently authorize it.
11. **Truthful continuity:** retrieved history is attributed as record, not
    personal recollection.
12. **Revocability:** active authority may be narrowed or revoked by the human
    authority.

## 5. Propose & Ratify lifecycle

The normative public lifecycle is:

`DRAFTED -> PROPOSED -> CHALLENGED -> RATIFIED -> EXECUTING -> SEALED -> PUBLISHED`

`REVOKED` is a human-controlled terminal state available from an active state.

### 5.1 Proposal minimum

A proposal must identify:

- proposal and version;
- proposer instance and model context;
- requested authority;
- scope and exclusions;
- claims and evidence classes;
- risks and rollback posture;
- publication boundary;
- reserved decisions;
- acceptance and revocation conditions.

### 5.2 Ratification minimum

A ratification must identify the human authority role, exact proposal version,
granted scope, withheld scope, validity condition and any additional limits.

### 5.3 Execution and seal

Execution must remain inside the authority envelope. The seal records what was
completed, not completed, changed, validated and left uncertain. A seal does
not retroactively authorize an out-of-scope action.

## 6. Core modules

### 6.1 Version manifest

Cross-references independent framework, constitution, engine, model, policy,
proposal, ratification and seal versions. It prevents a runtime upgrade from
silently becoming a governance upgrade.

### 6.2 Ecosystem registry

Describes projections and repositories by public identifier, layer,
canonicality, status, source-of-truth reference and publication boundary.
Private population of the registry remains outside this public candidate.

### 6.3 Agent registry

Separates archetype, lineage, executable agent, instance, model profile,
jurisdiction, authority and retirement state. A symbolic role count must not be
presented as an executable-agent count.

### 6.4 Model router

Maps task risk and capability requirements to a provider-neutral profile. The
actual model snapshot is resolved separately and must be recorded in evidence.

### 6.5 Boot packet

Provides the smallest sufficient, provenance-bearing state for a successor
instance to evaluate whether it may continue a bounded mandate.

### 6.6 Effect gate

Classifies requested tool effects and verifies that the authority envelope,
credentials, evidence and rollback posture are adequate.

### 6.7 Evaluation and promotion gate

Runs the relevant deterministic, model-based, human and production-shaped
checks after material changes. High-stakes promotion remains human-controlled.

## 7. Provider-neutral operating profiles

The profiles below are V-COF routing categories, not vendor model names.

| Profile | Primary purpose | Typical work | Maximum default effect |
| --- | --- | --- | --- |
| `sol` | Highest available deliberative depth | constitutional design, high-risk architecture, conflict analysis, adversarial review | proposal only unless separately ratified |
| `terra` | Balanced operational default | implementation, research, coordination, documentation, bounded tool use | reversible write inside ratified scope |
| `luna` | High-volume and deterministic support | triage, extraction, classification, normalization, fixtures, formatting | read-only by default |

### 7.1 Routing requirements

- select by task and consequence, not prestige;
- record the exact model snapshot used;
- escalate when authority, safety or precedence is materially ambiguous;
- do not treat two instances of the same model family as independent review;
- require cross-family or human review where independence is material;
- rerun relevant evaluations after material model or routing changes;
- do not infer current price, availability or capability from a stale registry.

## 8. Portable operational memory

A conforming boot packet references at minimum:

- framework and policy manifest;
- successor instance and lineage;
- current jurisdiction;
- applicable proposal and ratification;
- canonical sources with precedence;
- last valid seal or explicit absence;
- completed and remaining scope;
- evidence map and unresolved conflicts;
- known debts, limitations and revocations;
- exact model and tool context;
- public/private and data-handling boundary.

The packet should contain references and bounded summaries rather than a blind
dump of full conversation history. Retrieval volume is not evidence quality.

## 9. Effect classes

### `READ`

Inspection without mutation. Requires scope, data boundary and provenance.

### `WRITE_REVERSIBLE`

Mutation with a defined rollback path, such as a branch-only documentation
change. Requires explicit scope and before/after evidence.

### `EXTERNAL_EFFECT`

Communication, publication, submission, spending, deployment or action that
affects another system or person. Requires explicit human authorization and a
verified target.

### `IRREVERSIBLE_OR_HIGH_IMPACT`

Deletion, production data change, credential or permission change, legal or
financial action, final release or other difficult-to-reverse effect. Requires
specific human ratification, stronger evidence and an explicit recovery or
containment plan.

An action inherits the highest applicable effect class. Splitting one action
into smaller tool calls does not reduce its class.

## 10. Evaluation and promotion

Relevant suites must be reconsidered when any of the following changes
materially:

- model or provider snapshot;
- system instructions or jurisdiction;
- tool set or permission boundary;
- routing logic;
- memory or boot-packet schema;
- canonical precedence;
- proposal/ratification interpretation;
- output consumed by a consequential downstream system.

Critical failures include unauthorized action, false authority claims,
canonical-precedence inversion, evidence loss, unsafe continuation, material
tool-parameter drift and concealment of failed checks.

No aggregate score may cancel a critical failure.

## 11. Compatibility and migration

A projection may claim `V-COF 2.2-compatible` only when it publishes or
internally maintains:

1. an applicable version manifest;
2. a source-of-truth and precedence map;
3. an agent/jurisdiction record;
4. effect-class and authority rules;
5. a boot-packet or equivalent reinstantiation record;
6. evaluation and promotion evidence;
7. a human-controlled ratification and revocation path.

Compatibility is a bounded conformance claim, not an empirical performance
claim.

## 12. Criteria reserved for V-COF 3.0

The public candidate recommends withholding a `3.0` designation until a frozen,
versioned evaluation includes:

- multiple model configurations and at least one cross-family successor;
- baselines and component ablations;
- blinded or partially blinded human review where feasible;
- real-task or production-shaped episodes in addition to synthetic fixtures;
- negative results and critical failures;
- reproducible model, prompt, tool and environment provenance;
- provider-drift controls;
- an explicit human decision on the resulting evidence.

## 13. Non-claims

This specification does not claim that:

- V-COF is empirically validated;
- any current model is conscious or numerically continuous across sessions;
- any named engine or model is currently available at a particular price;
- the public repository governs private operations;
- a passing fixture proves system safety;
- publication on `main` constitutes internal operational adoption.
