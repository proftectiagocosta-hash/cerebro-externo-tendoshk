from src.agents.classifier import TextClassifier


classifier = TextClassifier()


def test_classifier_identifies_decisao_estrategica() -> None:
    result = classifier.classify("Precisamos definir a prioridade e o roadmap do projeto.")

    assert result.tipo_entrada == "decisao_estrategica"
    assert result.confianca > 0


def test_classifier_identifies_memoria_protocolo() -> None:
    result = classifier.classify("Documento de protocolo e memoria de procedimento interno.")

    assert result.tipo_entrada == "memoria_protocolo"
    assert result.confianca > 0


def test_classifier_returns_indefinido_for_empty_text() -> None:
    result = classifier.classify("   ")

    assert result.tipo_entrada == "indefinido"
    assert result.confianca == 0.0