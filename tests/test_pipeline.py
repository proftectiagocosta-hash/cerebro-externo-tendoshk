from src.core.pipeline import TendoshkPipeline


def test_pipeline_runs_integrated_flow_for_strategic_text() -> None:
    pipeline = TendoshkPipeline()
    result = pipeline.run(
        "Precisamos definir a prioridade e a direcao do roadmap do projeto piloto "
        "TENDOSHK_CENTRAL para consolidar componentes reutilizaveis."
    )

    assert result.memory_bundle.identity["nome"] == "Tendoshk"
    assert result.classification.tipo_entrada != "indefinido"
    assert result.priority_result.score_total >= 0
    assert result.routing_result.projeto_sugerido
    assert result.curated_output.chat_index_block
    assert result.curated_output.npt_entry_block