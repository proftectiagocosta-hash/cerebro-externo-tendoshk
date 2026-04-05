from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.agents.curator import ChatIndexArtifact, NPTEntryArtifact


def render_chat_index_block(artifact: ChatIndexArtifact) -> str:
    return "\n".join(
        [
            "[CHAT_INDEX]",
            f"nome_sugerido={artifact.nome_sugerido}",
            f"tipo_indexacao={artifact.tipo_indexacao}",
            f"projeto_principal={artifact.projeto_principal}",
            f"arquivo_drive={artifact.arquivo_drive}",
            f"descricao_curta={artifact.descricao_curta}",
            f"potencial_reutilizacao={artifact.potencial_reutilizacao}",
            "[/CHAT_INDEX]",
        ]
    )


def render_npt_entry_block(artifact: NPTEntryArtifact) -> str:
    return "\n".join(
        [
            "[NPT_ENTRY]",
            f"tipo={artifact.tipo}",
            f"projeto={artifact.projeto}",
            f"subtipo={artifact.subtipo}",
            f"prioridade={artifact.prioridade}",
            f"destino={artifact.destino}",
            f"modo={artifact.modo}",
            f"origem={artifact.origem}",
            f"conteudo={artifact.conteudo}",
            "[/NPT_ENTRY]",
        ]
    )
