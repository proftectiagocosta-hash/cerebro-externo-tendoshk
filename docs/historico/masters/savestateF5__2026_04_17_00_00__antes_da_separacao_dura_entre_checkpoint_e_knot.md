# savestateF5 — Constituição Permanente de Save State e Geração de Checkpoints do Cérebro Tendoshk

## Natureza
A `savestateF5` é uma peça permanente e soberana da arquitetura do Cérebro Tendoshk. Sua função é governar o processo de leitura estrutural do chat para fins de salvamento de estado, geração de checkpoint rastreável, preservação do ponto real da linha de trabalho, continuidade entre sessões e chats, redução de reconstrução manual e proteção contra dispersão e perda de contexto estrutural. Esta peça só deve ser alterada por decisão explícita do usuário.

## Função
A `savestateF5` existe para definir, de forma estável: quando executar save state; como analisar o chat para salvar o estado certo; o que deve entrar no checkpoint; o que não deve entrar no checkpoint; como nomear checkpoint; onde salvar checkpoint; como preservar estado estrutural e não apenas resumo superficial; e como manter continuidade confiável entre chats.

## Separação dura
A `savestateF5` governa somente save state. Ela não substitui `curadoriav61`, `loadstateF9`, checkpoint, NPT, curadoria ou ingestão. Ela não faz curadoria estrutural, não gera `[NPT_ENTRY]`, não gera `[CHAT_INDEX]`, não faz load state e não substitui o checkpoint. Ela apenas governa como o checkpoint volátil deve ser criado.

## Regra de acionamento
Quando o usuário disser `savestateF5 no github`, o procedimento correto é: verificar se o link do GitHub já foi informado no chat atual; se não foi, solicitar ao usuário; se foi, abrir o repositório; localizar este arquivo mestre; aplicar suas regras ao chat inteiro; gerar um novo checkpoint volátil; salvar esse checkpoint no GitHub; e deixar a autorização final da plataforma concluir a escrita. É proibido gerar checkpoint só com base na última mensagem. O save state deve considerar o chat inteiro e o ponto estrutural dominante da linha.

## Objetivo do save state
O objetivo do save state é preservar, de forma rastreável e segura: onde a linha realmente está; o que já foi decidido; o que não deve ser perdido; o que não deve ser reaberto sem motivo forte; o próximo passo exato; as travas anti-dispersão; os artefatos relevantes do momento; e o estado útil para retomada em chat novo ou no mesmo chat. Save state não é resumo bonito. Save state é estado operacional de continuidade.

## O que o save state deve capturar
Todo checkpoint gerado sob esta peça deve tentar preservar, no mínimo:

### Meta
- projeto
- linha de trabalho
- repositório
- branch
- commit de referência, quando disponível
- data/hora

### Estado atual
- onde paramos
- objetivo ativo
- status geral da linha

### Decisões já tomadas
- decisões reais já consolidadas
- regras já definidas
- exclusões já decididas
- limites já aceitos

### Preservações
- regras ativas
- trava anti-dispersão
- o que não deve ser reaberto sem motivo forte

### Artefatos e fontes relevantes
- arquivos relevantes
- módulos relevantes
- testes relevantes
- fontes relevantes da linha

### Próximo passo
- próximo passo exato
- critério de conclusão do próximo passo

### Retomada curta
- onde paramos
- o que já foi decidido
- o próximo passo exato

## O que não deve entrar no checkpoint
O checkpoint não deve virar dumping de conversa. Evitar incluir: emoção circunstancial sem impacto estrutural; conversa casual; repetição de contexto já embutido no repositório; reflexão aberta sem consequência prática; redundância de regras permanentes já contidas nos arquivos mestres; comentário genérico; verborragia jurídica desnecessária; e múltiplas hipóteses ainda não decididas como se fossem decisões. O checkpoint deve ser enxuto, mas suficiente. Nem raso, nem inflado.

## Regra de foco estrutural
O save state deve buscar o eixo dominante da linha de trabalho. Se o chat tocar muitos assuntos, o checkpoint deve priorizar: o núcleo da utilidade futura; a continuidade dominante; o que realmente precisa ser preservado para retomada; e o que evita perda de estado. O checkpoint não deve tentar salvar tudo. Ele deve salvar o que sustenta a continuidade correta.

## Regra de decisão
No checkpoint, só registrar como decisão aquilo que já estiver explicitamente aceito, operacionalmente assumido, tecnicamente consolidado ou claramente adotado no fluxo do chat. Não registrar como decisão hipótese, intenção vaga, possibilidade futura ou ideia não fechada.

## Regra de trava anti-dispersão
Todo checkpoint deve registrar a trava anti-dispersão vigente da linha, quando houver. A trava anti-dispersão existe para impedir que o próximo chat reabra fundamentos já estabilizados sem motivo forte, desvie para frentes paralelas cedo demais, perca o eixo da linha ou troque continuidade concreta por expansão prematura. Se houver trava anti-dispersão clara, ela deve ser explicitada.

## Regra do “não reabrir sem motivo forte”
Todo checkpoint deve explicitar, quando couber: `o_que_nao_reabrir_sem_motivo_forte`. Isso serve para preservar decisões já consolidadas, separações de camada, limites do sistema, escolhas arquiteturais provisoriamente estáveis e exclusões deliberadas.

