# loadstateF9 — Constituição Permanente de Load State e Retomada do Cérebro Tendoshk

## Natureza
A `loadstateF9` é uma peça permanente e soberana da arquitetura do Cérebro Externo Tendoshk. Sua função é governar o processo de retomada entre chats, restauração de estado de uma linha de trabalho, consulta ao repositório oficial, localização do checkpoint mais recente e semanticamente compatível e reposicionamento operacional do trabalho. Esta peça só deve ser alterada por decisão explícita do usuário.

## Função
A `loadstateF9` existe para definir, de forma estável: quando executar load state; como localizar o repositório correto; como localizar este arquivo mestre; como localizar o checkpoint correto; como restaurar o estado de uma linha; como responder de forma objetiva e confiável; como evitar falsas retomadas; e como impedir mistura entre load, save e curadoria.

## Separação dura
A `loadstateF9` governa somente retomada. Ela não substitui `savestateF5`, `curadoriav61`, checkpoint, NPT, curadoria ou ingestão. Ela não faz save state, não gera checkpoint, não faz curadoria estrutural, não gera `[NPT_ENTRY]`, não gera `[CHAT_INDEX]` e não salva nada automaticamente. Ela apenas lê, verifica, localiza, restaura e reposiciona.

## Regra de acionamento
Quando o usuário disser `loadstateF9 no github`, o procedimento correto é: verificar se o link do GitHub já foi informado no chat atual; se não foi, solicitar ao usuário; se foi, abrir o repositório; localizar este arquivo mestre; aplicar suas regras; fazer uma segunda busca pelo checkpoint mais recente e semanticamente compatível; restaurar o estado exato da linha; e responder com a saída operacional exigida. É proibido responder load state apenas com base em memória implícita do assistente se o repositório estiver acessível.

## Objetivo do load state
O objetivo do load state é restaurar, com o máximo de fidelidade prática possível: onde a linha realmente está; o que já foi decidido; o que está em aberto; o próximo passo exato; o que não deve ser reaberto sem motivo forte; e o eixo dominante da continuidade. Load state não é comentário sobre o projeto. Load state é restauração operacional de estado.

## Ordem obrigatória da retomada
Toda retomada sob esta peça deve obedecer a esta ordem:
1. verificar o link do repositório; se o link não estiver no chat atual, solicitar ao usuário
2. abrir o repositório
3. localizar este arquivo mestre
4. fazer a segunda busca
5. restaurar estado
6. entregar a resposta final

## Regra de busca do checkpoint
A busca do checkpoint não deve pegar apenas o último arquivo da pasta. Ela deve buscar o checkpoint mais recente, semanticamente compatível com a linha de trabalho, mais específico quando houver vários candidatos e mais útil para a continuidade atual.

### Critérios de prioridade
1. compatibilidade semântica com a linha atual
2. checkpoint mais específico da linha
3. checkpoint mais recente
4. complementação com estado atual do repositório, se necessário

### Regra crítica
O checkpoint correto nem sempre é só o cronologicamente mais novo.

## Regra de compatibilidade semântica
Ao avaliar compatibilidade do checkpoint, considerar: projeto dominante, linha de trabalho, módulos citados, arquivos centrais mencionados, decisões preservadas, próximo passo registrado, trava anti-dispersão e estado do repositório. Se houver mais de uma linha viva no repositório, o sistema deve escolher a que mais se alinha à linha evocada pelo contexto do chat atual.

## Regra de honestidade operacional
A retomada deve explicitar o modo de verificação usado.

### Modos possíveis
- evocação textual
- verificação documental parcial
- verificação documental plena

### Regra
Se o repositório foi consultado, isso deve ser dito explicitamente. Se o checkpoint foi encontrado, isso deve ser dito explicitamente. Se houve incerteza, isso deve ser dito explicitamente. Não fingir retomada plena quando houve apenas evocação parcial.

## O que deve ser restaurado
Sempre que possível, o load state deve restaurar: projeto dominante, linha de trabalho, onde paramos, objetivo ativo, decisões consolidadas, regras ativas relevantes, trava anti-dispersão, artefatos relevantes e próximo passo exato. O foco da restauração é a continuidade operacional, não a reprodução total do chat anterior.

