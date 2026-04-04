import json
import shutil
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = PROJECT_ROOT / "src" / "cli" / "main.py"


def run_cli(*args: str, project_root: Path = PROJECT_ROOT) -> subprocess.CompletedProcess[str]:
    cli_path = project_root / "src" / "cli" / "main.py"
    return subprocess.run(
        [sys.executable, str(cli_path), *args],
        cwd=project_root,
        capture_output=True,
        text=True,
    )


def make_isolated_project(tmp_path: Path) -> Path:
    project_root = tmp_path / "project"
    shutil.copytree(PROJECT_ROOT / "src", project_root / "src")
    shutil.copytree(PROJECT_ROOT / "memory", project_root / "memory")
    return project_root


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


def test_cli_save_run_creates_json_with_expected_fields(tmp_path: Path) -> None:
    project_root = make_isolated_project(tmp_path)

    result = run_cli(
        "--text",
        "Documento de protocolo e memoria de procedimento para padronizar o fluxo interno do projeto.",
        "--format",
        "json",
        "--save-run",
        project_root=project_root,
    )

    saved_files = list((project_root / "data" / "runs").glob("run_*.json"))
    assert result.returncode == 0
    assert len(saved_files) == 1

    payload = json.loads(saved_files[0].read_text(encoding="utf-8"))
    assert payload["timestamp"]
    assert payload["input_text"]
    assert payload["output_format"] == "json"
    assert payload["output_text"]
    assert "classification" in payload
    assert "priority" in payload
    assert "routing" in payload


def test_cli_export_blocks_creates_chat_index_and_npt_entry_files(tmp_path: Path) -> None:
    project_root = make_isolated_project(tmp_path)

    result = run_cli(
        "--text",
        "Documento de protocolo e memoria de procedimento para padronizar o fluxo interno do projeto.",
        "--export-blocks",
        project_root=project_root,
    )

    chat_index_files = list((project_root / "data" / "exports" / "chat_index").glob("chat_index_*.txt"))
    npt_entry_files = list((project_root / "data" / "exports" / "npt_entry").glob("npt_entry_*.txt"))

    assert result.returncode == 0
    assert len(chat_index_files) == 1
    assert len(npt_entry_files) == 1