# loadstateF9 — Constituição Permanente de Load State e Retomada do Cérebro Tendoshk

## Natureza
A `loadstateF9` é uma peça permanente e soberana da arquitetura do Cérebro Externo Tendoshk. Sua função é governar o processo de retomada entre chats, restauração de estado de uma linha de trabalho, consulta ao repositório oficial, localização do checkpoint mais recente ou mais compatível conforme o modo acionado e reposicionamento operacional do trabalho. Esta peça só deve ser alterada por decisão explícita do usuário.

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
- como operar em modo direto ou em modo assistido sem ambiguidade

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
- lista opções quando estiver em modo assistido

## Regra de acionamento

Existem agora três formas oficiais de acionamento desta peça no GitHub.

### 1. Carga direta cronológica
Quando o usuário disser:

`quickloadF9 no github`

o procedimento correto é:

1. verificar se o link do GitHub já foi informado no chat atual
2. se não foi, solicitar ao usuário
3. se foi, abrir o repositório
4. localizar este arquivo mestre
5. aplicar suas regras
6. localizar o checkpoint válido mais recente em `docs/checkpoints/`
7. se a listagem direta for insuficiente, executar busca expandida pela trilha versionada do repositório
8. restaurar o estado exato da linha contida nesse checkpoint
9. responder com a saída operacional exigida

### 2. Carga assistida por lista recente
Quando o usuário disser:

`loadstateF9 no github`

o procedimento correto é:

1. verificar se o link do GitHub já foi informado no chat atual
2. se não foi, solicitar ao usuário
3. se foi, abrir o repositório
4. localizar este arquivo mestre
5. aplicar suas regras
6. localizar os checkpoints válidos mais recentes em `docs/checkpoints/`
7. se a listagem direta for insuficiente, executar busca expandida pela trilha versionada do repositório
8. listar os checkpoints recentes com descrição curta para escolha do usuário
9. aguardar a seleção explícita antes de restaurar o estado

### 3. Carga assistida por filtro textual
Quando o usuário disser algo como:

`loadstateF9 <string> no github`

o procedimento correto é:

1. verificar se o link do GitHub já foi informado no chat atual
2. se não foi, solicitar ao usuário
3. se foi, abrir o repositório
4. localizar este arquivo mestre
5. aplicar suas regras
6. usar a string fornecida como pista de busca
7. localizar checkpoints semanticamente ou textualmente compatíveis
8. se a listagem direta for insuficiente, executar busca expandida pela trilha versionada do repositório
9. listar os candidatos com descrição curta para escolha do usuário
10. aguardar a seleção explícita antes de restaurar o estado

### Regra crítica
É proibido responder load state apenas com base em memória implícita do assistente se o repositório estiver acessível.

### Regra crítica adicional
`quickloadF9 no github` executa carga direta.  
`loadstateF9 no github` não deve carregar automaticamente enquanto estiver em modo assistido por lista.  
`loadstateF9 <string> no github` não deve carregar automaticamente enquanto estiver em modo assistido por filtro, salvo se o usuário deixar inequívoco que deseja o primeiro candidato compatível.

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

## Modos oficiais de carga

Esta peça passa a operar em três modos oficiais.

### 1. Modo direto cronológico
Comando:
`quickloadF9 no github`

Natureza:
- carga automática
- cronológica
- sem etapa intermediária de escolha
- usa o checkpoint válido mais recente

Uso ideal:
- quando o usuário quer simplesmente entrar no último estado salvo
- quando não deseja navegar entre múltiplas linhas
- quando o critério desejado é recência pura

### 2. Modo assistido por lista recente
Comando:
`loadstateF9 no github`

Natureza:
- não carrega de imediato
- lista checkpoints recentes
- delega a escolha final ao usuário

Uso ideal:
- quando existem várias linhas vivas
- quando o usuário quer ver as opções antes de carregar
- quando a escolha cronológica pura pode levar à linha errada

### 3. Modo assistido por filtro
Comando:
`loadstateF9 <string> no github`

Natureza:
- não carrega de imediato
- usa a string como pista de busca
- lista checkpoints compatíveis para escolha

Uso ideal:
- quando o usuário lembra de uma linha, tema, módulo ou palavra
- quando quer navegar por checkpoints semelhantes
- quando a semântica deve ajudar a encontrar a linha certa, mas não decidir sozinha

### Regra soberana derivada
A semântica continua valiosa, mas não governa sozinha toda retomada.  
No modo direto, governa a cronologia válida.  
No modo assistido, governa a navegação e a escolha consciente.

