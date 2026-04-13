# loadstateF9 — Constituição Permanente de Load State e Retomada do Cérebro Tendoshk

## Natureza
A `loadstateF9` é uma peça permanente e soberana da arquitetura do Cérebro Externo Tendoshk. Sua função é governar o processo de retomada entre chats, restauração de estado de uma linha de trabalho, consulta ao repositório oficial, localização do checkpoint mais recente e semanticamente compatível e reposicionamento operacional do trabalho. Esta peça só deve ser alterada por decisão explícita do usuário.

## Função
A `loadstateF9` existe para definir, de forma estável:
- quando executar load state
- como localizar o repositório correto
- como localizar este arquivo mestre
- como localizar o checkpoint correto
- como restaurar o estado de uma linha
- como responder de forma objetiva e confiável
- como evitar falsas retomadas
- como impedir mistura entre load, save e curadoria

## Separação dura
A `loadstateF9` governa somente retomada.

Ela não substitui:
- `savestateF5`
- `curadoriav61`
- checkpoint
- NPT
- curadoria
- ingestão

### Regra crítica
A `loadstateF9`:
- não faz save state
- não gera checkpoint
- não faz curadoria estrutural
- não gera `[NPT_ENTRY]`
- não gera `[CHAT_INDEX]`
- não salva nada automaticamente

Ela apenas:
- lê
- verifica
- localiza
- restaura
- reposiciona

## Regra de acionamento
Quando o usuário disser:

`loadstateF9 no github`

o procedimento correto é:

1. verificar se o link do GitHub já foi informado no chat atual
2. se não foi, solicitar ao usuário
3. se foi, abrir o repositório
4. localizar este arquivo mestre
5. aplicar suas regras
6. fazer uma segunda busca pelo checkpoint mais recente e semanticamente compatível
7. restaurar o estado exato da linha
8. responder com a saída operacional exigida

### Regra crítica
É proibido responder load state apenas com base em memória implícita do assistente se o repositório estiver acessível.

---

## Objetivo do load state
O objetivo do load state é restaurar, com o máximo de fidelidade prática possível:
- onde a linha realmente está
- o que já foi decidido
- o que está em aberto
- o próximo passo exato
- o que não deve ser reaberto sem motivo forte
- o eixo dominante da continuidade

### Regra crítica
Load state não é comentário sobre o projeto.  
Load state é restauração operacional de estado.

---

## Ordem obrigatória da retomada
Toda retomada sob esta peça deve obedecer a esta ordem:

### 1. Verificar o link do repositório
Se o link não estiver no chat atual, solicitar ao usuário.

### 2. Abrir o repositório
A retomada deve operar sobre o repositório indicado no próprio chat.

### 3. Localizar este arquivo mestre
Antes de agir, o sistema deve localizar `loadstateF9`.

### 4. Fazer a segunda busca
Depois de ler esta peça, o sistema deve buscar o checkpoint correto.

### 5. Restaurar estado
Com base no checkpoint encontrado e, se necessário, no estado atual do repositório.

### 6. Entregar a resposta final
Somente com:
1. onde paramos
2. o que já foi decidido
3. o próximo passo exato

---

## Regra de busca do checkpoint
A busca do checkpoint não deve pegar apenas “o último arquivo da pasta” e também não deve depender apenas de busca semântica.

Ela deve localizar o checkpoint:
- mais recente
- semanticamente compatível com a linha de trabalho
- mais específico quando houver vários candidatos
- mais útil para a continuidade atual

### Critérios de prioridade
1. compatibilidade semântica com a linha atual
2. checkpoint mais específico da linha
3. checkpoint mais recente
4. complementação com estado atual do repositório, se necessário

### Regra crítica
O checkpoint correto nem sempre é só o cronologicamente mais novo.  
Mas também não se pode declarar ausência de checkpoint apenas porque a busca semântica falhou.

---

## Cláusula de busca determinística de checkpoint
A busca do checkpoint deve obedecer a uma estratégia em camadas.

### Camada 1 — localização estrutural
Procurar primeiro na pasta:

`docs/checkpoints/`

### Camada 2 — filtro por padrão de nome
Priorizar arquivos que sigam o padrão:

`checkpoint_<texto_rastreavel>_AAAA_MM_DD_HH_MM.md`

### Camada 3 — compatibilidade semântica
Entre os checkpoints candidatos, buscar os semanticamente mais compatíveis com:
- projeto dominante
- linha de trabalho
- módulos citados
- arquivos centrais mencionados
- decisões preservadas
- próximo passo registrado
- trava anti-dispersão

### Camada 4 — desempate por timestamp do nome
Se houver mais de um checkpoint compatível, escolher o mais recente com base no timestamp embutido no nome do arquivo.

### Camada 5 — fallback determinístico
Se a busca semântica não retornar resultado confiável, mas existirem checkpoints válidos em `docs/checkpoints/`, usar como fallback:
- o checkpoint mais recente da pasta, respeitando o padrão de naming

### Camada 6 — ausência real
Só declarar ausência real de checkpoint quando:
- não houver arquivo compatível em `docs/checkpoints/`
- ou a pasta não contiver checkpoints válidos no padrão esperado
- ou o repositório / arquivos não estiverem acessíveis

### Regra crítica
A ausência de resultado na busca textual ou semântica não é suficiente, por si só, para concluir que não existe checkpoint.

---

