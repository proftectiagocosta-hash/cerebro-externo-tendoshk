from __future__ import annotations

from dataclasses import dataclass

from src.agents.classifier import ClassifierResult
from src.core.priority_engine import PriorityResult


@dataclass(frozen=True)
class RouterResult:
    tipo_entrada: str
    projeto_sugerido: str
    tipo_indexacao: str
    prioridade_sugerida: str
    destino_sugerido: str
    justificativa: str


class Router:
    PROJECT_BY_TYPE: dict[str, str] = {
        "decisao_estrategica": "TENDOSHK_CENTRAL",
        "artefato_tecnico": "NPT_NUCLEO_PERSISTENTE_TENDOSHK",
        "dev_log": "AMBIENTES_RETOMADA",
        "memoria_protocolo": "SISTEMA_MEMORIA_AUDITORIA",
        "chat_antigo": "NPT_NUCLEO_PERSISTENTE_TENDOSHK",
    }

    def route(
        self,
        classifier_result: ClassifierResult,
        priority_result: PriorityResult,
    ) -> RouterResult:
        tipo_entrada = classifier_result.tipo_entrada
        projeto_sugerido = self.PROJECT_BY_TYPE.get(tipo_entrada, "NPT_NUCLEO_PERSISTENTE_TENDOSHK")
        tipo_indexacao = self._suggest_index_type(tipo_entrada)
        prioridade_sugerida = priority_result.classificacao
        destino_sugerido = self._suggest_destination(tipo_entrada)
        justificativa = (
            f"Rota sugerida a partir do tipo '{tipo_entrada}' e da prioridade "
            f"'{priority_result.classificacao}'."
        )

        return RouterResult(
            tipo_entrada=tipo_entrada,
            projeto_sugerido=projeto_sugerido,
            tipo_indexacao=tipo_indexacao,
            prioridade_sugerida=prioridade_sugerida,
            destino_sugerido=destino_sugerido,
            justificativa=justificativa,
        )

    @staticmethod
    def _suggest_index_type(tipo_entrada: str) -> str:
        if tipo_entrada == "indefinido":
            return "INDEXAR COMO REFERÊNCIA FRACA"
        return "INDEXAR COMO FONTE"

    @staticmethod
    def _suggest_destination(tipo_entrada: str) -> str:
        if tipo_entrada == "indefinido":
            return "CHAT_INDEX_ONLY"
        return "NPT_NUCLEO_PERSISTENTE_TENDOSHK"


if __name__ == "__main__":
    router = Router()
    classifier_result = ClassifierResult(
        tipo_entrada="decisao_estrategica",
        confianca=0.95,
        justificativa="Categoria detectada por palavras-chave de prioridade e roadmap.",
    )
    priority_result = PriorityResult(
        score_total=21.0,
        score_maximo=25.0,
        percentual=0.84,
        classificacao="alta",
    )
    route = router.route(classifier_result, priority_result)

    print("Router test")
    print(f"tipo_entrada={route.tipo_entrada}")
    print(f"projeto_sugerido={route.projeto_sugerido}")
    print(f"tipo_indexacao={route.tipo_indexacao}")
    print(f"prioridade_sugerida={route.prioridade_sugerida}")
    print(f"destino_sugerido={route.destino_sugerido}")
    print(f"justificativa={route.justificativa}")