## Ordem obrigatória da retomada
Toda retomada sob esta peça deve obedecer a esta ordem:

### 1. Verificar o link do repositório
Se o link não estiver no chat atual, solicitar ao usuário.

### 2. Abrir o repositório
A retomada deve operar sobre o repositório indicado no próprio chat.

### 3. Localizar este arquivo mestre
Antes de agir, o sistema deve localizar `loadstateF9`.

### 4. Fazer a busca correta conforme o modo
Depois de ler esta peça, o sistema deve:
- localizar o checkpoint válido mais recente no modo direto
- ou localizar a lista recente no modo assistido por lista
- ou localizar checkpoints compatíveis no modo assistido por filtro

### 5. Restaurar estado
Com base no checkpoint encontrado e, se necessário, no estado atual do repositório.

### 6. Entregar a resposta final
No modo direto, somente com:
1. onde paramos
2. o que já foi decidido
3. o próximo passo exato

Nos modos assistidos, com:
1. explicitação do modo assistido
2. lista navegável de checkpoints
3. breve descrição de cada um
4. solicitação de escolha explícita do usuário

## Regra de busca do checkpoint

A busca do checkpoint deve respeitar o modo de carga acionado.

### No modo direto cronológico
Quando o comando for:

`quickloadF9 no github`

a busca deve localizar:
- checkpoints válidos em `docs/checkpoints/`
- arquivos no padrão esperado
- o checkpoint mais recente pelo timestamp embutido no nome

Neste modo, a cronologia governa a escolha final.

### No modo assistido por lista recente
Quando o comando for:

`loadstateF9 no github`

a busca deve localizar:
- checkpoints válidos em `docs/checkpoints/`
- os mais recentes pelo timestamp do nome
- uma lista recente suficiente para escolha manual do usuário

Neste modo, a cronologia governa a lista, mas não a escolha final.

### No modo assistido por filtro
Quando o comando for:

`loadstateF9 <string> no github`

a busca deve localizar:
- checkpoints válidos em `docs/checkpoints/`
- candidatos compatíveis com a string fornecida
- correspondência por nome, projeto, linha de trabalho, onde paramos, próximo passo e outros campos úteis

Neste modo, a compatibilidade ajuda a montar a lista, mas não deve substituir a escolha do usuário quando houver ambiguidade relevante.

### Regra crítica
A existência de múltiplos checkpoints compatíveis não autoriza o sistema a escolher silenciosamente em modo assistido.

### Regra crítica
A ausência de resultado semântico não é suficiente, por si só, para concluir que não existe checkpoint.

## Cláusula de busca determinística de checkpoint

A busca do checkpoint deve obedecer a uma estratégia em camadas.

### Camada 1 — localização estrutural
Procurar primeiro na pasta:

`docs/checkpoints/`

### Camada 2 — filtro por padrão de nome
Priorizar arquivos que sigam o padrão:

`checkpoint_<texto_rastreavel>_AAAA_MM_DD_HH_MM.md`

### Camada 3 — leitura do modo de carga
Antes de escolher ou listar, identificar qual modo foi acionado:
- modo direto cronológico
- modo assistido por lista recente
- modo assistido por filtro

### Camada 4 — seleção de candidatos
#### No modo direto cronológico
Selecionar checkpoints válidos e escolher o mais recente pelo timestamp do nome.

#### No modo assistido por lista recente
Selecionar os checkpoints válidos mais recentes e montar uma lista para o usuário.

#### No modo assistido por filtro
Selecionar os checkpoints mais compatíveis com a string fornecida, considerando:
- nome do arquivo
- projeto dominante
- linha de trabalho
- módulos citados
- arquivos centrais mencionados
- decisões preservadas
- próximo passo registrado
- trava anti-dispersão

### Camada 5 — desempate por timestamp do nome
Se houver mais de um checkpoint igualmente compatível no modo assistido por filtro, ordenar do mais recente para o mais antigo.

### Camada 6 — fallback determinístico
Se a busca por filtro não retornar resultado confiável, mas existirem checkpoints válidos em `docs/checkpoints/`, o sistema pode:
- informar que não encontrou compatibilidade forte
- exibir os checkpoints recentes válidos como fallback assistido

### Camada 7 — ausência real
Só declarar ausência real de checkpoint quando:
- não houver arquivo compatível em `docs/checkpoints/`
- ou a pasta não contiver checkpoints válidos no padrão esperado
- ou o repositório / arquivos não estiverem acessíveis
- e a busca expandida pela trilha versionada também não localizar checkpoint utilizável

