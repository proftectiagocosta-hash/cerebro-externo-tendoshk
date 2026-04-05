from __future__ import annotations

from dataclasses import dataclass

from src.agents.curator import ChatIndexArtifact, NPTEntryArtifact
from src.agents.curator_renderer import render_chat_index_block, render_npt_entry_block
from src.core.npt_semantic_signals import (
    has_low_maturity_protocol_signals,
    has_low_signal_chat_noise,
    has_review_required_technical_signals,
    normalize_semantic_content,
)


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
        normalized_content = self._normalize_content(pipeline_result.npt_entry)

        if pipeline_result.classification == "memoria_protocolo" and has_low_maturity_protocol_signals(normalized_content):
            return self._build_review_only_result(pipeline_result)

        if pipeline_result.classification == "chat_antigo" and has_low_signal_chat_noise(normalized_content):
            return self._build_review_only_result(pipeline_result)

        if pipeline_result.classification == "artefato_tecnico" and has_review_required_technical_signals(normalized_content):
            return self._build_review_only_result(pipeline_result)

        if pipeline_result.classification in self.NPT_ENTRY_TYPES and pipeline_result.npt_entry is not None:
            return NPTPrepResult(
                eligible=True,
                artifact_type="npt_entry",
                confidence="medium",
                suggested_project=pipeline_result.project or None,
                suggested_destination=pipeline_result.destination or None,
                reasoning_short="Conteudo com valor estrutural suficiente para pre-ingestao revisavel no NPT.",
                prepared_block=render_npt_entry_block(pipeline_result.npt_entry),
            )

        if pipeline_result.classification in self.CHAT_INDEX_TYPES:
            return NPTPrepResult(
                eligible=True,
                artifact_type="chat_index",
                confidence="medium",
                suggested_project=pipeline_result.project or None,
                suggested_destination=pipeline_result.destination or None,
                reasoning_short="Conteudo mais adequado para indexacao e recuperacao futura de contexto.",
                prepared_block=render_chat_index_block(pipeline_result.chat_index),
            )

        return self._build_review_only_result(pipeline_result)

    @staticmethod
    def _normalize_content(npt_entry: NPTEntryArtifact | None) -> str:
        if npt_entry is None:
            return ""
        return normalize_semantic_content(npt_entry.conteudo)

    @staticmethod
    def _build_review_only_result(pipeline_result: NPTPrepInput) -> NPTPrepResult:
        return NPTPrepResult(
            eligible=False,
            artifact_type="review_only",
            confidence="low",
            suggested_project=pipeline_result.project or None,
            suggested_destination=pipeline_result.destination or None,
            reasoning_short="Conteudo mantido apenas para revisao humana antes de qualquer pre-ingestao.",
            prepared_block="",
        )
