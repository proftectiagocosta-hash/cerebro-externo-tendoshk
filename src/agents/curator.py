from __future__ import annotations

from dataclasses import dataclass


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

    def render_block(self) -> str:
        return "\n".join(
            [
                "[CHAT_INDEX]",
                f"nome_sugerido={self.nome_sugerido}",
                f"tipo_indexacao={self.tipo_indexacao}",
                f"projeto_principal={self.projeto_principal}",
                f"arquivo_drive={self.arquivo_drive}",
                f"descricao_curta={self.descricao_curta}",
                f"potencial_reutilizacao={self.potencial_reutilizacao}",
                "[/CHAT_INDEX]",
            ]
        )


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

    def render_block(self) -> str:
        return "\n".join(
            [
                "[NPT_ENTRY]",
                f"tipo={self.tipo}",
                f"projeto={self.projeto}",
                f"subtipo={self.subtipo}",
                f"prioridade={self.prioridade}",
                f"destino={self.destino}",
                f"modo={self.modo}",
                f"origem={self.origem}",
                f"conteudo={self.conteudo}",
                "[/NPT_ENTRY]",
            ]
        )


@dataclass(frozen=True)
class CuratorOutput:
    chat_index: ChatIndexArtifact
    npt_entry: NPTEntryArtifact | None

    @property
    def chat_index_block(self) -> str:
        return self.chat_index.render_block()

    @property
    def npt_entry_block(self) -> str:
        if self.npt_entry is None:
            return ""
        return self.npt_entry.render_block()


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