### Regra crítica
A ausência de resultado na busca textual ou semântica não é suficiente, por si só, para concluir que não existe checkpoint.

## Cláusula de busca expandida por trilha versionada

Se a listagem direta de `docs/checkpoints/` não for suficiente para localizar, listar ou carregar checkpoints válidos, o sistema não deve concluir ausência real de checkpoint imediatamente.

Antes de declarar que não há checkpoint utilizável, deve executar uma busca expandida pela trilha versionada do repositório.

### Ordem obrigatória da busca expandida

#### Etapa 1 — tentativa canônica direta
Tentar primeiro a rotina padrão em:

`docs/checkpoints/`

Buscando:
- arquivos válidos no padrão esperado
- checkpoints recentes
- checkpoints compatíveis com o modo acionado

#### Etapa 2 — verificação de insuficiência da listagem direta
A listagem direta deve ser considerada insuficiente quando ocorrer qualquer um destes casos:
- a pasta retornar apenas arquivos auxiliares como `README`
- a listagem não expuser claramente os checkpoints existentes
- a ferramenta de consulta não devolver os arquivos esperados
- houver forte indício contextual de que checkpoints existem, mas não estejam sendo entregues de forma navegável

### Regra crítica
Insuficiência de listagem não equivale a ausência real de checkpoint.

#### Etapa 3 — busca por trilha versionada recente
Se a listagem direta for insuficiente, o sistema deve buscar na trilha versionada do repositório:
- commits recentes que adicionaram arquivos em `docs/checkpoints/`
- commits recentes cuja mensagem mencione `checkpoint`
- commits recentes que contenham diff com criação de arquivo de checkpoint
- referências explícitas a arquivos `docs/checkpoints/checkpoint_*.md`

#### Etapa 4 — recuperação do checkpoint pela trilha versionada
Se um commit recente revelar a criação ou atualização de checkpoint válido, o sistema deve tratar esse rastro como evidência operacional suficiente para:
- identificar o nome do checkpoint
- recuperar seu conteúdo
- ordenar checkpoints por recência
- restaurar ou listar checkpoints conforme o modo acionado

### Regra crítica
Quando a trilha versionada revelar de forma clara a existência de um checkpoint canônico em `docs/checkpoints/`, o sistema não deve continuar afirmando ausência de checkpoint apenas porque a listagem direta da pasta falhou.

#### Etapa 5 — aplicação por modo

### No modo direto cronológico
Comando:
`quickloadF9 no github`

Se a listagem direta falhar, mas a trilha versionada revelar checkpoints válidos, o sistema deve:
1. identificar os checkpoints canônicos encontrados pela trilha versionada
2. ordenar pela recência válida
3. selecionar o mais recente
4. restaurar o estado correspondente
5. entregar a resposta final no formato de carga direta

### No modo assistido por lista recente
Comando:
`loadstateF9 no github`

Se a listagem direta falhar, mas a trilha versionada revelar checkpoints válidos, o sistema deve:
1. identificar os checkpoints recentes disponíveis
2. ordenar pela recência válida
3. montar lista navegável com descrição curta
4. aguardar escolha explícita do usuário

### No modo assistido por filtro
Comando:
`loadstateF9 <string> no github`

Se a listagem direta falhar, mas a trilha versionada revelar checkpoints válidos, o sistema deve:
1. localizar checkpoints compatíveis pela string
2. usar nome do arquivo, linha de trabalho, projeto, onde paramos, próximo passo e campos equivalentes como base de compatibilidade
3. ordenar os candidatos
4. montar lista navegável para escolha do usuário

## Regra de evidência operacional suficiente

É considerada evidência operacional suficiente da existência de checkpoint canônico qualquer uma das seguintes situações:
- arquivo de checkpoint recuperado diretamente em `docs/checkpoints/`
- commit que mostre a criação explícita de `docs/checkpoints/checkpoint_*.md`
- diff de commit contendo o conteúdo integral ou substancial do checkpoint
- referência clara e verificável ao arquivo canônico de checkpoint dentro do repositório oficial

### Regra crítica
Se houver evidência operacional suficiente, o sistema deve operar sobre ela.
Não deve exigir, sem necessidade, que o usuário forneça manualmente hash, nome exato ou caminho completo de um checkpoint que já está rastreável no repositório.

## Regra de ausência real reforçada

