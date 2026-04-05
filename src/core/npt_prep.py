from dataclasses import dataclass
from typing import Optional


@dataclass
class NPTPrepResult:
    eligible: bool
    artifact_type: str
    confidence: str
    suggested_project: Optional[str]
    suggested_destination: Optional[str]
    reasoning_short: str
    prepared_block: str


class NPTPrep:
    def prepare(self, pipeline_result: dict) -> NPTPrepResult:
        classification = pipeline_result.get("classification", "")
        priority = pipeline_result.get("priority", "")
        route = pipeline_result.get("route", "")
        curated_text = pipeline_result.get("curated_text", "")

        artifact_type = "review_only"
        confidence = "low"
        suggested_project = None
        suggested_destination = None
        reasoning_short = "Conteúdo ainda não atende critério suficiente para bloco preparatório do NPT."
        prepared_block = ""

        if classification in {"strategic", "protocol", "memory", "project"}:
            artifact_type = "npt_entry"
            confidence = "medium"
            suggested_project = self._map_project(route, classification)
            suggested_destination = self._map_destination(suggested_project)
            reasoning_short = "Conteúdo com indícios de valor estrutural e possível utilidade persistente."
            prepared_block = self._build_npt_entry(
                suggested_project=suggested_project,
                suggested_destination=suggested_destination,
                priority=priority,
                content=curated_text,
            )

        elif classification in {"reference", "archive", "historical"}:
            artifact_type = "chat_index"
            confidence = "medium"
            suggested_project = self._map_project(route, classification)
            suggested_destination = self._map_destination(suggested_project)
            reasoning_short = "Conteúdo parece mais adequado para indexação e referência futura."
            prepared_block = self._build_chat_index(
                suggested_project=suggested_project,
                suggested_destination=suggested_destination,
                content=curated_text,
            )

        eligible = artifact_type in {"npt_entry", "chat_index"}

        return NPTPrepResult(
            eligible=eligible,
            artifact_type=artifact_type,
            confidence=confidence,
            suggested_project=suggested_project,
            suggested_destination=suggested_destination,
            reasoning_short=reasoning_short,
            prepared_block=prepared_block,
        )

    def _map_project(self, route: str, classification: str) -> str:
        if "ambiente" in route.lower():
            return "AMBIENTES_RETOMADA"
        if "memoria" in route.lower() or classification in {"memory", "protocol"}:
            return "NPT_NUCLEO_PERSISTENTE_TENDOSHK"
        return "TENDOSHK_CENTRAL"

    def _map_destination(self, project: Optional[str]) -> Optional[str]:
        mapping = {
            "AMBIENTES_RETOMADA": "ambientes_retomada.md",
            "NPT_NUCLEO_PERSISTENTE_TENDOSHK": "npt_nucleo_persistente_tendoshk.md",
            "TENDOSHK_CENTRAL": "tendoshk_central.md",
        }
        return mapping.get(project)

    def _build_npt_entry(
        self,
        suggested_project: Optional[str],
        suggested_destination: Optional[str],
        priority: str,
        content: str,
    ) -> str:
        return f"""[NPT_ENTRY]
tipo=registro_curado
projeto={suggested_project or ""}
subtipo=pre_ingestao_cerebro_externo
prioridade={priority or "media"}
destino={suggested_destination or ""}
modo=consolidar
origem=cerebro_externo_tendoshk
conteudo={content.strip()}
[/NPT_ENTRY]"""

    def _build_chat_index(
        self,
        suggested_project: Optional[str],
        suggested_destination: Optional[str],
        content: str,
    ) -> str:
        resumo = content.strip().replace("\n", " ")
        resumo = resumo[:220]

        return f"""[CHAT_INDEX]
nome_sugerido=Registro preparado pelo cerebro externo
tipo_indexacao=INDEXAR COMO REFERÊNCIA FRACA
projeto_principal={suggested_project or ""}
arquivo_drive={suggested_destination or ""}
descricao_curta={resumo}
potencial_reutilizacao=Consulta futura e recuperação de contexto relevante
[/CHAT_INDEX]"""