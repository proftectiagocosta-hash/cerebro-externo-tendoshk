from src.agents.curator import ChatIndexArtifact, NPTEntryArtifact
from src.core.npt_prep import NPTPrep, NPTPrepInput


def test_npt_prep_generates_npt_entry_for_structural_content() -> None:
    result = NPTPrep().prepare(
        NPTPrepInput(
            classification="memoria_protocolo",
            project="SISTEMA_MEMORIA_AUDITORIA",
            destination="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            chat_index=ChatIndexArtifact(
                nome_sugerido="Registro",
                tipo_indexacao="INDEXAR COMO FONTE",
                projeto_principal="SISTEMA_MEMORIA_AUDITORIA",
                arquivo_drive="memoria.md",
                descricao_curta="Descricao curta",
                potencial_reutilizacao="alto",
            ),
            npt_entry=NPTEntryArtifact(
                tipo="memoria_protocolo",
                projeto="SISTEMA_MEMORIA_AUDITORIA",
                subtipo="simulacao_integrada",
                prioridade="alta",
                destino="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
                modo="consolidar",
                origem="chatgpt",
                conteudo="Conteudo curado",
            ),
        )
    )

    assert result.eligible is True
    assert result.artifact_type == "npt_entry"
    assert result.suggested_project == "SISTEMA_MEMORIA_AUDITORIA"
    assert result.prepared_block.startswith("[NPT_ENTRY]")


def test_npt_prep_generates_chat_index_for_chat_history() -> None:
    result = NPTPrep().prepare(
        NPTPrepInput(
            classification="chat_antigo",
            project="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            destination="CHAT_INDEX_ONLY",
            chat_index=ChatIndexArtifact(
                nome_sugerido="Registro",
                tipo_indexacao="INDEXAR COMO REFERENCIA FRACA",
                projeto_principal="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
                arquivo_drive="",
                descricao_curta="Descricao curta",
                potencial_reutilizacao="medio",
            ),
            npt_entry=None,
        )
    )

    assert result.eligible is True
    assert result.artifact_type == "chat_index"
    assert result.prepared_block.startswith("[CHAT_INDEX]")


def test_npt_prep_returns_review_only_for_non_ingestable_content() -> None:
    result = NPTPrep().prepare(
        NPTPrepInput(
            classification="dev_log",
            project="AMBIENTES_RETOMADA",
            destination="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            chat_index=ChatIndexArtifact(
                nome_sugerido="Registro",
                tipo_indexacao="INDEXAR COMO REFERENCIA FRACA",
                projeto_principal="AMBIENTES_RETOMADA",
                arquivo_drive="",
                descricao_curta="Descricao curta",
                potencial_reutilizacao="baixo",
            ),
            npt_entry=NPTEntryArtifact(
                tipo="dev_log",
                projeto="AMBIENTES_RETOMADA",
                subtipo="simulacao_integrada",
                prioridade="media",
                destino="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
                modo="consolidar",
                origem="chatgpt",
                conteudo="Conteudo curado",
            ),
        )
    )

    assert result.eligible is False
    assert result.artifact_type == "review_only"
    assert result.prepared_block == ""
