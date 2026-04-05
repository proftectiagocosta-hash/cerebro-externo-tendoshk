from src.agents.curator import Curator, CuratorInput


curator = Curator()


def test_curator_generates_chat_index_always() -> None:
    result = curator.curate(
        CuratorInput(
            titulo_sugerido="Teste",
            tipo_entrada="indefinido",
            tipo_indexacao="INDEXAR COMO REFERENCIA FRACA",
            projeto_principal="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            descricao_curta="Descricao curta",
            potencial_reutilizacao="baixo",
            conteudo="Conteudo base",
        )
    )

    assert result.chat_index.nome_sugerido == "Teste"
    assert result.chat_index.tipo_indexacao == "INDEXAR COMO REFERENCIA FRACA"
    assert "[CHAT_INDEX]" in result.chat_index_block
    assert "[/CHAT_INDEX]" in result.chat_index_block


def test_curator_generates_npt_entry_for_defined_input() -> None:
    result = curator.curate(
        CuratorInput(
            titulo_sugerido="Teste",
            tipo_entrada="decisao_estrategica",
            tipo_indexacao="INDEXAR COMO FONTE",
            projeto_principal="TENDOSHK_CENTRAL",
            descricao_curta="Descricao curta",
            potencial_reutilizacao="alto",
            conteudo="Conteudo base",
            destino="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
        )
    )

    assert result.npt_entry is not None
    assert result.npt_entry.tipo == "decisao_estrategica"
    assert result.npt_entry.projeto == "TENDOSHK_CENTRAL"
    assert "[NPT_ENTRY]" in result.npt_entry_block
    assert "[/NPT_ENTRY]" in result.npt_entry_block


def test_curator_skips_npt_entry_for_indefinido() -> None:
    result = curator.curate(
        CuratorInput(
            titulo_sugerido="Teste",
            tipo_entrada="indefinido",
            tipo_indexacao="INDEXAR COMO REFERENCIA FRACA",
            projeto_principal="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
            descricao_curta="Descricao curta",
            potencial_reutilizacao="baixo",
            conteudo="Conteudo base",
        )
    )

    assert result.npt_entry is None
    assert result.npt_entry_block == ""
