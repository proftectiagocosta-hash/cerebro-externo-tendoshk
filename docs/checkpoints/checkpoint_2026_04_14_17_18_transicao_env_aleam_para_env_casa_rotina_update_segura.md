# Checkpoint — transicao_env_aleam_para_env_casa_rotina_update_segura

## meta
- projeto: SISTEMA_MEMORIA_AUDITORIA
- linha_de_trabalho: refinamento dos masters TGM, PRESENCA_VIVA e EXECUCAO_REPO com preparacao de rotina segura de atualizacao de documentos soberanos
- repo: proftectiagocosta-hash/cerebro-externo-tendoshk
- branch: main
- commit_referencia: nao_verificado_neste_save
- data_hora: 2026-04-14 17:18 America/Manaus

## estado_atual
- onde_paramos: o repo ja foi atualizado com novo `tgm.md` e com a criacao de `execucao_repo.md`; a reanalise confirmou melhora estrutural do nucleo dos masters; permanece pendente atualizar `docs/masters/presenca_viva.md` para espelhar formalmente a dependencia exclusiva de carga pelo TGM.
- objetivo_ativo: implementar a nova rotina segura de atualizacao de arquivos soberanos usando `presenca_viva.md` como primeiro caso canonico, preservando rastreabilidade e evitando pseudoexecucao de update em arquivo existente.
- status_geral: estado estrategico importante preservado antes da saida do env-aleam, com continuidade planejada para o env-casa.

## decidido
- o `TGM` deve carregar `PRESENCA_VIVA` imediatamente apos sua propria resolucao pelo mestre correspondente.
- o `TGM` e o unico mnemonico autorizado a carregar `PRESENCA_VIVA`.
- o `TGM` tambem passa a carregar `EXECUCAO_REPO` de forma condicional quando houver necessidade real de alteracao versionada autorizada no repositorio.
- `EXECUCAO_REPO` nao substitui `savestateF5`, `loadstateF9` nem `curadoriav61`; governa apenas a integridade da transicao entre proposta e escrita real versionada.
- nao houve conflito estrutural relevante entre `EXECUCAO_REPO` e `savestateF5`; a relacao correta e de camadas diferentes.
- o `presenca_viva.md` ainda precisa ser ajustado para declarar explicitamente sua regra de carregamento como dependencia exclusiva do `TGM`.
- a atualizacao de `presenca_viva.md` sera usada como caso inaugural da nova rotina segura de atualizacao de documentos soberanos.
- o usuario vai sair agora do env-aleam e pretende continuar depois no env-casa.

## preservacoes
- regras_ativas: manter `TGM` como mestre soberano; `PRESENCA_VIVA` como dependente permanente; `EXECUCAO_REPO` como dependente condicional; preservar separacao dura entre modo, manifestacao, curadoria, save, load e escrita versionada.
- trava_antidispersao: nao abrir novas frentes antes de implementar a rotina segura e concluir a atualizacao de `presenca_viva.md`; usar o retorno no env-casa para executar essa linha sem desvio.
- o_que_nao_reabrir_sem_motivo_forte: nao voltar a discutir se `EXECUCAO_REPO` conflita com `savestateF5`; nao reabrir a necessidade do ajuste em `presenca_viva.md`; nao perder a decisao de usar esse arquivo como primeiro caso canonico da nova rotina.

## artefatos_e_fontes
- arquivos_relevantes: docs/masters/tgm.md; docs/masters/presenca_viva.md; docs/masters/execucao_repo.md; docs/masters/savestateF5.md; docs/masters/loadstateF9.md; docs/masters/curadoriav61.md
- modulos_relevantes: arquitetura dos masters do Cérebro Externo Tendoshk; governanca de dependencias TGM -> PRESENCA_VIVA; governanca condicional TGM -> EXECUCAO_REPO
- testes_relevantes: reanalise do repo apos atualizacao; tentativa de update automatico de `presenca_viva.md` falhou por rotina de update sem `sha`; validacao conceitual da nova estrategia de rotina segura por preservacao historica e recriacao do arquivo canonico

## proximo_passo
- proximo_passo_exato: no env-casa, formalizar a nova rotina segura de atualizacao de documentos soberanos e aplica-la ao `docs/masters/presenca_viva.md`, preservando a versao anterior como historico rastreavel e publicando a nova versao canonica ajustada.
- criterio_de_conclusao_do_proximo_passo: rotina definida e aplicada com sucesso ao `presenca_viva.md`, com registro da substituicao historica, novo arquivo canonico publicado e commit realizado de forma honesta e rastreavel.

## retomada_curta
- onde paramos: falta atualizar `presenca_viva.md` para alinhar sua regra de carregamento ao novo `tgm.md`; o repo ja contem `tgm.md` atualizado e `execucao_repo.md` criado.
- o que ja foi decidido: `PRESENCA_VIVA` depende exclusivamente do `TGM`; `EXECUCAO_REPO` e dependente condicional do `TGM`; `presenca_viva.md` sera o primeiro caso da nova rotina segura de atualizacao.
- o proximo passo exato: retomar no env-casa e implementar a rotina segura usando `presenca_viva.md` como caso inaugural.
