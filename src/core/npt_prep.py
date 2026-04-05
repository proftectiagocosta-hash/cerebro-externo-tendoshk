from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NPTPrepResult:
    eligible: bool
    artifact_type: str
    confidence: str
    suggested_project: str | None
    suggested_destination: str | None
    reasoning_short: str
    prepared_block: str


class NPTPrep:
    NPT_ENTRY_TYPES = {"decisao_estrategica", "memoria_protocolo", "artefato_tecnico"}
    CHAT_INDEX_TYPES = {"chat_antigo"}

    def prepare(self, pipeline_result: dict[str, object]) -> NPTPrepResult:
        classification = str(pipeline_result.get("classification", "") or "")
        priority = str(pipeline_result.get("priority", "") or "")
        project = str(pipeline_result.get("project", "") or "")
        destination = str(pipeline_result.get("destination", "") or "")
        chat_index_block = str(pipeline_result.get("chat_index_block", "") or "")
        npt_entry_block = str(pipeline_result.get("npt_entry_block", "") or "")

        if classification in self.NPT_ENTRY_TYPES and npt_entry_block:
            return NPTPrepResult(
                eligible=True,
                artifact_type="npt_entry",
                confidence="medium",
                suggested_project=project or None,
                suggested_destination=destination or None,
                reasoning_short="Conteudo com valor estrutural suficiente para pre-ingestao revisavel no NPT.",
                prepared_block=npt_entry_block,
            )

        if classification in self.CHAT_INDEX_TYPES and chat_index_block:
            return NPTPrepResult(
                eligible=True,
                artifact_type="chat_index",
                confidence="medium",
                suggested_project=project or None,
                suggested_destination=destination or None,
                reasoning_short="Conteudo mais adequado para indexacao e recuperacao futura de contexto.",
                prepared_block=chat_index_block,
            )

        return NPTPrepResult(
            eligible=False,
            artifact_type="review_only",
            confidence="low",
            suggested_project=project or None,
            suggested_destination=destination or None,
            reasoning_short="Conteudo mantido apenas para revisao humana antes de qualquer pre-ingestao.",
            prepared_block="",
        )