Só declarar ausência real de checkpoint quando:
- a listagem direta de `docs/checkpoints/` falhar ou não trouxer checkpoints válidos
- e a busca expandida pela trilha versionada também não localizar checkpoint utilizável
- e não houver referência confiável em commits, diffs ou arquivos correlatos
- e não houver outro rastro documental suficiente no repositório oficial

### Regra crítica
Antes disso, qualquer resposta de ausência deve ser tratada apenas como:
- ausência ainda não confirmada
- ou localização ainda inconclusiva

## Regra de integridade do quickload

O `quickloadF9 no github` existe para entrar no último estado salvo válido com o mínimo de fricção operacional.

Logo:
- ele não deve depender apenas da primeira forma de listagem disponível
- ele deve insistir na localização do checkpoint pela trilha oficial do repositório
- ele só deve falhar quando a ausência real estiver suficientemente confirmada

### Regra soberana derivada
No `quickloadF9`, a cronologia soberana deve ser aplicada sobre o melhor rastro confiável disponível do checkpoint canônico, e não apenas sobre a primeira listagem estrutural da pasta.

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
Se houver mais de uma linha viva no repositório, o sistema deve escolher a que mais se alinha à linha evocada pelo contexto do chat atual apenas quando estiver em modo direto semanticamente autorizado.  
Nos modos assistidos, essa compatibilidade deve servir para montar ou ordenar a lista, não para eliminar a escolha do usuário sem necessidade.

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
Se a resposta estiver em modo assistido, isso também deve ser dito explicitamente.  
Se houve busca expandida pela trilha versionada, isso também deve ser dito explicitamente.

### Regra crítica
Não fingir retomada plena quando houve apenas evocação parcial.

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
- confundir listagem assistida com restauração efetiva

## Critério de falsa retomada
Não considerar a retomada suficiente quando:
- apenas o tema geral foi lembrado
- não houve consulta ao repositório mesmo com repo acessível
- não houve busca por checkpoint
- o checkpoint correto não foi identificado
- não foram exploradas as trilhas versionadas quando a listagem direta foi insuficiente
- não foi restaurado onde paramos
- não foram restauradas decisões já tomadas
- o próximo passo exato não foi devolvido
- o sistema caiu em resumo genérico
- o sistema listou opções, mas se comportou como se já tivesse restaurado o estado

## Regra de fallback
Se o repositório, o arquivo mestre ou os checkpoints não estiverem acessíveis:

1. dizer explicitamente que a retomada está limitada
2. operar no melhor modo possível com o contexto disponível
3. explicitar que a verificação não foi plena
4. não fingir reposição exata de estado

### Regra crítica
Fallback não é licença para inventar estado.

## Relação com o checkpoint
A `loadstateF9` depende do checkpoint como fonte volátil principal.

A relação correta é:
- `savestateF5` gera checkpoint
- checkpoint registra estado de linha
- `loadstateF9` lê checkpoint e restaura estado

### Regra crítica
Load state não substitui checkpoint.  
Sem checkpoint, a retomada fica menos confiável.

## Relação com o repositório
O repositório GitHub é a trilha versionada de consulta entre chats.

### Regra
Quando o usuário disser `quickloadF9 no github`, `loadstateF9 no github` ou `loadstateF9 <string> no github`, o sistema deve:
- usar o repositório informado no próprio chat
- localizar `docs/masters/loadstateF9.md`
- buscar checkpoint em `docs/checkpoints/`
- e, se necessário, complementar a busca pela trilha versionada do próprio repositório

### Regra crítica
Em chat novo, o link do repositório não deve ser presumido se não tiver sido enviado no próprio chat.

## Regra de listagem assistida de checkpoints

Nos modos assistidos, o sistema deve exibir checkpoints em formato navegável para escolha do usuário.

### Tamanho padrão da lista
O padrão recomendado é listar até 10 checkpoints válidos, salvo se o usuário pedir outro número.

### Cada item da lista deve trazer, sempre que possível
1. nome do checkpoint
2. data/hora inferida do nome ou do conteúdo
3. projeto ou linha de trabalho
4. descrição curta

### Regra da descrição curta
A descrição curta deve ser enxuta e útil.  
Ela deve ser extraída preferencialmente de:
- `retomada_curta`
- `onde_paramos`
- `objetivo_ativo`
- `proximo_passo_exato`

### Regra crítica
A listagem assistida não deve virar dump integral dos checkpoints.  
Ela deve servir para navegação consciente e escolha rápida.

### Regra crítica
Em modo assistido, o sistema não deve fingir que listar já equivale a restaurar.  
Listar é listar.  
Restaurar é carregar o checkpoint escolhido.

