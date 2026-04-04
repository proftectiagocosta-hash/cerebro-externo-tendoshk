import json
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = PROJECT_ROOT / "src" / "cli" / "main.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CLI_PATH), *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )


def test_cli_uses_example_text_without_arguments() -> None:
    result = run_cli()

    assert result.returncode == 0
    assert "Memoria carregada:" in result.stdout
    assert "Classificacao" in result.stdout
    assert "Prioridade" in result.stdout
    assert "score_maximo=" in result.stdout
    assert "percentual=" in result.stdout
    assert "Roteamento" in result.stdout
    assert "CHAT_INDEX" in result.stdout


def test_cli_runs_with_text_argument() -> None:
    result = run_cli(
        "--text",
        "Documento de protocolo e memoria de procedimento para padronizar o fluxo interno do projeto.",
    )

    assert result.returncode == 0
    assert "tipo_entrada=memoria_protocolo" in result.stdout


def test_cli_json_output_contains_main_fields() -> None:
    result = run_cli(
        "--text",
        "Documento de protocolo e memoria de procedimento para padronizar o fluxo interno do projeto.",
        "--format",
        "json",
    )

    payload = json.loads(result.stdout)

    assert result.returncode == 0
    assert payload["memoria_resumo"]["nome"] == "Tendoshk"
    assert "classificacao" in payload
    assert payload["prioridade"]["score_total"] >= 0
    assert "score_maximo" in payload["prioridade"]
    assert "percentual" in payload["prioridade"]
    assert "roteamento" in payload
    assert payload["chat_index_block"]


def test_cli_creates_output_file(tmp_path: Path) -> None:
    output_path = tmp_path / "outputs" / "resultado.txt"

    result = run_cli(
        "--text",
        "Documento de protocolo e memoria de procedimento para padronizar o fluxo interno do projeto.",
        "--output",
        str(output_path),
    )

    assert result.returncode == 0
    assert output_path.exists()
    assert "CHAT_INDEX" in output_path.read_text(encoding="utf-8")


def test_cli_reads_text_from_file(tmp_path: Path) -> None:
    input_path = tmp_path / "entrada.txt"
    input_path.write_text(
        "Documento de protocolo e memoria de procedimento para padronizar o fluxo interno do projeto.",
        encoding="utf-8",
    )

    result = run_cli("--file", str(input_path))

    assert result.returncode == 0
    assert "tipo_entrada=memoria_protocolo" in result.stdout


def test_cli_fails_for_missing_input_file() -> None:
    result = run_cli("--file", "arquivo_inexistente.txt")

    assert result.returncode != 0
    assert "arquivo nao encontrado" in result.stderr