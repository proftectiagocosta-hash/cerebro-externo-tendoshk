from __future__ import annotations

LOW_MATURITY_TERMS = ("rascunho", "incompleto", "sem decisao", "sem dono")
LOW_SIGNAL_CHAT_TERMS = ("conversa curta", "sem profundidade", "descartavel")
REVIEW_REQUIRED_TECH_TERMS = ("instavel", "ajuste rapido", "deve ser revisada")
MULTI_INTENT_STRATEGIC_TERMS = ("prioridade", "direcao", "roadmap", "estrategia")
MULTI_INTENT_TECHNICAL_TERMS = ("codigo", "json", "yaml", "api", "funcao", "erro")
MULTI_INTENT_OPERATIONAL_TERMS = ("ambiente", "wsl", "retomada", "operacional", "checkpoint")


def normalize_semantic_content(content: str) -> str:
    return content.strip().lower()


def has_low_maturity_protocol_signals(content: str) -> bool:
    return _has_any_term(content, LOW_MATURITY_TERMS)


def has_low_signal_chat_noise(content: str) -> bool:
    return _has_any_term(content, LOW_SIGNAL_CHAT_TERMS)


def has_review_required_technical_signals(content: str) -> bool:
    return _has_any_term(content, REVIEW_REQUIRED_TECH_TERMS)


def has_low_canonicity_multi_intent_signals(content: str) -> bool:
    return (
        _has_any_term(content, MULTI_INTENT_STRATEGIC_TERMS)
        and _has_any_term(content, MULTI_INTENT_TECHNICAL_TERMS)
        and _has_any_term(content, MULTI_INTENT_OPERATIONAL_TERMS)
    )


def _has_any_term(content: str, terms: tuple[str, ...]) -> bool:
    return any(term in content for term in terms)
