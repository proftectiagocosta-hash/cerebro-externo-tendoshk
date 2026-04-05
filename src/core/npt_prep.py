from __future__ import annotations

from dataclasses import dataclass

from src.agents.curator import ChatIndexArtifact, NPTEntryArtifact


@dataclass(frozen=True)
class NPTPrepInput:
    classification: str
    project: str
    destination: str
    chat_index: ChatIndexArtifact
    npt_entry: NPTEntryArtifact | None


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

    def prepare(self, pipeline_result: NPTPrepInput) -> NPTPrepResult:
        if pipeline_result.classification in self.NPT_ENTRY_TYPES and pipeline_result.npt_entry is not None:
            return NPTPrepResult(
                eligible=True,
                artifact_type="npt_entry",
                confidence="medium",
                suggested_project=pipeline_result.project or None,
                suggested_destination=pipeline_result.destination or None,
                reasoning_short="Conteudo com valor estrutural suficiente para pre-ingestao revisavel no NPT.",
                prepared_block=pipeline_result.npt_entry.render_block(),
            )

        if pipeline_result.classification in self.CHAT_INDEX_TYPES:
            return NPTPrepResult(
                eligible=True,
                artifact_type="chat_index",
                confidence="medium",
                suggested_project=pipeline_result.project or None,
                suggested_destination=pipeline_result.destination or None,
                reasoning_short="Conteudo mais adequado para indexacao e recuperacao futura de contexto.",
                prepared_block=pipeline_result.chat_index.render_block(),
            )

        return NPTPrepResult(
            eligible=False,
            artifact_type="review_only",
            confidence="low",
            suggested_project=pipeline_result.project or None,
            suggested_destination=pipeline_result.destination or None,
            reasoning_short="Conteudo mantido apenas para revisao humana antes de qualquer pre-ingestao.",
            prepared_block="",
        )