## Estrutura da resposta obrigatória

A resposta do load state depende do modo acionado.

### No modo direto cronológico
A resposta deve conter somente:

#### 1. Onde paramos
Descrição objetiva do ponto estrutural exato da linha.

#### 2. O que já foi decidido
Lista curta das decisões reais já consolidadas.

#### 3. O próximo passo exato
Uma ação concreta, única e executável.

### No modo assistido por lista recente
A resposta deve conter:
1. informação explícita de que está em modo assistido
2. lista dos checkpoints recentes
3. breve descrição de cada um
4. pedido de escolha explícita do usuário

### No modo assistido por filtro
A resposta deve conter:
1. informação explícita de que está em modo assistido por filtro
2. a string usada como pista
3. lista dos checkpoints compatíveis encontrados
4. breve descrição de cada um
5. pedido de escolha explícita do usuário

### Opcional, quando necessário
- incerteza encontrada
- modo de verificação usado
- se o repositório foi consultado
- qual checkpoint foi usado
- se houve busca expandida pela trilha versionada
- por que houve fallback

### Regra crítica
A resposta não deve virar ensaio, diagnóstico aberto ou comentário genérico.

## Regra de trava anti-dispersão
Se o checkpoint carregar trava anti-dispersão relevante, o load state deve respeitá-la.

Isso significa:
- não reabrir fundamentos sem motivo forte
- não desviar cedo para frentes paralelas
- não trocar continuidade concreta por expansão prematura

## Regra do “não reabrir sem motivo forte”
Se o checkpoint trouxer um campo equivalente a:

`o_que_nao_reabrir_sem_motivo_forte`

a retomada deve usá-lo como limite operacional da linha.

### Regra crítica
A retomada correta não apaga travas já registradas.

## Regra de complementação com estado do repo
Depois de localizar o checkpoint, o sistema pode complementar a retomada com leitura do estado atual do repositório, quando isso ajudar a:
- confirmar continuidade
- detectar avanço posterior
- validar arquivos centrais
- ajustar o próximo passo exato

### Regra crítica
Complementar não significa substituir o checkpoint.  
O checkpoint continua sendo o núcleo da retomada.

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

Nos modos assistidos, o sucesso parcial da primeira etapa consiste em:
- localizar corretamente os checkpoints válidos
- exibir a lista de forma útil
- permitir escolha consciente do usuário sem falsa restauração

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
- `quickloadF9 no github`
- `loadstateF9 no github`
- `loadstateF9 <string> no github`
- `curadoriav61 no github`
- `savestateF5 no github`

Natureza:
- iniciam sua rotina completa ao serem evocados
- executam a ação correspondente
- entregam o resultado final da ação
- encerram automaticamente ao fim da entrega, conforme sua natureza

### Regra adicional sobre a família F9
- `quickloadF9 no github` conclui a restauração ao fim da carga direta
- `loadstateF9 no github` conclui sua primeira etapa ao listar opções, e só conclui a restauração após escolha explícita do usuário
- `loadstateF9 <string> no github` conclui sua primeira etapa ao listar candidatos compatíveis, e só conclui a restauração após escolha explícita do usuário, salvo instrução inequívoca em contrário

### Regra soberana derivada
- `TGM` altera o regime do chat
- `quickloadF9`, `loadstateF9`, `curadoriav61` e `savestateF5` executam e fecham conforme a natureza de sua própria peça
- a existência de etapa assistida não altera o fato de que continuam sendo comandos de ação, e não comandos de modo

### Regra crítica
É proibido confundir comando de modo com comando de ação.

## Cláusula de estabilidade
Esta peça deve ser tratada como permanente, até segunda ordem.

Ela só deve ser alterada por decisão explícita do usuário.

Mudanças de linha, fase ou chat não justificam alteração automática desta peça.

## Formulação canônica da correção
A `loadstateF9` deve buscar checkpoints primeiro pela pasta canônica `docs/checkpoints/`, mas, se a listagem direta for insuficiente, deve obrigatoriamente recorrer à trilha versionada do repositório oficial antes de concluir ausência real de checkpoint. Em `quickloadF9`, essa busca expandida é parte do próprio dever de restaurar o último estado salvo válido sem depender de apontamento manual do usuário quando o rastro já existir no GitHub.

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
- navegação consciente entre checkpoints quando houver múltiplas frentes

Não responder como resumidor.  
Responder como sistema de load state estrutural do Cérebro Tendoshk.
