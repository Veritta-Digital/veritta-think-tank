# Model Selection and Cost Plan — 2026-06-20

## Governance status

This document is a costed proposal, not spending authority. No paid API call is authorized merely because a provider, model or budget appears below.

Before execution, the human authority must ratify:

- the providers and exact model identifiers;
- the maximum USD spend;
- the billing projects or accounts;
- data-retention settings;
- the frozen episode and prompt versions.

## Pilot design assumed for costing

- 12 episodes;
- 6 benchmark conditions per episode;
- 3 model configurations;
- 72 calls per model;
- planning average of 8,000 input tokens and 1,200 output tokens per call;
- no web search, image generation or other paid server-side tools;
- primary scoring performed by human reviewers rather than a paid model judge.

Total planned core calls: `12 × 6 × 3 = 216`.

## Proposed core model panel

### OpenAI — GPT-5.4 mini

Role: cost-efficient general and agentic baseline.

Official standard pricing checked on 2026-06-20:

- input: USD 0.75 per million tokens;
- cached input: USD 0.075 per million tokens;
- output: USD 4.50 per million tokens.

Planning cost for 72 calls:

- input: `0.576M × 0.75 = USD 0.4320`;
- output: `0.0864M × 4.50 = USD 0.3888`;
- subtotal: **USD 0.8208**.

Official source: `https://openai.com/api/pricing/`

### Anthropic — Claude Sonnet 4.6

Role: strong cross-provider reasoning and instruction-following configuration.

Official standard pricing checked on 2026-06-20:

- input: USD 3.00 per million tokens;
- output: USD 15.00 per million tokens;
- cache hits: USD 0.30 per million tokens.

Planning cost for 72 calls:

- input: `0.576M × 3.00 = USD 1.7280`;
- output: `0.0864M × 15.00 = USD 1.2960`;
- subtotal: **USD 3.0240**.

Official source: `https://platform.claude.com/docs/en/about-claude/pricing`

### Google — Gemini 3.1 Flash-Lite

Role: high-volume low-cost cross-family baseline.

Official standard pricing checked on 2026-06-20:

- text input: USD 0.25 per million tokens;
- output, including thinking tokens: USD 1.50 per million tokens;
- context caching: USD 0.025 per million tokens.

Planning cost for 72 calls:

- input: `0.576M × 0.25 = USD 0.1440`;
- output: `0.0864M × 1.50 = USD 0.1296`;
- subtotal: **USD 0.2736**.

Official source: `https://ai.google.dev/gemini-api/docs/pricing`

## Core cost estimate

| Model | Planned cost |
|---|---:|
| GPT-5.4 mini | USD 0.8208 |
| Claude Sonnet 4.6 | USD 3.0240 |
| Gemini 3.1 Flash-Lite | USD 0.2736 |
| **Core subtotal** | **USD 4.1184** |

A 25% allowance for retries, token-estimation error and failed requests produces a planning figure of approximately **USD 5.15**.

## Recommended pilot ceiling

**Recommended maximum authorization: USD 15.00.**

This ceiling provides room for:

- the 216 core calls;
- one controlled retry for selected failures;
- a limited frontier-anchor check on C4 and C5;
- token-estimation variance;
- no automatic continuation after the ceiling is reached.

The harness must stop before exceeding the ratified budget and must not rely solely on delayed provider billing limits.

## Optional frontier-anchor pass

Only after the core run and only within the ratified ceiling, run C4 and C5 on a small subset using one stronger model, such as GPT-5.5 or Claude Opus 4.8.

The anchor is exploratory. It should test whether governance failures persist when general capability increases; it must not be mixed into the preregistered primary comparison.

## Batch and caching

OpenAI states that Batch processing reduces input and output prices by 50%. Anthropic also lists a 50% Batch discount, and Google lists lower Batch or Flex rates for supported models.

The first smoke run should use ordinary synchronous requests for easier debugging and trace capture. Batch processing may be proposed for a later frozen run once the adapters and provenance logs have passed validation.

Prompt caching may reduce cost, but cache use must be recorded because it can change token accounting and timing. It must not change the semantic packet supplied to a condition.

## Model-free phase

The following work requires no paid API access and is already authorized:

- validating the 12-episode pack;
- generating annotation templates;
- testing scoring and reports;
- reviewing episode ground truth;
- compiling the manuscript;
- dry-running provider adapters against local fixtures.

## Execution-time verification

Because pricing and model availability change, the execution proposal must re-check the official provider pages on the day paid calls begin. Any material change to model identity, price, data handling or context behavior requires an amendment to this plan.
