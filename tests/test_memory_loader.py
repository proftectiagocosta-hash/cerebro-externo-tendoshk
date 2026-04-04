from src.core.memory_loader import MemoryBundle, MemoryLoader


def test_memory_loader_loads_identity_and_projects_catalog() -> None:
    bundle = MemoryLoader().load()

    assert isinstance(bundle, MemoryBundle)
    assert bundle.identity["nome"] == "Tendoshk"
    assert "projetos_canonicos" in bundle.projects_catalog
    assert len(bundle.projects_catalog["projetos_canonicos"]) > 0