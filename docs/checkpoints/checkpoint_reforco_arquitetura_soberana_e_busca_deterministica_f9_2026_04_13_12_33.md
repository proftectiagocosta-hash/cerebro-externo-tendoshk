# Checkpoint — reforco_arquitetura_soberana_e_busca_deterministica_f9

## meta
- projeto: NPT_NUCLEO_PERSISTENTE_TENDOSHK
- linha_de_trabalho: consolidacao_da_arquitetura_soberana_do_cerebro_tendoshk_com_reforco_da_logica_de_busca_deterministica_do_loadstate
- repo: proftectiagocosta-hash/cerebro-externo-tendoshk
- branch: main
- commit_referencia: nao_verificado_nesta_sessao
- data_hora: 2026-04-13 12:33 UTC-04

## estado_atual
- onde_paramos: os 4 arquivos mestres permanentes ja foram criados no repositorio (`tgm.md`, `curadoriav61.md`, `savestateF5.md`, `loadstateF9.md`), a pasta `docs/checkpoints/` ja existe e o sistema foi reforcado conceitualmente com uma nova versao correta do `loadstateF9`, agora contendo busca deterministica de checkpoint em camadas
- objetivo_ativo: tornar o ciclo TGM + F5 + F9 + V61 realmente operacional e confiavel entre chats
- status_geral: arquitetura soberana consolidada; falta validar o fluxo real com checkpoint salvo e retomada executada sobre ele

## decidido
- `TGM no github` e o mnemonic oficial do Tendoshk God Mode e funciona como comando de modo
- `curadoriav61`, `savestateF5` e `loadstateF9` sao mestres permanentes e checkpoint e a unica camada volatil
- `loadstateF9 no github`, `curadoriav61 no github` e `savestateF5 no github` sao comandos de acao autoencerraveis
- o sistema deve distinguir regras permanentes de estado volatil do chat
- `curadoriav61` nao deve ser simplificado a ponto de perder governanca de canonicos, destinos e parser-safe
- o `loadstateF9` precisava de reforco porque a regra antiga dizia o que buscar, mas nao amarrava suficientemente o metodo mecanico de recuperar um checkpoint existente
- a nova regra correta do `loadstateF9` agora exige busca deterministica por `docs/checkpoints/`, prefixo `checkpoint_`, desempate por timestamp do nome e fallback para o checkpoint mais recente da pasta antes de declarar ausencia real

## preservacoes
- regras_ativas: respeitar os 4 mestres como constituintes permanentes do sistema; usar `docs/checkpoints/` como unica camada volatil; exigir link do repo no proprio chat antes de operar; manter separacao dura entre modo soberano, curadoria, save state, load state e checkpoint
- trava_antidispersao: nao abrir novas frentes antes de validar o ciclo real do sistema novo com checkpoint salvo e `loadstateF9` corrigido; o foco imediato e consolidar a confiabilidade de save/load
- o_que_nao_reabrir_sem_motivo_forte: nao voltar a misturar curadoria com save/load; nao reduzir o `curadoriav61` a uma versao fraca; nao trocar o mnemonic `TGM`; nao depender apenas de busca semantica para localizar checkpoint; nao declarar ausencia de checkpoint sem antes aplicar busca deterministica em camadas

## artefatos_e_fontes
- arquivos_relevantes: docs/masters/tgm.md; docs/masters/curadoriav61.md; docs/masters/savestateF5.md; docs/masters/loadstateF9.md; docs/masters/README.txt; docs/checkpoints/README.txt
- modulos_relevantes: sistema_soberano_de_modo_curadoria_save_load_checkpoint
- testes_relevantes: validacao funcional pendente do fluxo `loadstateF9 no github` apos salvar este checkpoint e atualizar o `loadstateF9.md` no repo

## proximo_passo
- proximo_passo_exato: salvar este checkpoint em `docs/checkpoints/`, garantir que a versao corrigida do `loadstateF9.md` esteja commitada no GitHub e em seguida executar `loadstateF9 no github` para validar a retomada pelo metodo deterministico novo
- criterio_de_conclusao_do_proximo_passo: o sistema deve conseguir localizar checkpoint real no repo e devolver corretamente onde paramos, o que ja foi decidido e o proximo passo exato sem cair em falsa ausencia de checkpoint

## retomada_curta
- onde paramos: paramos com os 4 mestres permanentes ja criados e com o `loadstateF9` conceitualmente corrigido para busca deterministica de checkpoint
- o que ja foi decidido: TGM e comando de modo; F9, V61 e F5 sao acoes autoencerraveis; checkpoint e a unica camada volatil; `curadoriav61` deve manter governanca forte; `loadstateF9` agora precisa buscar checkpoint por estrutura + prefixo + timestamp + semantica
- o proximo passo exato: salvar este checkpoint, commitar a versao corrigida do `loadstateF9.md` e testar `loadstateF9 no github`