## O que não deve acontecer no load state
Durante o load state, é proibido: gerar checkpoint novo, salvar arquivo novo, fazer curadoria NPT, ingerir no NPT, gerar `[NPT_ENTRY]`, gerar `[CHAT_INDEX]`, abrir novas frentes sem necessidade, substituir checkpoint por opinião solta ou responder genericamente.

## Critério de falsa retomada
Não considerar a retomada suficiente quando: apenas o tema geral foi lembrado; não houve consulta ao repositório mesmo com repo acessível; não houve busca por checkpoint; o checkpoint correto não foi identificado; não foi restaurado onde paramos; não foram restauradas decisões já tomadas; o próximo passo exato não foi devolvido; ou o sistema caiu em resumo genérico.

## Regra de fallback
Se o repositório, o arquivo mestre ou os checkpoints não estiverem acessíveis: dizer explicitamente que a retomada está limitada, operar no melhor modo possível com o contexto disponível, explicitar que a verificação não foi plena e não fingir reposição exata de estado. Fallback não é licença para inventar estado.

## Relação com o checkpoint
A `loadstateF9` depende do checkpoint como fonte volátil principal. A relação correta é: `savestateF5` gera checkpoint; checkpoint registra estado de linha; `loadstateF9` lê checkpoint e restaura estado. Load state não substitui checkpoint. Sem checkpoint, a retomada fica menos confiável.

## Relação com o repositório
O repositório GitHub é a trilha versionada de consulta entre chats. Quando o usuário disser `loadstateF9 no github`, o sistema deve usar o repositório informado no próprio chat, localizar `docs/masters/loadstateF9.md` e buscar checkpoint em `docs/checkpoints/`. Em chat novo, o link do repositório não deve ser presumido se não tiver sido enviado no próprio chat.

## Estrutura da resposta obrigatória
A resposta do load state deve conter somente:

### 1. Onde paramos
Descrição objetiva do ponto estrutural exato da linha.

### 2. O que já foi decidido
Lista curta das decisões reais já consolidadas.

### 3. O próximo passo exato
Uma ação concreta, única e executável.

### Opcional, quando necessário
- incerteza encontrada
- modo de verificação usado
- se o repositório foi consultado
- qual checkpoint foi usado

A resposta não deve virar ensaio, diagnóstico aberto ou comentário genérico.

## Regra de trava anti-dispersão
Se o checkpoint carregar trava anti-dispersão relevante, o load state deve respeitá-la. Isso significa: não reabrir fundamentos sem motivo forte, não desviar cedo para frentes paralelas e não trocar continuidade concreta por expansão prematura.

## Regra do “não reabrir sem motivo forte”
Se o checkpoint trouxer um campo equivalente a `o_que_nao_reabrir_sem_motivo_forte`, a retomada deve usá-lo como limite operacional da linha. A retomada correta não apaga travas já registradas.

## Regra de complementação com estado do repo
Depois de localizar o checkpoint, o sistema pode complementar a retomada com leitura do estado atual do repositório, quando isso ajudar a confirmar continuidade, detectar avanço posterior, validar arquivos centrais ou ajustar o próximo passo exato. Complementar não significa substituir o checkpoint. O checkpoint continua sendo o núcleo da retomada.

## Critério de sucesso do load state
Um load state é considerado bem-sucedido quando: o repositório foi corretamente identificado; esta peça foi lida; o checkpoint correto foi localizado; a linha dominante foi restaurada; e a resposta final trouxe onde paramos, o que já foi decidido e o próximo passo exato.

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
A `loadstateF9` existe para impedir que retomada dependa de memória implícita, reconstrução manual excessiva, reexplicação repetida, resumo genérico ou improviso. Ela existe para transformar um novo chat em continuidade, reposicionamento, recuperação fiel do ponto da linha e retomada operacional confiável. Não responder como resumidor. Responder como sistema de load state estrutural do Cérebro Tendoshk.
