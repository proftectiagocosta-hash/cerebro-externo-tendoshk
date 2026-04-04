from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.pipeline import TendoshkPipeline


EXAMPLE_TEXT = (
    "Precisamos definir a prioridade e a direcao do roadmap do projeto piloto "
    "TENDOSHK_CENTRAL para consolidar componentes reutilizaveis."
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Executa o piloto do Cerebro Externo Tendoshk.")
    parser.add_argument("--text", help="Texto de entrada para o pipeline do piloto.")
    return parser


if __name__ == "__main__":
    args = build_parser().parse_args()
    input_text = args.text or EXAMPLE_TEXT

    pipeline = TendoshkPipeline()
    result = pipeline.run(input_text)

    print("Simulacao integrada do Cerebro Externo Tendoshk")
    print(
        f"Memoria carregada: nome={result.memory_bundle.identity.get('nome')} | "
        f"projetos={len(result.memory_bundle.projects_catalog.get('projetos_canonicos', []))}"
    )
    print("Classificacao")
    print(f"tipo_entrada={result.classification.tipo_entrada}")
    print(f"confianca={result.classification.confianca:.2f}")
    print(f"justificativa={result.classification.justificativa}")
    print("Prioridade")
    print(f"score_total={result.priority_result.score_total:.2f}")
    print(f"classificacao={result.priority_result.classificacao}")
    print("Roteamento")
    print(f"projeto_sugerido={result.routing_result.projeto_sugerido}")
    print(f"tipo_indexacao={result.routing_result.tipo_indexacao}")
    print(f"prioridade_sugerida={result.routing_result.prioridade_sugerida}")
    print(f"destino_sugerido={result.routing_result.destino_sugerido}")
    print(f"justificativa={result.routing_result.justificativa}")
    print("CHAT_INDEX")
    print(result.curated_output.chat_index_block)

    if result.curated_output.npt_entry_block:
        print("NPT_ENTRY")
        print(result.curated_output.npt_entry_block)