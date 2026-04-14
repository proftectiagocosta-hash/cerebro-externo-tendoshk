# Checkpoint — bootstrap_de_mnemonicos_e_ativacao_tgm_chat

## meta
- projeto: NPT_NUCLEO_PERSISTENTE_TENDOSHK
- linha_de_trabalho: consolidacao_da_camada_de_bootstrap_conversacional_do_regime_soberano_do_cerebro_tendoshk
- repo: proftectiagocosta-hash/cerebro-externo-tendoshk
- branch: main
- commit_referencia: nao_verificado_nesta_sessao
- data_hora: 2026-04-13 12:45 UTC-04

## estado_atual
- onde_paramos: a arquitetura soberana ja possuia os 4 mestres permanentes e a camada de checkpoints, mas foi identificado que em chat virgem os mnemonicos nao existem por si; por isso foi criada a logica de um arquivo de ativacao conversacional (`ativacao_tgm_chat.md`) para habilitar soberanamente o regime minimo de mnemonicos antes do uso efetivo de TGM, F9, F5 e V61
- objetivo_ativo: fechar o bootstrap do sistema entre chats novos e tornar a ativacao do regime confiavel antes de executar load/save/curadoria
- status_geral: arquitetura madura; camada de ativacao em chat novo definida conceitualmente; falta materializar e validar em uso real

## decidido
- um chat novo nao deve presumir o significado operacional de `TGM no github`, `loadstateF9 no github`, `savestateF5 no github` e `curadoriav61 no github`
- foi decidido criar `ativacao_tgm_chat.md` como peca de bootstrap conversacional do regime
- `ativacao_tgm_chat.md` nao substitui `docs/masters/tgm.md`; o primeiro e arquivo de uso em chat, o segundo e constituicao permanente no repo
- a funcao do arquivo de ativacao e habilitar soberanamente os mnemonicos e vincular o chat ao repo, sem executar automaticamente TGM/F9/F5/V61
- a versao correta do arquivo de ativacao deve ser minima e focada em habilitacao do regime de mnemonicos, nao em explicacao extensa do sistema

## preservacoes
- regras_ativas: manter separacao entre peca mestre permanente e peca de ativacao conversacional; exigir ativacao do regime em chat novo antes de presumir mnemonicos; usar o repo informado no arquivo de ativacao como referencia versionada; manter TGM como comando de modo e F9/F5/V61 como acoes autoencerraveis
- trava_antidispersao: nao testar mnemônicos em chat novo sem antes enviar o arquivo de ativacao; o foco imediato e validar a camada de bootstrap antes de expandir o sistema
- o_que_nao_reabrir_sem_motivo_forte: nao tratar `ativacao_tgm_chat.md` como substituto de `tgm.md`; nao rebaixar o arquivo de ativacao a mero texto passivo; nao pressupor mnemonicos em chat virgem; nao misturar ativacao do regime com execucao automatica das acoes

## artefatos_e_fontes
- arquivos_relevantes: docs/masters/tgm.md; docs/masters/curadoriav61.md; docs/masters/savestateF5.md; docs/masters/loadstateF9.md; ativacao_tgm_chat.md
- modulos_relevantes: bootstrap_conversacional_do_regime_de_mnemonicos
- testes_relevantes: teste real pendente em chat novo com envio de `ativacao_tgm_chat.md` seguido de `loadstateF9 no github`

## proximo_passo
- proximo_passo_exato: salvar este checkpoint, salvar `ativacao_tgm_chat.md` no repo para manter registro oficial da peca de bootstrap e depois testar em chat novo com a ordem `ativacao_tgm_chat.md` -> `loadstateF9 no github`
- criterio_de_conclusao_do_proximo_passo: um chat novo deve conseguir reconhecer os mnemonicos apos a ativacao e executar corretamente o `loadstateF9 no github`

## retomada_curta
- onde paramos: paramos com a arquitetura soberana pronta e com a camada de ativacao em chat novo definida conceitualmente por `ativacao_tgm_chat.md`
- o que ja foi decidido: chat virgem nao presume mnemonicos; `ativacao_tgm_chat.md` habilita o regime minimo de comandos; TGM e comando de modo; F9/F5/V61 sao acoes autoencerraveis
- o proximo passo exato: salvar este checkpoint, versionar `ativacao_tgm_chat.md` e testar o bootstrap em um chat novo
