# Checkpoint — correcao_do_bootstrap_e_resolucao_deterministica_dos_mnemonicos

## meta
- projeto: NPT_NUCLEO_PERSISTENTE_TENDOSHK
- linha_de_trabalho: consolidacao_do_bootstrap_conversacional_com_resolucao_deterministica_dos_mnemonicos_do_cerebro_tendoshk
- repo: proftectiagocosta-hash/cerebro-externo-tendoshk
- branch: main
- commit_referencia: nao_verificado_nesta_sessao
- data_hora: 2026-04-13 12:58 UTC-04

## estado_atual
- onde_paramos: a arquitetura soberana ja estava formalizada e o bootstrap em chat novo ja existia por `ativacao_tgm_chat.md`, mas um teste real mostrou que a ativacao inicial ainda permitia improviso semantico; por isso foi criada a clausula de resolucao deterministica dos mnemonicos e entregue a versao corrigida do `ativacao_tgm_chat.md`
- objetivo_ativo: tornar o bootstrap em chat novo realmente confiavel e impedir que os mnemonicos sejam resolvidos por semantica frouxa em vez de arquivo mestre explicito
- status_geral: arquitetura madura; bootstrap corrigido conceitualmente; falta salvar a versao corrigida e validar em teste real

## decidido
- o comportamento observado no outro chat nao esta aprovado como padrao
- apos a ativacao do regime, cada mnemonic deve ser resolvido explicitamente pelo arquivo mestre correspondente
- `TGM no github` / `tgm no github` devem apontar para `docs/masters/tgm.md`
- `loadstateF9 no github` deve apontar para `docs/masters/loadstateF9.md`
- `savestateF5 no github` deve apontar para `docs/masters/savestateF5.md`
- `curadoriav61 no github` deve apontar para `docs/masters/curadoriav61.md`
- e proibido substituir a leitura do arquivo mestre correspondente por README generico, leitura generica do repo, checkpoint fora da rotina correta, aproximacao semantica ou improviso operacional
- a versao corrigida do `ativacao_tgm_chat.md` com a clausula de resolucao deterministica foi entregue

## preservacoes
- regras_ativas: manter os 4 mestres permanentes e os checkpoints como unica camada volatil; exigir ativacao do regime em chat novo; exigir resolucao deterministica dos mnemonicos via arquivo mestre explicito; manter TGM como comando de modo e F9/F5/V61 como acoes autoencerraveis
- trava_antidispersao: nao considerar o bootstrap validado antes de testar a versao corrigida do `ativacao_tgm_chat.md` em chat novo; o foco imediato e confirmar que `tgm no github` abre `docs/masters/tgm.md` explicitamente
- o_que_nao_reabrir_sem_motivo_forte: nao voltar a permitir inferencia semantica livre dos mnemonicos; nao tratar a ativacao como suficiente se ela nao obrigar leitura do arquivo mestre correspondente; nao misturar bootstrap com execucao automatica das acoes

## artefatos_e_fontes
- arquivos_relevantes: docs/masters/tgm.md; docs/masters/curadoriav61.md; docs/masters/savestateF5.md; docs/masters/loadstateF9.md; ativacao_tgm_chat.md
- modulos_relevantes: bootstrap_conversacional_do_regime_de_mnemonicos_com_resolucao_deterministica
- testes_relevantes: teste real pendente em chat novo com a versao corrigida do `ativacao_tgm_chat.md` seguido de `tgm no github`

## proximo_passo
- proximo_passo_exato: salvar este checkpoint, substituir no repositorio o `ativacao_tgm_chat.md` pela versao corrigida e depois testar em chat novo com a ordem `ativacao_tgm_chat.md` -> `tgm no github`
- criterio_de_conclusao_do_proximo_passo: o sistema deve abrir explicitamente `docs/masters/tgm.md` ao receber `tgm no github`, sem recorrer a inferencia semantica do repositorio

## retomada_curta
- onde paramos: paramos com o bootstrap conversacional corrigido conceitualmente para resolucao deterministica dos mnemonicos
- o que ja foi decidido: o comportamento anterior nao foi aprovado; cada mnemonic deve apontar explicitamente para seu arquivo mestre; o `ativacao_tgm_chat.md` foi reescrito com essa clausula
- o proximo passo exato: salvar este checkpoint, atualizar `ativacao_tgm_chat.md` no repo e validar `tgm no github` em chat novo
