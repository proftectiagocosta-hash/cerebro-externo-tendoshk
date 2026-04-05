from __future__ import annotations

LOW_MATURITY_TERMS = ("rascunho", "incompleto", "sem decisao", "sem dono")
LOW_SIGNAL_CHAT_TERMS = ("conversa curta", "sem profundidade", "descartavel")
REVIEW_REQUIRED_TECH_TERMS = ("instavel", "ajuste rapido", "deve ser revisada")


def normalize_semantic_content(content: str) -> str:
    return content.strip().lower()


def has_low_maturity_protocol_signals(content: str) -> bool:
    return _has_any_term(content, LOW_MATURITY_TERMS)


def has_low_signal_chat_noise(content: str) -> bool:
    return _has_any_term(content, LOW_SIGNAL_CHAT_TERMS)


def has_review_required_technical_signals(content: str) -> bool:
    return _has_any_term(content, REVIEW_REQUIRED_TECH_TERMS)


def _has_any_term(content: str, terms: tuple[str, ...]) -> bool:
    return any(term in content for term in terms)
