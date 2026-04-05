from __future__ import annotations

from dataclasses import dataclass

from src.agents.curator_renderer import render_chat_index_block, render_npt_entry_block


@dataclass(frozen=True)
class CuratorInput:
    titulo_sugerido: str
    tipo_entrada: str
    tipo_indexacao: str
    projeto_principal: str
    descricao_curta: str
    potencial_reutilizacao: str
    conteudo: str
    arquivo_drive: str = ""
    subtipo: str = ""
    prioridade: str = "media"
    destino: str = ""


@dataclass(frozen=True)
class ChatIndexArtifact:
    nome_sugerido: str
    tipo_indexacao: str
    projeto_principal: str
    arquivo_drive: str
    descricao_curta: str
    potencial_reutilizacao: str


@dataclass(frozen=True)
class NPTEntryArtifact:
    tipo: str
    projeto: str
    subtipo: str
    prioridade: str
    destino: str
    modo: str
    origem: str
    conteudo: str


@dataclass(frozen=True)
class CuratorOutput:
    chat_index: ChatIndexArtifact
    npt_entry: NPTEntryArtifact | None

    @property
    def chat_index_block(self) -> str:
        return render_chat_index_block(self.chat_index)

    @property
    def npt_entry_block(self) -> str:
        if self.npt_entry is None:
            return ""
        return render_npt_entry_block(self.npt_entry)


class Curator:
    def curate(self, data: CuratorInput) -> CuratorOutput:
        chat_index = self._build_chat_index_artifact(data)
        npt_entry = None

        if data.tipo_entrada != "indefinido":
            npt_entry = self._build_npt_entry_artifact(data)

        return CuratorOutput(
            chat_index=chat_index,
            npt_entry=npt_entry,
        )

    @staticmethod
    def _build_chat_index_artifact(data: CuratorInput) -> ChatIndexArtifact:
        return ChatIndexArtifact(
            nome_sugerido=data.titulo_sugerido,
            tipo_indexacao=data.tipo_indexacao,
            projeto_principal=data.projeto_principal,
            arquivo_drive=data.arquivo_drive,
            descricao_curta=data.descricao_curta,
            potencial_reutilizacao=data.potencial_reutilizacao,
        )

    @staticmethod
    def _build_npt_entry_artifact(data: CuratorInput) -> NPTEntryArtifact:
        return NPTEntryArtifact(
            tipo=data.tipo_entrada,
            projeto=data.projeto_principal,
            subtipo=data.subtipo,
            prioridade=data.prioridade,
            destino=data.destino,
            modo="consolidar",
            origem="chatgpt",
            conteudo=data.conteudo,
        )


if __name__ == "__main__":
    curator = Curator()
    example = CuratorInput(
        titulo_sugerido="Decisao inicial do piloto",
        tipo_entrada="decisao_estrategica",
        tipo_indexacao="INDEXAR COMO FONTE",
        projeto_principal="TENDOSHK_CENTRAL",
        descricao_curta="Define um direcionamento inicial para o projeto piloto.",
        potencial_reutilizacao="alto",
        conteudo="Priorizar componentes simples, reutilizaveis e testaveis nesta primeira fase.",
        arquivo_drive="tendoshk_central.md",
        subtipo="direcionamento_inicial",
        prioridade="alta",
        destino="NPT_NUCLEO_PERSISTENTE_TENDOSHK",
    )
    result = curator.curate(example)

    print("Curator test")
    print(result.chat_index_block)
    print("---")
    print(result.npt_entry_block)
