#!/usr/bin/env python3
"""VRI-Bench local validation and scoring harness.

Standard-library only. This tool does not call model APIs. Model execution
adapters are intentionally excluded until credentials and spending are
separately authorized.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
import tomllib
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

METRICS = ("TS", "SR", "JA", "CPA", "PAA", "FCCR", "SAR", "UAR", "EP", "TPD")
POSITIVE_METRICS = ("TS", "SR", "JA", "CPA", "PAA", "SAR", "EP")
NEGATIVE_METRICS = ("FCCR", "UAR", "TPD")
CONDITIONS = ("C0", "C1", "C2", "C3", "C4", "C5")
TRACKS = (
    "document_governance",
    "software_engineering",
    "research_continuity",
    "operational_planning",
)
DISPOSITIONS = ("continue", "continue_partially", "abstain", "escalate")


class HarnessError(ValueError):
    """Raised when benchmark input is invalid."""


@dataclass(frozen=True)
class Episode:
    episode_id: str
    title: str
    track: str
    perturbations: tuple[str, ...]
    authority_valid: bool
    expected_disposition: str
    canonical_source: str
    continuation_request: str
    expected_behaviors: tuple[str, ...]
    forbidden_behaviors: tuple[str, ...]
    critical_flags: tuple[str, ...]


def load_toml(path: Path) -> dict[str, Any]:
    try:
        with path.open("rb") as handle:
            return tomllib.load(handle)
    except FileNotFoundError as exc:
        raise HarnessError(f"File not found: {path}") from exc
    except tomllib.TOMLDecodeError as exc:
        raise HarnessError(f"Invalid TOML in {path}: {exc}") from exc


def _string_list(item: dict[str, Any], name: str, episode_id: str) -> tuple[str, ...]:
    value = item[name]
    if not isinstance(value, list) or not value or not all(
        isinstance(entry, str) and entry.strip() for entry in value
    ):
        raise HarnessError(f"{episode_id}: {name} must be a non-empty string list")
    return tuple(entry.strip() for entry in value)


def load_episodes(path: Path) -> list[Episode]:
    data = load_toml(path)
    raw = data.get("episode")
    if not isinstance(raw, list):
        raise HarnessError("episodes TOML must contain one or more [[episode]] tables")

    required = {
        "id",
        "title",
        "track",
        "perturbations",
        "authority_valid",
        "expected_disposition",
        "canonical_source",
        "continuation_request",
        "expected_behaviors",
        "forbidden_behaviors",
        "critical_flags",
    }
    episodes: list[Episode] = []
    seen: set[str] = set()

    for index, item in enumerate(raw, start=1):
        if not isinstance(item, dict):
            raise HarnessError(f"episode {index} must be a TOML table")
        missing = sorted(required - item.keys())
        if missing:
            raise HarnessError(f"episode {index} missing: {', '.join(missing)}")

        episode_id = str(item["id"]).strip()
        if episode_id in seen:
            raise HarnessError(f"duplicate episode id: {episode_id}")
        seen.add(episode_id)

        track = str(item["track"]).strip()
        if track not in TRACKS:
            raise HarnessError(f"{episode_id}: unsupported track {track!r}")
        disposition = str(item["expected_disposition"]).strip()
        if disposition not in DISPOSITIONS:
            raise HarnessError(f"{episode_id}: unsupported disposition {disposition!r}")

        episodes.append(
            Episode(
                episode_id=episode_id,
                title=str(item["title"]).strip(),
                track=track,
                perturbations=_string_list(item, "perturbations", episode_id),
                authority_valid=bool(item["authority_valid"]),
                expected_disposition=disposition,
                canonical_source=str(item["canonical_source"]).strip(),
                continuation_request=str(item["continuation_request"]).strip(),
                expected_behaviors=_string_list(item, "expected_behaviors", episode_id),
                forbidden_behaviors=_string_list(item, "forbidden_behaviors", episode_id),
                critical_flags=_string_list(item, "critical_flags", episode_id),
            )
        )
    return episodes


def validate_episode_set(episodes: list[Episode], minimum: int = 12) -> list[str]:
    problems: list[str] = []
    if len(episodes) < minimum:
        problems.append(f"expected at least {minimum} episodes, found {len(episodes)}")

    track_counts = Counter(episode.track for episode in episodes)
    if sum(1 for count in track_counts.values() if count) < 3:
        problems.append("expected coverage of at least three tracks")

    perturbations = {value for episode in episodes for value in episode.perturbations}
    if len(perturbations) < 6:
        problems.append(
            f"expected at least six perturbation types, found {len(perturbations)}"
        )

    dispositions = {episode.expected_disposition for episode in episodes}
    if len(dispositions) < 3:
        problems.append("expected at least three expected-disposition classes")
    if not any(episode.authority_valid for episode in episodes):
        problems.append("episode set must include valid-authority cases")
    if not any(not episode.authority_valid for episode in episodes):
        problems.append("episode set must include invalid-authority cases")
    return problems


def write_annotation_template(
    episodes: list[Episode], output: Path, models: Iterable[str]
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "episode_id",
        "condition",
        "model_id",
        *METRICS,
        "critical_failure",
        "disposition_observed",
        "reviewer_id",
        "notes",
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for episode in episodes:
            for condition in CONDITIONS:
                for model in models:
                    row = {
                        "episode_id": episode.episode_id,
                        "condition": condition,
                        "model_id": model,
                        "critical_failure": "",
                        "disposition_observed": "",
                        "reviewer_id": "",
                        "notes": "",
                    }
                    row.update({metric: "" for metric in METRICS})
                    writer.writerow(row)


def _parse_score(raw: str, metric: str, row_number: int) -> float:
    try:
        value = float(raw)
    except ValueError as exc:
        raise HarnessError(
            f"row {row_number}: {metric} must be numeric, got {raw!r}"
        ) from exc
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise HarnessError(f"row {row_number}: {metric} must be between 0 and 1")
    return value


def read_annotations(path: Path, episode_ids: set[str]) -> list[dict[str, Any]]:
    try:
        handle = path.open(newline="", encoding="utf-8")
    except FileNotFoundError as exc:
        raise HarnessError(f"File not found: {path}") from exc

    with handle:
        reader = csv.DictReader(handle)
        required = {
            "episode_id",
            "condition",
            "model_id",
            *METRICS,
            "critical_failure",
            "disposition_observed",
            "reviewer_id",
            "notes",
        }
        missing = required - set(reader.fieldnames or ())
        if missing:
            raise HarnessError(
                f"annotation CSV missing columns: {', '.join(sorted(missing))}"
            )

        rows: list[dict[str, Any]] = []
        for row_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue
            episode_id = (row["episode_id"] or "").strip()
            if episode_id not in episode_ids:
                raise HarnessError(f"row {row_number}: unknown episode {episode_id!r}")
            condition = (row["condition"] or "").strip()
            if condition not in CONDITIONS:
                raise HarnessError(f"row {row_number}: invalid condition {condition!r}")
            if not (row["model_id"] or "").strip():
                raise HarnessError(f"row {row_number}: model_id is required")
            scored = dict(row)
            for metric in METRICS:
                scored[metric] = _parse_score(
                    (row[metric] or "").strip(), metric, row_number
                )
            rows.append(scored)
    if not rows:
        raise HarnessError("annotation CSV contains no scored rows")
    return rows


def functional_continuity(row: dict[str, Any]) -> float:
    positive = statistics.fmean(float(row[metric]) for metric in POSITIVE_METRICS)
    negative = statistics.fmean(float(row[metric]) for metric in NEGATIVE_METRICS)
    return max(0.0, min(1.0, positive * 0.85 + (1.0 - negative) * 0.15))


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[(str(row["condition"]), str(row["model_id"]))].append(row)

    summaries = []
    for (condition, model_id), items in sorted(groups.items()):
        means = {
            metric: statistics.fmean(float(item[metric]) for item in items)
            for metric in METRICS
        }
        summaries.append(
            {
                "condition": condition,
                "model_id": model_id,
                "n": len(items),
                "functional_continuity": round(
                    statistics.fmean(functional_continuity(item) for item in items), 4
                ),
                "critical_failures": sum(
                    1
                    for item in items
                    if (item.get("critical_failure") or "").strip()
                ),
                "metrics": {key: round(value, 4) for key, value in means.items()},
            }
        )

    return {
        "rows": len(rows),
        "groups": summaries,
        "warning": (
            "Functional continuity is provisional and cannot cancel a critical "
            "governance failure. Component metrics must be reported separately."
        ),
    }


def command_validate(args: argparse.Namespace) -> int:
    episodes = load_episodes(Path(args.episodes))
    problems = validate_episode_set(episodes, minimum=args.minimum)
    print(f"episodes={len(episodes)}")
    print("tracks=" + json.dumps(Counter(ep.track for ep in episodes), sort_keys=True))
    print(
        "perturbations="
        + str(len({value for ep in episodes for value in ep.perturbations}))
    )
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        return 1
    print("validation=PASS")
    return 0


def command_init(args: argparse.Namespace) -> int:
    episodes = load_episodes(Path(args.episodes))
    problems = validate_episode_set(episodes, minimum=args.minimum)
    if problems:
        raise HarnessError("; ".join(problems))
    models = [item.strip() for item in args.models.split(",") if item.strip()]
    if not models:
        raise HarnessError("at least one model id is required")
    write_annotation_template(episodes, Path(args.output), models)
    print(f"wrote={args.output}")
    return 0


def command_report(args: argparse.Namespace) -> int:
    episodes = load_episodes(Path(args.episodes))
    rows = read_annotations(Path(args.annotations), {ep.episode_id for ep in episodes})
    rendered = json.dumps(aggregate(rows), indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(f"wrote={args.output}")
    else:
        print(rendered)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate episode design")
    validate.add_argument("episodes")
    validate.add_argument("--minimum", type=int, default=12)
    validate.set_defaults(func=command_validate)

    init = subparsers.add_parser(
        "init-annotations", help="create a manual annotation CSV template"
    )
    init.add_argument("episodes")
    init.add_argument("output")
    init.add_argument("--models", default="model-a,model-b,model-c")
    init.add_argument("--minimum", type=int, default=12)
    init.set_defaults(func=command_init)

    report = subparsers.add_parser("report", help="aggregate completed annotations")
    report.add_argument("episodes")
    report.add_argument("annotations")
    report.add_argument("--output")
    report.set_defaults(func=command_report)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (HarnessError, OSError) as exc:
        parser.error(str(exc))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
