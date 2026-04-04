import pytest

from src.core.priority_engine import PriorityEngine, PriorityEvaluation


@pytest.mark.parametrize(
    ("evaluation", "expected_score", "expected_label", "expected_percentual"),
    [
        (PriorityEvaluation(0, 0, 0, 0, 0), 0.0, "baixa", 0.0),
        (PriorityEvaluation(2, 2, 2, 2, 2), 10.0, "media", 0.4),
        (PriorityEvaluation(5, 4, 5, 3, 4), 21.0, "alta", 0.84),
    ],
)
def test_priority_engine_scores_and_classifies(
    evaluation: PriorityEvaluation,
    expected_score: float,
    expected_label: str,
    expected_percentual: float,
) -> None:
    result = PriorityEngine().evaluate(evaluation)

    assert result.score_total == expected_score
    assert result.score_maximo == 25.0
    assert result.percentual == expected_percentual
    assert result.classificacao == expected_label


def test_priority_engine_rejects_scores_outside_range() -> None:
    evaluation = PriorityEvaluation(6, 0, 0, 0, 0)

    with pytest.raises(ValueError):
        PriorityEngine().evaluate(evaluation)