from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.pipeline import PipelineResult, TendoshkPipeline


EXAMPLE_TEXT = (
    "Precisamos definir a prioridade e a direcao do roadmap do projeto piloto "
    "TENDOSHK_CENTRAL para consolidar componentes reutilizaveis."
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Executa o piloto do Cerebro Externo Tendoshk.")
    parser.add_argument("--text", help="Texto de entrada para o pipeline do piloto.")
    parser.add_argument("--file", help="Caminho de um arquivo de texto para servir como entrada.")
    parser.add_argument("--output", help="Caminho de um arquivo para salvar a saida textual.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    return parser


def resolve_input_text(args: argparse.Namespace, parser: argparse.ArgumentParser) -> str:
    if args.text:
        return args.text

    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            parser.error(f"arquivo nao encontrado: {args.file}")
        return file_path.read_text(encoding="utf-8")

    return EXAMPLE_TEXT


def render_text_output(result: PipelineResult) -> str:
    lines = [
        "Simulacao integrada do Cerebro Externo Tendoshk",
        (
            f"Memoria carregada: nome={result.memory_bundle.identity.get('nome')} | "
            f"projetos={len(result.memory_bundle.projects_catalog.get('projetos_canonicos', []))}"
        ),
        "Classificacao",
        f"tipo_entrada={result.classification.tipo_entrada}",
        f"confianca={result.classification.confianca:.2f}",
        f"justificativa={result.classification.justificativa}",
        "Prioridade",
        f"score_total={result.priority_result.score_total:.2f}",
        f"classificacao={result.priority_result.classificacao}",
        "Roteamento",
        f"projeto_sugerido={result.routing_result.projeto_sugerido}",
        f"tipo_indexacao={result.routing_result.tipo_indexacao}",
        f"prioridade_sugerida={result.routing_result.prioridade_sugerida}",
        f"destino_sugerido={result.routing_result.destino_sugerido}",
        f"justificativa={result.routing_result.justificativa}",
        "CHAT_INDEX",
        result.curated_output.chat_index_block,
    ]

    if result.curated_output.npt_entry_block:
        lines.extend(["NPT_ENTRY", result.curated_output.npt_entry_block])

    return "\n".join(lines)


def build_json_output(result: PipelineResult) -> dict[str, object]:
    return {
        "memoria_resumo": {
            "nome": result.memory_bundle.identity.get("nome"),
            "projetos": len(result.memory_bundle.projects_catalog.get("projetos_canonicos", [])),
        },
        "classificacao": {
            "tipo_entrada": result.classification.tipo_entrada,
            "confianca": result.classification.confianca,
            "justificativa": result.classification.justificativa,
        },
        "prioridade": {
            "score_total": result.priority_result.score_total,
            "classificacao": result.priority_result.classificacao,
        },
        "roteamento": {
            "projeto_sugerido": result.routing_result.projeto_sugerido,
            "tipo_indexacao": result.routing_result.tipo_indexacao,
            "prioridade_sugerida": result.routing_result.prioridade_sugerida,
            "destino_sugerido": result.routing_result.destino_sugerido,
            "justificativa": result.routing_result.justificativa,
        },
        "chat_index_block": result.curated_output.chat_index_block,
        "npt_entry_block": result.curated_output.npt_entry_block,
    }


def render_output(result: PipelineResult, output_format: str) -> str:
    if output_format == "json":
        return json.dumps(build_json_output(result), ensure_ascii=False, indent=2)
    return render_text_output(result)


def maybe_write_output(output_text: str, output_path: str | None) -> None:
    if not output_path:
        return

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output_text, encoding="utf-8")


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    input_text = resolve_input_text(args, parser)

    pipeline = TendoshkPipeline()
    result = pipeline.run(input_text)
    output_text = render_output(result, args.format)

    print(output_text)
    maybe_write_output(output_text, args.output)