from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.agents.classifier import ClassifierResult, TextClassifier
from src.agents.curator import Curator, CuratorInput, CuratorOutput
from src.core.memory_loader import MemoryBundle, MemoryLoader
from src.core.npt_prep import NPTPrep, NPTPrepResult
from src.core.priority_engine import PriorityEngine, PriorityEvaluation, PriorityResult
from src.core.router import Router, RouterResult


@dataclass(frozen=True)
class PipelineResult:
    memory_bundle: MemoryBundle
    classification: ClassifierResult
    priority_result: PriorityResult
    routing_result: RouterResult
    curated_output: CuratorOutput
    npt_prep: NPTPrepResult


class TendoshkPipeline:
    def __init__(self) -> None:
        self.memory_loader = MemoryLoader()
        self.classifier = TextClassifier()
        self.priority_engine = PriorityEngine()
        self.router = Router()
        self.curator = Curator()
        self.npt_prep = NPTPrep()

    def run(self, text: str) -> PipelineResult:
        memory_bundle = self.memory_loader.load()
        classification = self.classifier.classify(text)
        priority_evaluation = self._build_priority_evaluation(classification.tipo_entrada)
        priority_result = self.priority_engine.evaluate(priority_evaluation)
        routing_result = self.router.route(classification, priority_result)
        arquivo_drive = self._find_project_file(
            memory_bundle.projects_catalog,
            routing_result.projeto_sugerido,
        )
        curator_input = CuratorInput(
            titulo_sugerido="Simulacao integrada inicial do piloto",
            tipo_entrada=classification.tipo_entrada,
            tipo_indexacao=routing_result.tipo_indexacao,
            projeto_principal=routing_result.projeto_sugerido,
            descricao_curta="Resultado inicial da simulacao integrada do Cerebro Externo Tendoshk.",
            potencial_reutilizacao=self._map_reuse_label(priority_result.classificacao),
            conteudo=text,
            arquivo_drive=arquivo_drive,
            subtipo="simulacao_integrada",
            prioridade=routing_result.prioridade_sugerida,
            destino=routing_result.destino_sugerido,
        )
        curated_output = self.curator.curate(curator_input)
        npt_prep = self.npt_prep.prepare(
            {
                "classification": classification.tipo_entrada,
                "priority": priority_result.classificacao,
                "project": routing_result.projeto_sugerido,
                "destination": routing_result.destino_sugerido,
                "chat_index": curated_output.chat_index,
                "npt_entry": curated_output.npt_entry,
                "chat_index_block": curated_output.chat_index_block,
                "npt_entry_block": curated_output.npt_entry_block,
            }
        )

        return PipelineResult(
            memory_bundle=memory_bundle,
            classification=classification,
            priority_result=priority_result,
            routing_result=routing_result,
            curated_output=curated_output,
            npt_prep=npt_prep,
        )

    @staticmethod
    def _build_priority_evaluation(tipo_entrada: str) -> PriorityEvaluation:
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

    @staticmethod
    def _map_reuse_label(classificacao: str) -> str:
        mapping = {
            "alta": "alto",
            "media": "medio",
            "baixa": "baixo",
        }
        return mapping.get(classificacao, "medio")

    @staticmethod
    def _find_project_file(projects_catalog: dict[str, Any], project_name: str) -> str:
        for project in projects_catalog.get("projetos_canonicos", []):
            if project.get("nome") == project_name:
                return project.get("arquivo_drive", "")
        return ""


if __name__ == "__main__":
    example_text = (
        "Precisamos definir a prioridade e a direcao do roadmap do projeto piloto "
        "TENDOSHK_CENTRAL para consolidar componentes reutilizaveis."
    )

    pipeline = TendoshkPipeline()
    result = pipeline.run(example_text)

    print("Pipeline test")
    print(
        f"Memoria carregada: nome={result.memory_bundle.identity.get('nome')} | "
        f"projetos={len(result.memory_bundle.projects_catalog.get('projetos_canonicos', []))}"
    )
    print(f"tipo_entrada={result.classification.tipo_entrada}")
    print(f"score_total={result.priority_result.score_total:.2f}")
    print(f"projeto_sugerido={result.routing_result.projeto_sugerido}")
    print(result.curated_output.chat_index_block)
    if result.curated_output.npt_entry_block:
        print(result.curated_output.npt_entry_block)
    print(f"npt_prep={result.npt_prep.artifact_type}")
