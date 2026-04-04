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
class CuratorOutput:
    chat_index_block: str
    npt_entry_block: str


class Curator:
    def curate(self, data: CuratorInput) -> CuratorOutput:
        chat_index_block = self._build_chat_index_block(data)
        npt_entry_block = ""

        if data.tipo_entrada != "indefinido":
            npt_entry_block = self._build_npt_entry_block(data)

        return CuratorOutput(
            chat_index_block=chat_index_block,
            npt_entry_block=npt_entry_block,
        )

    @staticmethod
    def _build_chat_index_block(data: CuratorInput) -> str:
        return "\n".join(
            [
                "[CHAT_INDEX]",
                f"nome_sugerido={data.titulo_sugerido}",
                f"tipo_indexacao={data.tipo_indexacao}",
                f"projeto_principal={data.projeto_principal}",
                f"arquivo_drive={data.arquivo_drive}",
                f"descricao_curta={data.descricao_curta}",
                f"potencial_reutilizacao={data.potencial_reutilizacao}",
                "[/CHAT_INDEX]",
            ]
        )

    @staticmethod
    def _build_npt_entry_block(data: CuratorInput) -> str:
        return "\n".join(
            [
                "[NPT_ENTRY]",
                f"tipo={data.tipo_entrada}",
                f"projeto={data.projeto_principal}",
                f"subtipo={data.subtipo}",
                f"prioridade={data.prioridade}",
                f"destino={data.destino}",
                "modo=consolidar",
                "origem=chatgpt",
                f"conteudo={data.conteudo}",
                "[/NPT_ENTRY]",
            ]
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