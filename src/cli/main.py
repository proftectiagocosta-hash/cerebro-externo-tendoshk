from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.agents.classifier import TextClassifier
from src.agents.curator import Curator, CuratorInput
from src.core.memory_loader import MemoryLoader
from src.core.priority_engine import PriorityEngine, PriorityEvaluation
from src.core.router import Router


def build_priority_evaluation(tipo_entrada: str) -> PriorityEvaluation:
    if tipo_entrada == "decisao_estrategica":
        return PriorityEvaluation(
            valor_estrategico=5,
            reaproveitamento=4,
            alinhamento_tendoshk=5,
            urgencia=3,
            potencial_monetizacao=4,
        )

    return PriorityEvaluation(
        valor_estrategico=3,
        reaproveitamento=3,
        alinhamento_tendoshk=3,
        urgencia=2,
        potencial_monetizacao=2,
    )


def map_reuse_label(classificacao: str) -> str:
    mapping = {
        "alta": "alto",
        "media": "medio",
        "baixa": "baixo",
    }
    return mapping.get(classificacao, "medio")


def find_project_file(projects_catalog: dict, project_name: str) -> str:
    for project in projects_catalog.get("projetos_canonicos", []):
        if project.get("nome") == project_name:
            return project.get("arquivo_drive", "")
    return ""


if __name__ == "__main__":
    example_text = (
        "Precisamos definir a prioridade e a direcao do roadmap do projeto piloto "
        "TENDOSHK_CENTRAL para consolidar componentes reutilizaveis."
    )

    memory_loader = MemoryLoader()
    classifier = TextClassifier()
    priority_engine = PriorityEngine()
    router = Router()
    curator = Curator()

    memory_bundle = memory_loader.load()
    classification = classifier.classify(example_text)
    priority_evaluation = build_priority_evaluation(classification.tipo_entrada)
    priority_result = priority_engine.evaluate(priority_evaluation)
    routing_result = router.route(classification, priority_result)

    curator_input = CuratorInput(
        titulo_sugerido="Simulacao integrada inicial do piloto",
        tipo_entrada=classification.tipo_entrada,
        tipo_indexacao=routing_result.tipo_indexacao,
        projeto_principal=routing_result.projeto_sugerido,
        descricao_curta="Resultado inicial da simulacao integrada do Cerebro Externo Tendoshk.",
        potencial_reutilizacao=map_reuse_label(priority_result.classificacao),
        conteudo=example_text,
        arquivo_drive=find_project_file(memory_bundle.projects_catalog, routing_result.projeto_sugerido),
        subtipo="simulacao_integrada",
        prioridade=routing_result.prioridade_sugerida,
        destino=routing_result.destino_sugerido,
    )
    curated = curator.curate(curator_input)

    print("Simulacao integrada do Cerebro Externo Tendoshk")
    print(
        f"Memoria carregada: nome={memory_bundle.identity.get('nome')} | "
        f"projetos={len(memory_bundle.projects_catalog.get('projetos_canonicos', []))}"
    )
    print("Classificacao")
    print(f"tipo_entrada={classification.tipo_entrada}")
    print(f"confianca={classification.confianca:.2f}")
    print(f"justificativa={classification.justificativa}")
    print("Prioridade")
    print(f"score_total={priority_result.score_total:.2f}")
    print(f"classificacao={priority_result.classificacao}")
    print("Roteamento")
    print(f"projeto_sugerido={routing_result.projeto_sugerido}")
    print(f"tipo_indexacao={routing_result.tipo_indexacao}")
    print(f"prioridade_sugerida={routing_result.prioridade_sugerida}")
    print(f"destino_sugerido={routing_result.destino_sugerido}")
    print(f"justificativa={routing_result.justificativa}")
    print("CHAT_INDEX")
    print(curated.chat_index_block)

    if curated.npt_entry_block:
        print("NPT_ENTRY")
        print(curated.npt_entry_block)