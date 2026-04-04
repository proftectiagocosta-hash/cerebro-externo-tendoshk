from __future__ import annotations

from dataclasses import dataclass, fields


@dataclass(frozen=True)
class PriorityWeights:
    valor_estrategico: float = 1.0
    reaproveitamento: float = 1.0
    alinhamento_tendoshk: float = 1.0
    urgencia: float = 1.0
    potencial_monetizacao: float = 1.0


@dataclass(frozen=True)
class PriorityEvaluation:
    valor_estrategico: float
    reaproveitamento: float
    alinhamento_tendoshk: float
    urgencia: float
    potencial_monetizacao: float


@dataclass(frozen=True)
class PriorityResult:
    score_total: float
    score_maximo: float
    percentual: float
    classificacao: str


class PriorityEngine:
    def __init__(self, weights: PriorityWeights | None = None) -> None:
        self.weights = weights or PriorityWeights()

    def evaluate(self, evaluation: PriorityEvaluation) -> PriorityResult:
        self._validate_scores(evaluation)

        score_total = (
            evaluation.valor_estrategico * self.weights.valor_estrategico
            + evaluation.reaproveitamento * self.weights.reaproveitamento
            + evaluation.alinhamento_tendoshk * self.weights.alinhamento_tendoshk
            + evaluation.urgencia * self.weights.urgencia
            + evaluation.potencial_monetizacao * self.weights.potencial_monetizacao
        )
        score_maximo = self._max_score()
        percentual = score_total / score_maximo if score_maximo else 0.0

        return PriorityResult(
            score_total=score_total,
            score_maximo=score_maximo,
            percentual=percentual,
            classificacao=self._classify(percentual),
        )

    @staticmethod
    def _validate_scores(evaluation: PriorityEvaluation) -> None:
        for field in fields(evaluation):
            value = getattr(evaluation, field.name)
            if not 0 <= value <= 5:
                raise ValueError(f"{field.name} must be between 0 and 5")

    def _max_score(self) -> float:
        return 5 * sum(getattr(self.weights, field.name) for field in fields(self.weights))

    @staticmethod
    def _classify(percentual: float) -> str:
        if percentual < 0.4:
            return "baixa"
        if percentual < 0.7:
            return "media"
        return "alta"


if __name__ == "__main__":
    engine = PriorityEngine()
    evaluation = PriorityEvaluation(
        valor_estrategico=5,
        reaproveitamento=4,
        alinhamento_tendoshk=5,
        urgencia=3,
        potencial_monetizacao=4,
    )
    result = engine.evaluate(evaluation)

    print("Priority engine test")
    print(f"Score total: {result.score_total:.2f}")
    print(f"Score maximo: {result.score_maximo:.2f}")
    print(f"Percentual: {result.percentual:.2f}")
    print(f"Classificacao: {result.classificacao}")