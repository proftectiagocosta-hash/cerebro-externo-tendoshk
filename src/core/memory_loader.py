from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class MemoryBundle:
    identity: dict[str, Any]
    projects_catalog: dict[str, Any]


class MemoryLoader:
    def __init__(self, base_path: Path | None = None) -> None:
        self.base_path = base_path or Path(__file__).resolve().parents[2]
        self.identity_path = self.base_path / "memory" / "identity" / "tendoshk_identity.yaml"
        self.projects_catalog_path = (
            self.base_path / "memory" / "projects" / "projects_catalog.yaml"
        )

    def load(self) -> MemoryBundle:
        self._validate_required_files()

        return MemoryBundle(
            identity=self._load_yaml(self.identity_path),
            projects_catalog=self._load_yaml(self.projects_catalog_path),
        )

    def _validate_required_files(self) -> None:
        missing_files = [
            str(path.relative_to(self.base_path))
            for path in (self.identity_path, self.projects_catalog_path)
            if not path.exists()
        ]
        if missing_files:
            missing_list = ", ".join(missing_files)
            raise FileNotFoundError(f"Required memory files were not found: {missing_list}")

    @staticmethod
    def _load_yaml(path: Path) -> dict[str, Any]:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        if not isinstance(data, dict):
            raise ValueError(f"YAML file must contain a mapping at the root: {path}")

        return data


if __name__ == "__main__":
    loader = MemoryLoader()
    bundle = loader.load()
    canonical_projects = bundle.projects_catalog.get("projetos_canonicos", [])

    print("Memory loader test")
    print(f"Base path: {loader.base_path}")
    print(f"Identity file: {loader.identity_path}")
    print(f"Projects file: {loader.projects_catalog_path}")
    print(f"Identity keys: {sorted(bundle.identity.keys())}")
    print(f"Canonical projects: {len(canonical_projects)}")