## Regra de naming do checkpoint
Os checkpoints devem ser salvos em `docs/checkpoints/`.

### Padrão obrigatório de nome
`checkpoint_AAAA_MM_DD_HH_MM_<texto_rastreavel>.md`

### Regra estrutural do padrão
O timestamp vem antes do texto rastreável para alinhar a ordenação alfabética do GitHub com a ordenação cronológica dos checkpoints.

### Regras para `<texto_rastreavel>`
- curto
- claro
- funcional
- ligado ao núcleo da linha
- sem caracteres problemáticos
- preferencialmente em minúsculas
- usar underscore no lugar de espaço

### Exemplo
`checkpoint_2026_04_13_21_42_nptprep_testes_cerebro_externo.md`

## Regra de conteúdo do checkpoint
Todo checkpoint gerado sob esta peça deve obedecer à seguinte estrutura base:

# Checkpoint — <texto_rastreavel>

## meta
- projeto:
- linha_de_trabalho:
- repo:
- branch:
- commit_referencia:
- data_hora:

## estado_atual
- onde_paramos:
- objetivo_ativo:
- status_geral:

## decidido
- 
- 
- 

## preservacoes
- regras_ativas:
- trava_antidispersao:
- o_que_nao_reabrir_sem_motivo_forte:

## artefatos_e_fontes
- arquivos_relevantes:
- modulos_relevantes:
- testes_relevantes:

## proximo_passo
- proximo_passo_exato:
- criterio_de_conclusao_do_proximo_passo:

## retomada_curta
- onde paramos:
- o que ja foi decidido:
- o proximo passo exato:

## Regra de commit de referência
Sempre que possível, o checkpoint deve registrar branch atual e commit de referência relevante. Se isso não estiver acessível, isso deve ser deixado explícito, sem fingir precisão. Não inventar commit, branch ou estado do repo.

## Regra de consulta ao repositório
Quando o save state for acionado no GitHub, o sistema deve abrir este arquivo mestre, analisar o chat e usar o repositório como local de salvamento do checkpoint. O save state não depende de memória implícita do assistente. Ele depende da leitura do chat atual, da consulta ao arquivo mestre e da escrita do checkpoint no repositório correto.

## Relação com load state
A `savestateF5` não faz load. A relação correta é: `savestateF5` gera novo checkpoint; `loadstateF9` busca checkpoint e restaura estado. Save state e load state são camadas diferentes.

## Relação com curadoria
A `savestateF5` não faz curadoria. Isso significa: não decidir incorporação NPT, não decidir indexação NPT e não gerar blocos de ingestão como efeito automático do save state. Um chat pode merecer checkpoint e não merecer curadoria. Um chat pode merecer curadoria e não precisar de save state forte. As camadas são independentes.

## Critério de save state insuficiente
Um save state é insuficiente quando: só resume superficialmente a conversa; não diz onde paramos; não registra decisões reais; não registra próximo passo exato; não registra trava anti-dispersão quando ela existe; não preserva o eixo dominante da linha; mistura hipótese com decisão; ou fica inflado a ponto de dificultar carga rápida futura.

## Estrutura obrigatória da resposta operacional do save state
Quando acionado, o sistema deve produzir, antes do salvamento: leitura do que precisa ser preservado; eixo dominante da linha; decisões consolidadas; próximo passo exato; nome sugerido do checkpoint; e conteúdo do checkpoint pronto para salvar. Depois disso, salvar no GitHub, se autorizado pela plataforma.

## Microcláusula de natureza e conclusão dos comandos
Os mnemônicos do sistema se dividem em duas classes.

### 1. Comando de modo
- `TGM no github`
- `tgm no github`

Natureza:
- ativa um regime soberano de operação
- não executa uma tarefa terminal por si só
- permanece ativo no chat até segunda ordem
- não exige comando de fechamento para concluir sua ativação

### 2. Comandos de ação autoencerráveis
- `loadstateF9 no github`
- `curadoriav61 no github`
- `savestateF5 no github`

Natureza:
- iniciam sua rotina completa ao serem evocados
- executam a ação correspondente
- entregam o resultado final da ação
- encerram automaticamente ao fim da entrega
- não exigem comando adicional de fechamento

### Regra soberana derivada
- `TGM` altera o regime do chat
- `loadstateF9`, `curadoriav61` e `savestateF5` executam e fecham sozinhos

### Regra crítica
É proibido confundir comando de modo com comando de ação.

## Cláusula de estabilidade
Esta peça deve ser tratada como permanente, até segunda ordem. Ela só deve ser alterada por decisão explícita do usuário. Mudanças de linha, fase ou chat não justificam alteração automática desta peça.

## Regra final
A `savestateF5` existe para impedir que continuidade dependa de memória difusa, reexplicação manual, resumo genérico ou improviso. Ela existe para transformar o final de um chat em estado rastreável, checkpoint seguro, ponto real de retomada e continuidade operacional confiável. Não responder como resumidor. Responder como sistema de save state estrutural do Cérebro Tendoshk.
