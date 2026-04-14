# Checkpoint — arquitetura_mestres_tgm_f5_f9_v61

## meta
- projeto: NPT_NUCLEO_PERSISTENTE_TENDOSHK
- linha_de_trabalho: formalizacao_do_sistema_soberano_de_modo_curadoria_save_load_e_checkpoints_do_cerebro_tendoshk
- repo: proftectiagocosta-hash/cerebro-externo-tendoshk
- branch: main
- commit_referencia: nao_verificado_nesta_sessao
- data_hora: 2026-04-13 12:13 UTC-04

## estado_atual
- onde_paramos: a arquitetura nova do sistema foi consolidada em 4 arquivos mestres permanentes (`tgm.md`, `curadoriav61.md`, `savestateF5.md`, `loadstateF9.md`) e 1 camada volatil (`docs/checkpoints/`); as pastas `docs/masters/` e `docs/checkpoints/` ja existem no repo e os 4 mestres ja foram criados com commits separados
- objetivo_ativo: tornar o sistema novo operacional de verdade com checkpoint inaugural e teste de retomada real
- status_geral: arquitetura soberana materializada no GitHub e pronta para entrar em uso

## decidido
- `TGM no github` e o mnemonic oficial do Tendoshk God Mode e funciona como comando de modo, nao como comando de acao terminal
- `curadoriav61`, `savestateF5` e `loadstateF9` sao mestres permanentes, fixos ate segunda ordem, e checkpoint e a unica camada volatil
- `loadstateF9 no github`, `curadoriav61 no github` e `savestateF5 no github` sao comandos de acao autoencerraveis
- `curadoriav61` deve preservar quase integralmente a governanca de curadoria, canonicos, destinos e parser-safe para evitar erros de destino
- o sistema novo deve operar com separacao dura entre modo soberano, curadoria, save state, load state e checkpoint

## preservacoes
- regras_ativas: respeitar os 4 mestres como constituintes permanentes do sistema; usar `docs/checkpoints/` como unica camada volatil; usar link do repo somente se enviado no chat atual; nao confundir curadoria com save/load; nao confundir TGM com comando de acao
- trava_antidispersao: nao abrir novas frentes antes de validar o fluxo real do sistema novo; o foco imediato e checkpoint inaugural seguido de teste real do `loadstateF9`
- o_que_nao_reabrir_sem_motivo_forte: nao voltar a misturar curadoria, save state, load state e modo soberano na mesma peca; nao reduzir `curadoriav61` a uma versao simplificada que perca governanca de destinos; nao trocar `TGM` por outro mnemonic; nao tratar checkpoint como ensaio inflado

## artefatos_e_fontes
- arquivos_relevantes: docs/masters/tgm.md; docs/masters/curadoriav61.md; docs/masters/savestateF5.md; docs/masters/loadstateF9.md; docs/masters/README.txt; docs/checkpoints/README.txt
- modulos_relevantes: sistema_soberano_de_modo_curadoria_save_load_checkpoint
- testes_relevantes: teste real pendente de `loadstateF9 no github` apos criacao deste checkpoint

## proximo_passo
- proximo_passo_exato: criar este checkpoint em `docs/checkpoints/` e em seguida executar `loadstateF9 no github` para validar a retomada do sistema novo a partir de um chat limpo ou continuidade controlada
- criterio_de_conclusao_do_proximo_passo: o sistema deve conseguir devolver corretamente onde paramos, o que ja foi decidido e o proximo passo exato a partir do checkpoint salvo

## retomada_curta
- onde paramos: paramos com os 4 mestres permanentes ja criados no repo e a camada de checkpoints pronta para uso
- o que ja foi decidido: TGM e comando de modo; curadoriav61, savestateF5 e loadstateF9 sao mestres fixos; checkpoint e a unica camada volatil; F9, V61 e F5 executam e fecham sozinhos
- o proximo passo exato: salvar este checkpoint inaugural e testar o `loadstateF9 no github`
