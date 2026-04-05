from __future__ import annotations

from pathlib import Path
from typing import Literal, NotRequired, TypedDict

import pytest
import yaml

from src.core.pipeline import TendoshkPipeline


class BehaviorCase(TypedDict):
    id: str
    title: str
    expected_classification: str
    expected_npt_prep: str
    calibration_status: Literal["stable", "suspect", "future_tuning_target"]
    rationale: str
    input_text: str
    notes: NotRequired[str]


FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "behavior_cases.yaml"


def load_behavior_cases() -> list[BehaviorCase]:
    payload = yaml.safe_load(FIXTURE_PATH.read_text(encoding="utf-8"))
    return payload["cases"]


@pytest.mark.parametrize("case", load_behavior_cases(), ids=lambda case: case["id"])
def test_pipeline_matches_expected_behavior_cases(case: BehaviorCase) -> None:
    result = TendoshkPipeline().run(case["input_text"])

    assert result.classification.tipo_entrada == case["expected_classification"], case["title"]
    assert result.npt_prep.artifact_type == case["expected_npt_prep"], case["rationale"]
