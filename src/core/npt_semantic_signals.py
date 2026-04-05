from __future__ import annotations

LOW_MATURITY_TERMS = ("rascunho", "incompleto", "sem decisao", "sem dono")
LOW_SIGNAL_CHAT_TERMS = ("conversa curta", "sem profundidade", "descartavel")
REVIEW_REQUIRED_TECH_TERMS = ("instavel", "ajuste rapido", "deve ser revisada")
MULTI_INTENT_STRATEGIC_TERMS = ("prioridade", "direcao", "roadmap", "estrategia")
MULTI_INTENT_TECHNICAL_TERMS = ("codigo", "json", "yaml", "api", "funcao", "erro")
MULTI_INTENT_OPERATIONAL_TERMS = ("ambiente", "wsl", "retomada", "operacional", "checkpoint")
HYBRID_STRATEGIC_OPERATIONAL_TERMS = ("checkpoint", "ambiente", "wsl", "retomada")


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


def has_low_canonicity_hybrid_strategy_signals(content: str) -> bool:
    strategic_matches = _count_terms(content, MULTI_INTENT_STRATEGIC_TERMS)
    operational_matches = _count_terms(content, HYBRID_STRATEGIC_OPERATIONAL_TERMS)
    return strategic_matches >= 3 and operational_matches >= 2


def _has_any_term(content: str, terms: tuple[str, ...]) -> bool:
    return any(term in content for term in terms)


def _count_terms(content: str, terms: tuple[str, ...]) -> int:
    return sum(1 for term in terms if term in content)
