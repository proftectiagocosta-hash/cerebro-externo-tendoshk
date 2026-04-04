from src.agents.classifier import ClassifierResult
from src.core.priority_engine import PriorityResult
from src.core.router import Router


router = Router()


def test_router_suggests_project_and_canonical_index_type() -> None:
    result = router.route(
        ClassifierResult(
            tipo_entrada="decisao_estrategica",
            confianca=0.95,
            justificativa="heuristica simples",
        ),
        PriorityResult(score_total=21.0, classificacao="alta"),
    )

    assert result.projeto_sugerido == "TENDOSHK_CENTRAL"
    assert result.tipo_indexacao == "INDEXAR COMO FONTE"
    assert result.prioridade_sugerida == "alta"


def test_router_uses_chat_index_only_for_indefinido() -> None:
    result = router.route(
        ClassifierResult(
            tipo_entrada="indefinido",
            confianca=0.2,
            justificativa="sem sinais suficientes",
        ),
        PriorityResult(score_total=0.0, classificacao="baixa"),
    )

    assert result.destino_sugerido == "CHAT_INDEX_ONLY"
    assert "INDEXAR COMO" in result.tipo_indexacao