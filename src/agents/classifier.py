from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClassifierResult:
    tipo_entrada: str
    confianca: float
    justificativa: str


class TextClassifier:
    CATEGORY_RULES: dict[str, tuple[str, ...]] = {
        "chat_antigo": ("conversa", "chat", "mensagem", "resposta", "pergunta"),
        "artefato_tecnico": ("api", "funcao", "erro", "codigo", "yaml", "json"),
        "decisao_estrategica": ("estrategia", "prioridade", "direcao", "roadmap"),
        "dev_log": ("dev log", "devlog", "checkpoint", "progresso", "implementado", "teste local"),
        "memoria_protocolo": ("protocolo", "memoria", "procedimento", "fluxo", "governanca"),
    }

    def classify(self, text: str) -> ClassifierResult:
        normalized_text = text.strip().lower()
        if not normalized_text:
            return ClassifierResult(
                tipo_entrada="indefinido",
                confianca=0.0,
                justificativa="Texto vazio ou sem sinais suficientes para classificacao.",
            )

        best_category = "indefinido"
        best_matches: list[str] = []

        for category, keywords in self.CATEGORY_RULES.items():
            matches = [keyword for keyword in keywords if keyword in normalized_text]
            if len(matches) > len(best_matches):
                best_category = category
                best_matches = matches

        if not best_matches:
            return ClassifierResult(
                tipo_entrada="indefinido",
                confianca=0.2,
                justificativa="Nenhuma heuristica simples encontrou palavras-chave relevantes.",
            )

        confidence = min(1.0, 0.35 + 0.2 * len(best_matches))
        justification = f"Categoria detectada por palavras-chave: {', '.join(best_matches)}."

        return ClassifierResult(
            tipo_entrada=best_category,
            confianca=confidence,
            justificativa=justification,
        )


if __name__ == "__main__":
    classifier = TextClassifier()
    examples = [
        "Dev log da sprint: implementado loader YAML e teste local executado.",
        "Precisamos decidir a prioridade e a direcao do roadmap do projeto piloto.",
        "Documento com protocolo operacional e memoria de procedimentos internos.",
    ]

    for example in examples:
        result = classifier.classify(example)
        print(f"Texto: {example}")
        print(f"Tipo: {result.tipo_entrada}")
        print(f"Confianca: {result.confianca:.2f}")
        print(f"Justificativa: {result.justificativa}")
        print("---")