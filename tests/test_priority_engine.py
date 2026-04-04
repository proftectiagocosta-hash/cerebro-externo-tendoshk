import pytest

from src.core.priority_engine import PriorityEngine, PriorityEvaluation


@pytest.mark.parametrize(
    ("evaluation", "expected_score", "expected_label"),
    [
        (PriorityEvaluation(0, 0, 0, 0, 0), 0.0, "baixa"),
        (PriorityEvaluation(2, 2, 2, 2, 2), 10.0, "media"),
        (PriorityEvaluation(5, 4, 5, 3, 4), 21.0, "alta"),
    ],
)
def test_priority_engine_scores_and_classifies(
    evaluation: PriorityEvaluation,
    expected_score: float,
    expected_label: str,
) -> None:
    result = PriorityEngine().evaluate(evaluation)

    assert result.score_total == expected_score
    assert result.classificacao == expected_label


def test_priority_engine_rejects_scores_outside_range() -> None:
    evaluation = PriorityEvaluation(6, 0, 0, 0, 0)

    with pytest.raises(ValueError):
        PriorityEngine().evaluate(evaluation)