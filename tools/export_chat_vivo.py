#!/usr/bin/env python3
"""
EXPORT_CHAT_VIVO v0.1

Executor local/GitHub Actions para preservar chats atuais em Markdown versionado,
com camada RAW, blocos sequenciais, índice, ponteiro current_chat.json e
EV-03.1 deduplicação conservadora por hash exato.

O script NÃO faz curadoria, NÃO resume e NÃO interpreta o conteúdo.
Ele apenas preserva fonte, registra bloco e atualiza índice.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any


PROTOCOL_NAME = "EXPORT_CHAT_VIVO"
PROTOCOL_VERSION = "v0.1"
DEFAULT_BASE_DIR = Path("docs/sistema/export_chat_vivo")
VALID_COVERAGE = {"parcial", "integral_declarada_pelo_usuario", "desconhecida"}


@dataclass
class ChatIndexEntry:
    chat_id: str
    titulo: str
    slug: str
    arquivo: str
    status: str
    cobertura: str
    ultimo_bloco: int
    criado_em: str
    atualizado_em: str
    origem: str
    observacoes: str = ""


@dataclass
class AppendResult:
    chat_id: str
    chat_file: Path
    raw_file: Path | None
    index_md: Path
    index_json: Path
    block_number: int
    content_hash: str | None
    status: str
    coverage: str
    operation: str


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def today_parts() -> tuple[str, str, str]:
    now = datetime.now()
    return now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")


def slugify(text: str, max_len: int = 80) -> str:
    text = text.lower().strip()
    replacements = {
        "á": "a", "à": "a", "ã": "a", "â": "a", "ä": "a",
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "í": "i", "ì": "i", "î": "i", "ï": "i",
        "ó": "o", "ò": "o", "õ": "o", "ô": "o", "ö": "o",
        "ú": "u", "ù": "u", "û": "u", "ü": "u",
        "ç": "c", "ñ": "n",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text[:max_len].strip("_") or "chat_sem_titulo"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def ensure_base_structure(base_dir: Path) -> None:
    (base_dir / "chats").mkdir(parents=True, exist_ok=True)
    (base_dir / "raw").mkdir(parents=True, exist_ok=True)
    if not (base_dir / "index.md").exists():
        write_initial_index_md(base_dir / "index.md")
    if not (base_dir / "index.json").exists():
        write_initial_index_json(base_dir / "index.json")
    if not (base_dir / "current_chat.json").exists():
        write_current_chat(base_dir, chat_id="", arquivo="", status="nenhum", observacoes="Ponteiro do chat vivo ativo.")


def write_initial_index_md(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# EXPORT_CHAT_VIVO — Índice\n\n"
        "| chat_id | titulo | status | cobertura | ultimo_bloco | arquivo | atualizado_em |\n"
        "|---|---|---|---|---:|---|---|\n",
        encoding="utf-8",
    )


def write_initial_index_json(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"protocolo": PROTOCOL_NAME, "versao": PROTOCOL_VERSION, "chats": []}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def current_chat_path(base_dir: Path) -> Path:
    return base_dir / "current_chat.json"


def read_current_chat(base_dir: Path) -> dict[str, Any]:
    path = current_chat_path(base_dir)
    if not path.exists():
        write_current_chat(base_dir, chat_id="", arquivo="", status="nenhum", observacoes="Ponteiro do chat vivo ativo.")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"current_chat.json inválido: {exc}") from exc


def write_current_chat(base_dir: Path, *, chat_id: str, arquivo: str, status: str, observacoes: str = "") -> None:
    path = current_chat_path(base_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "protocolo": PROTOCOL_NAME,
        "versao": PROTOCOL_VERSION,
        "chat_id": chat_id,
        "arquivo": arquivo,
        "status": status,
        "atualizado_em": now_str(),
        "observacoes": observacoes or "Ponteiro do chat vivo ativo.",
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_chat_id(base_dir: Path, explicit_chat_id: str | None) -> str:
    if explicit_chat_id and explicit_chat_id.strip():
        return explicit_chat_id.strip()
    current = read_current_chat(base_dir)
    chat_id = str(current.get("chat_id", "")).strip()
    status = str(current.get("status", "")).strip()
    if not chat_id:
        raise ValueError("chat_id não informado e current_chat.json não possui chat ativo.")
    if status not in {"em_andamento", "pausado"}:
        raise ValueError(f"current_chat.json aponta para chat com status não anexável: {status}")
    return chat_id


def load_index(index_json_path: Path) -> dict[str, Any]:
    if not index_json_path.exists():
        write_initial_index_json(index_json_path)
    try:
        data = json.loads(index_json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"index.json inválido: {index_json_path}: {exc}") from exc
    if "chats" not in data or not isinstance(data["chats"], list):
        raise ValueError("index.json precisa conter uma lista em 'chats'.")
    return data


def save_index(index_json_path: Path, index_md_path: Path, data: dict[str, Any]) -> None:
    index_json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# EXPORT_CHAT_VIVO — Índice",
        "",
        "| chat_id | titulo | status | cobertura | ultimo_bloco | arquivo | atualizado_em |",
        "|---|---|---|---|---:|---|---|",
    ]
    for item in sorted(data["chats"], key=lambda x: (x.get("criado_em", ""), x.get("chat_id", ""))):
        lines.append(
            f"| `{item['chat_id']}` | {escape_md_table(item['titulo'])} | {item['status']} | "
            f"{item['cobertura']} | {item['ultimo_bloco']} | `{item['arquivo']}` | {item['atualizado_em']} |"
        )
    index_md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def escape_md_table(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def find_entry(data: dict[str, Any], chat_id: str) -> dict[str, Any] | None:
    for item in data["chats"]:
        if item.get("chat_id") == chat_id:
            return item
    return None


def build_chat_id(title: str) -> str:
    year, month, day = today_parts()
    return f"{year}_{month}_{day}_{slugify(title, max_len=64)}"


def year_month_paths(base_dir: Path, subdir: str) -> Path:
    year, month, _day = today_parts()
    return base_dir / subdir / year / month


def write_raw_block(base_dir: Path, chat_id: str, block_number: int, content: str, content_hash: str | None = None) -> tuple[Path, str]:
    raw_dir = year_month_paths(base_dir, "raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_path = raw_dir / f"{chat_id}__bloco_{block_number:03}.txt"
    content_hash = content_hash or sha256_text(content)
    raw_path.write_text(content, encoding="utf-8")
    return raw_path, content_hash


def chat_file_path(base_dir: Path, chat_id: str) -> Path:
    year, month, _day = today_parts()
    path = base_dir / "chats" / year / month / f"{chat_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def relative_to_repo(path: Path) -> str:
    return path.as_posix()


def extract_registered_hashes(chat_markdown: str) -> set[str]:
    """Return all SHA-256 hashes already registered in a chat .md.

    EV-03.1 is intentionally conservative: only exact hash matches are treated
    as duplicates. No fuzzy/partial deduplication is performed here.
    """
    hashes: set[str] = set()
    patterns = [
        r"hash_sha256:\s*`?([0-9a-f]{64})`?",
        r"hash_conteudo:\s*([0-9a-f]{64})",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, chat_markdown, flags=re.IGNORECASE):
            hashes.add(match.group(1).lower())
    return hashes


def create_chat_header(*, chat_id: str, title: str, slug: str, status: str, coverage: str, created_at: str, updated_at: str, last_block: int, origin: str, observations: str) -> str:
    return (
        "---\n"
        f"protocolo: {PROTOCOL_NAME}\n"
        f"versao_protocolo: {PROTOCOL_VERSION}\n"
        f"chat_id: {chat_id}\n"
        f"titulo: {title}\n"
        f"slug: {slug}\n"
        f"status: {status}\n"
        f"origem: {origin}\n"
        f"cobertura: {coverage}\n"
        f"criado_em: {created_at}\n"
        f"atualizado_em: {updated_at}\n"
        f"ultimo_bloco: {last_block:03}\n"
        "arquivo_origem: chatgpt_web\n"
        f"observacoes: {observations}\n"
        "---\n\n"
    )


def create_block_markdown(*, block_number: int, origin: str, coverage: str, received_at: str, content_hash: str, raw_path: Path, previous_block: int | None, overlap_status: str) -> str:
    previous = "nenhum" if previous_block is None else f"BLOCO_{previous_block:03}"
    return (
        f"## BLOCO {block_number:03}\n\n"
        "metadados_bloco:\n"
        f"- origem: {origin}\n"
        f"- cobertura_bloco: {coverage}\n"
        f"- recebido_em: {received_at}\n"
        f"- hash_conteudo: {content_hash}\n"
        f"- raw_file: {relative_to_repo(raw_path)}\n"
        f"- bloco_anterior: {previous}\n"
        f"- sobreposicao_tratada: {overlap_status}\n\n"
        f"<!-- EXPORT_CHAT_VIVO_START:BLOCO_{block_number:03} -->\n\n"
        "conteudo: arquivo_externo\n"
        f"arquivo_raw: `{relative_to_repo(raw_path)}`\n"
        f"hash_sha256: `{content_hash}`\n\n"
        f"<!-- EXPORT_CHAT_VIVO_END:BLOCO_{block_number:03} -->\n\n"
    )


def update_header_metadata(content: str, *, status: str, coverage: str, updated_at: str, last_block: int) -> str:
    replacements = {
        r"^status: .*$": f"status: {status}",
        r"^cobertura: .*$": f"cobertura: {coverage}",
        r"^atualizado_em: .*$": f"atualizado_em: {updated_at}",
        r"^ultimo_bloco: .*$": f"ultimo_bloco: {last_block:03}",
    }
    header_end = content.find("---", 3)
    if not content.startswith("---") or header_end == -1:
        raise ValueError("Arquivo de chat sem cabeçalho YAML esperado.")
    header = content[:header_end]
    rest = content[header_end:]
    for pattern, replacement in replacements.items():
        header = re.sub(pattern, replacement, header, flags=re.MULTILINE)
    return header + rest


def init_chat(args: argparse.Namespace) -> AppendResult:
    base_dir = Path(args.base_dir)
    ensure_base_structure(base_dir)
    title = args.title.strip()
    if not title:
        raise ValueError("--title não pode ser vazio.")
    content = read_text_file(Path(args.input))
    if not content.strip():
        raise ValueError("Arquivo de entrada está vazio.")
    coverage = args.coverage
    if coverage not in VALID_COVERAGE:
        raise ValueError(f"Cobertura inválida: {coverage}")
    origin = args.origin
    created_at = now_str()
    chat_id = args.chat_id.strip() if args.chat_id else build_chat_id(title)
    slug = slugify(title)
    chat_path = chat_file_path(base_dir, chat_id)
    if chat_path.exists() and not args.force:
        raise FileExistsError(f"Chat já existe: {chat_path}. Use append ou --force conscientemente.")
    index_json_path = base_dir / "index.json"
    index_md_path = base_dir / "index.md"
    index_data = load_index(index_json_path)
    if find_entry(index_data, chat_id) and not args.force:
        raise ValueError(f"chat_id já existe no índice: {chat_id}")
    content_hash = sha256_text(content)
    raw_path, content_hash = write_raw_block(base_dir, chat_id, 1, content, content_hash)
    header = create_chat_header(chat_id=chat_id, title=title, slug=slug, status="em_andamento", coverage=coverage, created_at=created_at, updated_at=created_at, last_block=1, origin=origin, observations=args.observations or "")
    block = create_block_markdown(block_number=1, origin=origin, coverage=coverage, received_at=created_at, content_hash=content_hash, raw_path=raw_path, previous_block=None, overlap_status="nao_aplicavel")
    chat_path.write_text(header + block, encoding="utf-8")
    entry = ChatIndexEntry(chat_id=chat_id, titulo=title, slug=slug, arquivo=relative_to_repo(chat_path), status="em_andamento", cobertura=coverage, ultimo_bloco=1, criado_em=created_at, atualizado_em=created_at, origem=origin, observacoes=args.observations or "")
    index_data["chats"] = [item for item in index_data["chats"] if item.get("chat_id") != chat_id]
    index_data["chats"].append(asdict(entry))
    save_index(index_json_path, index_md_path, index_data)
    write_current_chat(base_dir, chat_id=chat_id, arquivo=relative_to_repo(chat_path), status="em_andamento", observacoes="Chat ativo definido pelo último init.")
    return AppendResult(chat_id, chat_path, raw_path, index_md_path, index_json_path, 1, content_hash, "em_andamento", coverage, "init")


def append_chat(args: argparse.Namespace) -> AppendResult:
    base_dir = Path(args.base_dir)
    ensure_base_structure(base_dir)
    chat_id = resolve_chat_id(base_dir, args.chat_id)
    content = read_text_file(Path(args.input))
    if not content.strip():
        raise ValueError("Arquivo de entrada está vazio.")
    coverage = args.coverage
    if coverage not in VALID_COVERAGE:
        raise ValueError(f"Cobertura inválida: {coverage}")
    index_json_path = base_dir / "index.json"
    index_md_path = base_dir / "index.md"
    index_data = load_index(index_json_path)
    entry = find_entry(index_data, chat_id)
    if not entry:
        raise ValueError(f"chat_id não encontrado no índice: {chat_id}")
    chat_path = Path(entry["arquivo"])
    if not chat_path.exists():
        raise FileNotFoundError(f"Arquivo de chat registrado no índice não existe: {chat_path}")
    last_block = int(entry.get("ultimo_bloco", 0))
    updated_at = now_str()
    content_hash = sha256_text(content)
    existing_content = chat_path.read_text(encoding="utf-8", errors="replace")
    registered_hashes = extract_registered_hashes(existing_content)
    if content_hash.lower() in registered_hashes:
        print("[CONFIRMADO] duplicado_detectado")
        print("acao=nao_criar_novo_bloco")
        print(f"chat_id={chat_id}")
        print(f"hash_sha256={content_hash}")
        print(f"ultimo_bloco={last_block:03}")
        return AppendResult(chat_id, chat_path, None, index_md_path, index_json_path, last_block, content_hash, entry.get("status", "em_andamento"), coverage, "duplicado_detectado")
    next_block = last_block + 1
    raw_path, content_hash = write_raw_block(base_dir, chat_id, next_block, content, content_hash)
    block = create_block_markdown(block_number=next_block, origin=args.origin, coverage=coverage, received_at=updated_at, content_hash=content_hash, raw_path=raw_path, previous_block=last_block, overlap_status="nao")
    updated_content = update_header_metadata(existing_content, status=entry.get("status", "em_andamento"), coverage=coverage, updated_at=updated_at, last_block=next_block)
    chat_path.write_text(updated_content.rstrip() + "\n\n" + block, encoding="utf-8")
    entry["ultimo_bloco"] = next_block
    entry["atualizado_em"] = updated_at
    entry["cobertura"] = coverage
    entry["origem"] = args.origin
    save_index(index_json_path, index_md_path, index_data)
    write_current_chat(base_dir, chat_id=chat_id, arquivo=relative_to_repo(chat_path), status=entry.get("status", "em_andamento"), observacoes="Chat ativo atualizado pelo último append.")
    return AppendResult(chat_id, chat_path, raw_path, index_md_path, index_json_path, next_block, content_hash, entry.get("status", "em_andamento"), coverage, "append")


def close_chat(args: argparse.Namespace) -> AppendResult | None:
    base_dir = Path(args.base_dir)
    ensure_base_structure(base_dir)
    chat_id = resolve_chat_id(base_dir, args.chat_id)
    index_json_path = base_dir / "index.json"
    index_md_path = base_dir / "index.md"
    index_data = load_index(index_json_path)
    entry = find_entry(index_data, chat_id)
    if not entry:
        raise ValueError(f"chat_id não encontrado no índice: {chat_id}")
    updated_at = now_str()
    entry["status"] = "fechado"
    entry["atualizado_em"] = updated_at
    chat_path = Path(entry["arquivo"])
    if not chat_path.exists():
        raise FileNotFoundError(f"Arquivo de chat registrado no índice não existe: {chat_path}")
    content = chat_path.read_text(encoding="utf-8", errors="replace")
    updated_content = update_header_metadata(content, status="fechado", coverage=entry.get("cobertura", "desconhecida"), updated_at=updated_at, last_block=int(entry.get("ultimo_bloco", 0)))
    chat_path.write_text(updated_content, encoding="utf-8")
    save_index(index_json_path, index_md_path, index_data)
    write_current_chat(base_dir, chat_id=chat_id, arquivo=relative_to_repo(chat_path), status="fechado", observacoes="Chat fechado pelo comando close.")
    result = AppendResult(chat_id, chat_path, None, index_md_path, index_json_path, int(entry.get("ultimo_bloco", 0)), None, "fechado", entry.get("cobertura", "desconhecida"), "close")
    print_result(result)
    return None


def print_result(result: AppendResult) -> None:
    print("[CONFIRMADO] Operação EXPORT_CHAT_VIVO concluída")
    print(f"operacao={result.operation}")
    print(f"chat_id={result.chat_id}")
    print(f"status={result.status}")
    print(f"cobertura={result.coverage}")
    print(f"ultimo_bloco={result.block_number:03}")
    print(f"chat_file={result.chat_file}")
    if result.raw_file:
        print(f"raw_file={result.raw_file}")
    if result.content_hash:
        print(f"hash_sha256={result.content_hash}")
    print(f"index_md={result.index_md}")
    print(f"index_json={result.index_json}")
    print(f"current_chat={current_chat_path(DEFAULT_BASE_DIR)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Executor local do EXPORT_CHAT_VIVO")
    parser.add_argument("--base-dir", default=str(DEFAULT_BASE_DIR), help="Diretório base do protocolo")
    subparsers = parser.add_subparsers(dest="command", required=True)
    init_p = subparsers.add_parser("init", help="Criar novo chat vivo")
    init_p.add_argument("--title", required=True, help="Título humano do chat")
    init_p.add_argument("--input", required=True, help="Arquivo .txt com conteúdo inicial")
    init_p.add_argument("--chat-id", default="", help="ID manual opcional do chat")
    init_p.add_argument("--coverage", default="integral_declarada_pelo_usuario", choices=sorted(VALID_COVERAGE))
    init_p.add_argument("--origin", default="ctrl_a_usuario")
    init_p.add_argument("--observations", default="")
    init_p.add_argument("--force", action="store_true", help="Permite sobrescrever entrada existente conscientemente")
    append_p = subparsers.add_parser("append", help="Anexar bloco a chat vivo existente")
    append_p.add_argument("--chat-id", default="", help="Opcional; se omitido, usa current_chat.json")
    append_p.add_argument("--input", required=True)
    append_p.add_argument("--coverage", default="integral_declarada_pelo_usuario", choices=sorted(VALID_COVERAGE))
    append_p.add_argument("--origin", default="ctrl_a_usuario")
    close_p = subparsers.add_parser("close", help="Fechar chat vivo")
    close_p.add_argument("--chat-id", default="", help="Opcional; se omitido, usa current_chat.json")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "init":
            print_result(init_chat(args))
        elif args.command == "append":
            print_result(append_chat(args))
        elif args.command == "close":
            close_chat(args)
        else:
            parser.error(f"Comando desconhecido: {args.command}")
    except Exception as exc:
        print(f"[ERRO] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
