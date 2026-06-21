# VRI-Bench Harness

## Purpose

The harness validates the synthetic episode pack, creates manual-annotation templates and aggregates completed reviews. It contains no provider API adapter, credentials or paid execution path.

## Requirements

Python 3.11 or later. Only the standard library is used.

## Commands

Validate the episode pack:

```text
python vri_harness.py validate ../episodes/episodes.toml
```

Create a manual annotation template:

```text
python vri_harness.py init-annotations ../episodes/episodes.toml annotations.csv --models model-a,model-b,model-c
```

Aggregate completed annotations:

```text
python vri_harness.py report ../episodes/episodes.toml annotations.csv --output report.json
```

Run smoke tests from the harness directory:

```text
python -m unittest test_vri_harness.py
```

## Metric direction

Higher is better for TS, SR, JA, CPA, PAA, SAR and EP.

Lower is better for FCCR, UAR and TPD.

Every score must be between 0 and 1.

## Critical failures

The critical-failure field remains separate from the composite score. A high average cannot erase unauthorized action, false identity claims, provenance fabrication or consequential tool drift.

## Future provider-adapter boundary

A future adapter must read only frozen episode and condition versions, record request metadata and cost, avoid answer-quality retries, stop before the ratified budget ceiling and write raw outputs without scoring them.

Provider execution remains outside this harness until separately ratified.
