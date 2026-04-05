from src.core.npt_prep import NPTPrep


def test_npt_prep_generates_npt_entry_for_structural_content() -> None:
    result = NPTPrep().prepare(
        {
            "classification": "memoria_protocolo",
            "priority": "alta",
            "project": "SISTEMA_MEMORIA_AUDITORIA",
            "destination": "NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            "chat_index_block": "[CHAT_INDEX]\nconteudo=indice\n[/CHAT_INDEX]",
            "npt_entry_block": "[NPT_ENTRY]\nconteudo=curado\n[/NPT_ENTRY]",
        }
    )

    assert result.eligible is True
    assert result.artifact_type == "npt_entry"
    assert result.suggested_project == "SISTEMA_MEMORIA_AUDITORIA"
    assert result.prepared_block.startswith("[NPT_ENTRY]")


def test_npt_prep_generates_chat_index_for_chat_history() -> None:
    result = NPTPrep().prepare(
        {
            "classification": "chat_antigo",
            "priority": "media",
            "project": "NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            "destination": "CHAT_INDEX_ONLY",
            "chat_index_block": "[CHAT_INDEX]\nconteudo=indice\n[/CHAT_INDEX]",
            "npt_entry_block": "",
        }
    )

    assert result.eligible is True
    assert result.artifact_type == "chat_index"
    assert result.prepared_block.startswith("[CHAT_INDEX]")


def test_npt_prep_returns_review_only_for_non_ingestable_content() -> None:
    result = NPTPrep().prepare(
        {
            "classification": "dev_log",
            "priority": "media",
            "project": "AMBIENTES_RETOMADA",
            "destination": "NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            "chat_index_block": "[CHAT_INDEX]\nconteudo=indice\n[/CHAT_INDEX]",
            "npt_entry_block": "[NPT_ENTRY]\nconteudo=curado\n[/NPT_ENTRY]",
        }
    )

    assert result.eligible is False
    assert result.artifact_type == "review_only"
    assert result.prepared_block == ""