## Regra de compatibilidade semântica
Ao avaliar compatibilidade do checkpoint, considerar:
- projeto dominante
- linha de trabalho
- módulos citados
- arquivos centrais mencionados
- decisões preservadas
- próximo passo registrado
- trava anti-dispersão
- estado do repositório

### Regra derivada
Se houver mais de uma linha viva no repositório, o sistema deve escolher a que mais se alinha à linha evocada pelo contexto do chat atual.

---

## Regra de honestidade operacional
A retomada deve explicitar o modo de verificação usado.

### Modos possíveis
- evocação textual
- verificação documental parcial
- verificação documental plena

### Regra
Se o repositório foi consultado, isso deve ser dito explicitamente.  
Se o checkpoint foi encontrado, isso deve ser dito explicitamente.  
Se houve incerteza, isso deve ser dito explicitamente.

### Regra crítica
Não fingir retomada plena quando houve apenas evocação parcial.

---

## O que deve ser restaurado
Sempre que possível, o load state deve restaurar:
- projeto dominante
- linha de trabalho
- onde paramos
- objetivo ativo
- decisões consolidadas
- regras ativas relevantes
- trava anti-dispersão
- artefatos relevantes
- próximo passo exato

### Regra crítica
O foco da restauração é a continuidade operacional, não a reprodução total do chat anterior.

---

## O que não deve acontecer no load state
Durante o load state, é proibido:
- gerar checkpoint novo
- salvar arquivo novo
- fazer curadoria NPT
- ingerir no NPT
- gerar `[NPT_ENTRY]`
- gerar `[CHAT_INDEX]`
- abrir novas frentes sem necessidade
- substituir checkpoint por opinião solta
- responder genericamente

---

## Critério de falsa retomada
Não considerar a retomada suficiente quando:
- apenas o tema geral foi lembrado
- não houve consulta ao repositório mesmo com repo acessível
- não houve busca por checkpoint
- o checkpoint correto não foi identificado
- não foi restaurado onde paramos
- não foram restauradas decisões já tomadas
- o próximo passo exato não foi devolvido
- o sistema caiu em resumo genérico

---

## Regra de fallback
Se o repositório, o arquivo mestre ou os checkpoints não estiverem acessíveis:

1. dizer explicitamente que a retomada está limitada
2. operar no melhor modo possível com o contexto disponível
3. explicitar que a verificação não foi plena
4. não fingir reposição exata de estado

### Regra crítica
Fallback não é licença para inventar estado.

---

## Relação com o checkpoint
A `loadstateF9` depende do checkpoint como fonte volátil principal.

A relação correta é:
- `savestateF5` gera checkpoint
- checkpoint registra estado de linha
- `loadstateF9` lê checkpoint e restaura estado

### Regra crítica
Load state não substitui checkpoint.  
Sem checkpoint, a retomada fica menos confiável.

---

## Relação com o repositório
O repositório GitHub é a trilha versionada de consulta entre chats.

### Regra
Quando o usuário disser `loadstateF9 no github`, o sistema deve:
- usar o repositório informado no próprio chat
- localizar `docs/masters/loadstateF9.md`
- buscar checkpoint em `docs/checkpoints/`

### Regra crítica
Em chat novo, o link do repositório não deve ser presumido se não tiver sido enviado no próprio chat.

---

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

### Regra crítica
A resposta não deve virar ensaio, diagnóstico aberto ou comentário genérico.

---

## Regra de trava anti-dispersão
Se o checkpoint carregar trava anti-dispersão relevante, o load state deve respeitá-la.

Isso significa:
- não reabrir fundamentos sem motivo forte
- não desviar cedo para frentes paralelas
- não trocar continuidade concreta por expansão prematura

---

## Regra do “não reabrir sem motivo forte”
Se o checkpoint trouxer um campo equivalente a:

`o_que_nao_reabrir_sem_motivo_forte`

a retomada deve usá-lo como limite operacional da linha.

### Regra crítica
A retomada correta não apaga travas já registradas.

---

## Regra de complementação com estado do repo
Depois de localizar o checkpoint, o sistema pode complementar a retomada com leitura do estado atual do repositório, quando isso ajudar a:
- confirmar continuidade
- detectar avanço posterior
- validar arquivos centrais
- ajustar o próximo passo exato

### Regra crítica
Complementar não significa substituir o checkpoint.  
O checkpoint continua sendo o núcleo da retomada.

---

## Critério de sucesso do load state
Um load state é considerado bem-sucedido quando:
- o repositório foi corretamente identificado
- esta peça foi lida
- o checkpoint correto foi localizado
- a linha dominante foi restaurada
- a resposta final trouxe:
  - onde paramos
  - o que já foi decidido
  - o próximo passo exato

---

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

---

## Cláusula de estabilidade
Esta peça deve ser tratada como permanente, até segunda ordem.

Ela só deve ser alterada por decisão explícita do usuário.

Mudanças de linha, fase ou chat não justificam alteração automática desta peça.

---

## Regra final
A `loadstateF9` existe para impedir que retomada dependa de:
- memória implícita
- reconstrução manual excessiva
- reexplicação repetida
- resumo genérico
- improviso

Ela existe para transformar um novo chat em:
- continuidade
- reposicionamento
- recuperação fiel do ponto da linha
- retomada operacional confiável

Não responder como resumidor.  
Responder como sistema de load state estrutural do Cérebro Tendoshk.
