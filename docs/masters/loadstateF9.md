# loadstateF9 — Constituição Permanente de Load State e Retomada do Cérebro Tendoshk

## Natureza

A `loadstateF9` é uma peça permanente e soberana da arquitetura do Cérebro Externo Tendoshk.

Sua função é governar a retomada entre chats, a localização de checkpoints, a restauração do estado de uma linha de trabalho e a aplicação correta desse estado ao chat evocador.

Ela não existe para comentar o projeto de forma vaga.  
Ela existe para restaurar estado com integridade.

Nesta formulação canônica, a `loadstateF9` passa a depender da governança complementar de `docs/masters/continuidade_verificavel.md` sempre que a rotina exigir prova formal da continuidade antes da aplicação do estado.

## Função

A `loadstateF9` existe para definir, de forma estável:

- quando executar load state
- como localizar o repositório correto
- como localizar este arquivo mestre
- como localizar o checkpoint correto
- como restaurar o estado de uma linha
- como distinguir localização do checkpoint e aplicação do checkpoint
- como impedir falsas retomadas
- como impedir falsas aplicações do estado carregado
- como operar em modo direto ou em modo assistido sem ambiguidade
- como submeter a continuidade à validação formal antes da restauração concluída

## Separação dura

A `loadstateF9` governa somente retomada.

Ela não substitui:
- `savestateF5`
- `curadoriav61`
- checkpoint
- NPT
- `continuidade_verificavel`

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
- aplica o estado ao chat somente depois da validação formal necessária

## Relação obrigatória com CONTINUIDADE_VERIFICAVEL

Quando a rotina de retomada exigir prova formal da continuidade, a `loadstateF9` deve carregar também o mestre dependente complementar `docs/masters/continuidade_verificavel.md` antes da aplicação final do estado ao chat evocador.

### Natureza da dependência complementar

A `CONTINUIDADE_VERIFICAVEL` não substitui a `loadstateF9`.

Ela governa:
- a prova de recência
- a prova mínima da trilha
- a distinção entre checkpoint real e checkpoint apenas plausível
- a classificação do material novo do chat atual
- a autorização ou bloqueio da declaração de continuidade concluída

### Regra crítica

É proibido tratar a localização de um checkpoint como restauração concluída quando a validação formal de continuidade ainda não ocorreu.

### Regra crítica adicional

A `loadstateF9` continua sendo a peça soberana da retomada.  
A `CONTINUIDADE_VERIFICAVEL` governa a prova formal dessa retomada.  
As duas peças operam em camadas complementares, não concorrentes.

## Regra de acionamento

Existem três formas oficiais de acionamento desta peça no GitHub.

### 1. Carga direta cronológica
Comando:
`quickloadF9 no github`

### 2. Carga assistida por lista recente
Comando:
`loadstateF9 no github`

### 3. Carga assistida por filtro textual
Comando:
`loadstateF9 <string> no github`

### Regra crítica

É proibido responder load state apenas com base em memória implícita do assistente se o repositório estiver acessível.

## Modos oficiais de carga

### 1. Modo direto cronológico
Natureza:
- carga automática
- cronológica
- sem etapa intermediária de escolha de checkpoint
- usa o checkpoint válido mais recente

### 2. Modo assistido por lista recente
Natureza:
- não carrega de imediato
- lista checkpoints recentes
- delega a escolha final ao usuário

### 3. Modo assistido por filtro
Natureza:
- não carrega de imediato
- usa a string como pista de busca
- lista checkpoints compatíveis para escolha

### Regra soberana derivada

A cronologia governa a soberania no modo direto.  
A escolha consciente do usuário governa a conclusão dos modos assistidos.

## Ordem obrigatória da retomada

Toda retomada sob esta peça deve obedecer a esta ordem:

### 1. Verificar o link do repositório
Se o link não estiver no chat atual, solicitar ao usuário.

### 2. Abrir o repositório
A retomada deve operar sobre o repositório indicado no próprio chat.

### 3. Localizar este arquivo mestre
Antes de agir, o sistema deve localizar `docs/masters/loadstateF9.md`.

### 4. Identificar o modo de carga
Determinar explicitamente se a rotina em curso é:
- carga direta
- carga assistida por lista
- carga assistida por filtro

### 5. Localizar o checkpoint candidato
Fazer a busca correta conforme o modo acionado.

### 6. Acionar CONTINUIDADE_VERIFICAVEL quando necessário
Antes da aplicação final do estado, a `loadstateF9` deve submeter a continuidade à validação formal quando houver risco relevante de:
- confundir plausibilidade com recência real
- confundir afinidade temática com soberania cronológica
- misturar checkpoint localizado com contexto local vivo
- declarar continuidade concluída sem prova mínima

### 7. Só depois avaliar a aplicação contextual
A aplicação do checkpoint ao chat atual só deve ocorrer depois da prova cronológica mínima e da classificação formal do material novo do chat atual.

### 8. Restaurar o estado
Com base no checkpoint validado e na classificação contextual correta.

### 9. Entregar a resposta final
No modo direto, com:
1. onde paramos
2. o que já foi decidido
3. o próximo passo exato

Nos modos assistidos, com:
1. informação explícita de que está em modo assistido
2. lista navegável de checkpoints
3. breve descrição de cada um
4. solicitação de escolha explícita do usuário

## Regra de busca do checkpoint

A busca do checkpoint deve respeitar o modo de carga acionado.

### No modo direto cronológico
A busca deve localizar:
- checkpoints válidos em `docs/checkpoints/`
- arquivos no padrão esperado
- o checkpoint mais recente pelo timestamp do nome ou pelo melhor rastro cronológico confiável disponível

### No modo assistido por lista recente
A busca deve localizar:
- checkpoints válidos em `docs/checkpoints/`
- os mais recentes pelo timestamp do nome
- uma lista recente suficiente para escolha manual do usuário

### No modo assistido por filtro
A busca deve localizar:
- checkpoints válidos em `docs/checkpoints/`
- candidatos compatíveis com a string fornecida
- correspondência por nome, projeto, linha de trabalho, onde paramos, objetivo ativo, próximo passo e outros campos úteis

### Regra crítica

A existência de múltiplos checkpoints compatíveis não autoriza escolha silenciosa em modo assistido.

### Regra crítica adicional

A ausência de resultado semântico não é suficiente, por si só, para concluir que não existe checkpoint.

## Cláusula de busca determinística de checkpoint

A busca do checkpoint deve obedecer a uma estratégia em camadas.

### Camada 1 — localização estrutural
Procurar primeiro em:
`docs/checkpoints/`

### Camada 2 — filtro por padrão de nome
Priorizar arquivos no padrão:
`checkpoint_AAAA_MM_DD_HH_MM_<texto_rastreavel>.md`

### Camada 3 — leitura do modo de carga
Identificar qual modo foi acionado antes de escolher ou listar.

### Camada 4 — seleção de candidatos
- no modo direto: escolher o mais recente pelo melhor rastro cronológico confiável disponível
- no modo assistido por lista: listar os mais recentes
- no modo assistido por filtro: listar os mais compatíveis com a string

### Camada 5 — desempate por timestamp do nome
Se houver mais de um checkpoint igualmente compatível, ordenar do mais recente para o mais antigo.

### Camada 6 — fallback assistido
Se a busca por filtro não retornar resultado confiável, mas existirem checkpoints válidos, exibir os checkpoints recentes como fallback assistido.

### Camada 7 — ausência real
Só declarar ausência real quando:
- não houver checkpoint válido em `docs/checkpoints/`
- ou o repositório / arquivos não estiverem acessíveis
- e a busca expandida pela trilha versionada também não localizar checkpoint utilizável

## Cláusula de busca expandida por trilha versionada

Se a listagem direta de `docs/checkpoints/` não for suficiente, a `loadstateF9` não deve concluir ausência real imediatamente.

Antes disso, deve executar busca expandida pela trilha versionada do repositório.

### Regra crítica

Insuficiência de listagem não equivale a ausência real.

### Regra derivada

Quando a trilha versionada revelar de forma clara a existência de checkpoint canônico, o sistema não deve continuar afirmando ausência de checkpoint apenas porque a listagem direta falhou.

## Regra de evidência operacional suficiente

É considerada evidência operacional suficiente da existência de checkpoint canônico qualquer uma das seguintes situações:
- arquivo de checkpoint recuperado diretamente em `docs/checkpoints/`
- commit que mostre a criação explícita de `docs/checkpoints/checkpoint_*.md`
- diff de commit contendo o conteúdo integral ou substancial do checkpoint
- referência clara e verificável ao arquivo canônico de checkpoint dentro do repositório oficial
- evidência clara de checkpoint canônico em caminho estrutural equivalente, desde que o rastro seja inequívoco

## Cláusula de compatibilidade contextual pós-localização e pré-aplicação do estado

A localização correta do checkpoint não equivale, por si só, à autorização de sobreposição imediata do contexto local.

Antes de aplicar o estado restaurado ao chat evocador, a `loadstateF9` deve executar leitura do contexto já vivo naquele próprio chat.

### Regra crítica

Localizar checkpoint não é o mesmo que sobrepor o chat.

### Regra soberana derivada

A `loadstateF9` deve distinguir duas etapas diferentes:
1. localização do estado salvo
2. aplicação do estado salvo ao contexto local do chat evocador

## Objetivo da compatibilidade contextual

A compatibilidade contextual existe para impedir:
1. sobrescrita silenciosa do andamento local do chat
2. fusão indevida entre checkpoint carregado e raciocínio já vivo
3. falsa continuidade entre linhas distintas
4. apagamento do presente do chat por simples recência cronológica do checkpoint

## Classificação obrigatória de compatibilidade

Após a leitura do contexto local, a `loadstateF9` deve classificar a compatibilidade entre checkpoint e chat evocador em uma destas categorias:

### 1. Compatibilidade neutra
Aplicação direta permitida.

### 2. Compatibilidade alta
Concatenação natural permitida, com explicitação suficiente.

### 3. Compatibilidade parcial
Concatenação explicitada obrigatória.

### 4. Compatibilidade divergente
Aviso explícito de deslocamento do eixo do chat.

### Regra crítica

Checkpoint correto com aplicação incorreta continua sendo retomada defeituosa.

## Regra específica para quickloadF9

O `quickloadF9 no github` continua sendo carga direta cronológica quanto à seleção do checkpoint.

Mas essa carga direta não elimina a obrigação de:
- validar formalmente a continuidade quando necessário
- avaliar a compatibilidade contextual antes da aplicação final

### Regra crítica

O `quickloadF9` pode ser direto na escolha do checkpoint sem ser cego na aplicação do checkpoint ao chat atual.

## Regra específica para loadstateF9 assistido

Nos modos assistidos:
- listar não é restaurar
- avaliar compatibilidade não transforma listagem em carga
- a `CONTINUIDADE_VERIFICAVEL` governa a integridade da listagem apresentada quando a prova formal for necessária

## Regra de honestidade operacional

A retomada deve explicitar o modo de verificação usado.

Sempre que necessário, a resposta deve tornar explícito:
- se o repositório foi consultado
- se o checkpoint foi encontrado
- se houve busca expandida pela trilha versionada
- se a continuidade foi validada formalmente
- se a aplicação foi direta, concatenada ou realizada com aviso de deslocamento
- se houve incerteza residual

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
- classificação de compatibilidade contextual aplicada ao chat evocador

## O que não deve acontecer no load state

Durante o load state, é proibido:
- gerar checkpoint novo
- salvar arquivo novo
- fazer curadoria NPT
- ingerir no NPT
- abrir novas frentes sem necessidade
- substituir checkpoint por opinião solta
- responder genericamente
- confundir listagem assistida com restauração efetiva
- localizar checkpoint e sobrepor o contexto local sem avaliação contextual
- tratar plausibilidade como prova suficiente de recência ou continuidade

## Critério de falsa retomada

Não considerar a retomada suficiente quando:
- não houve consulta ao repositório mesmo com repo acessível
- o checkpoint correto não foi identificado
- não foram exploradas as trilhas versionadas quando a listagem direta foi insuficiente
- a continuidade foi assumida por coerência aparente
- o próximo passo exato não foi devolvido
- o sistema caiu em resumo genérico

## Critério de falsa aplicação

Não considerar a aplicação do estado como correta quando:
- o checkpoint foi localizado, mas o chat local não foi lido
- o checkpoint foi tratado como soberano sem avaliação do contexto já vivo
- o sistema apagou implicitamente um andamento local relevante
- houve deslocamento do eixo do chat sem aviso explícito
- a validação final se apoiou apenas em busca genérica quando havia caminho ou trilha verificável

## Relação com CONTINUIDADE_VERIFICAVEL

A `loadstateF9` não substitui `CONTINUIDADE_VERIFICAVEL`.

A `loadstateF9` governa a retomada.  
A `CONTINUIDADE_VERIFICAVEL` governa a prova formal dessa retomada.

### Regra derivada

A restauração só deve ser tratada como plenamente concluída quando a prova formal necessária tiver ocorrido.

## Relação com o checkpoint

A `loadstateF9` depende do checkpoint como fonte volátil principal.

A relação correta é:
- `savestateF5` gera checkpoint
- checkpoint registra estado de linha
- `loadstateF9` lê checkpoint e restaura estado

## Relação com o repositório

O repositório GitHub é a trilha versionada de consulta entre chats.

Quando o usuário disser `quickloadF9 no github`, `loadstateF9 no github` ou `loadstateF9 <string> no github`, o sistema deve:
- usar o repositório informado no próprio chat
- localizar `docs/masters/loadstateF9.md`
- buscar checkpoint em `docs/checkpoints/`
- complementar a busca pela trilha versionada quando necessário
- validar formalmente a continuidade quando a rotina exigir prova antes da aplicação

### Regra crítica

Em chat novo, o link do repositório não deve ser presumido se não tiver sido enviado no próprio chat.

## Estrutura da resposta obrigatória

### No modo direto cronológico
A resposta deve conter:
1. onde paramos
2. o que já foi decidido
3. o próximo passo exato

E pode mencionar, quando necessário para honestidade operacional:
- o modo de verificação usado
- se houve validação formal da continuidade
- a classificação contextual
- se a aplicação foi direta, concatenada ou com aviso de deslocamento

### Nos modos assistidos
A resposta deve conter:
1. explicitação do modo assistido
2. lista útil dos checkpoints
3. breve descrição de cada um
4. pedido de escolha explícita do usuário

## Critério de sucesso do load state

Um load state é considerado bem-sucedido quando:
- o repositório foi corretamente identificado
- esta peça foi lida
- o checkpoint correto foi localizado
- a continuidade foi formalmente validada quando necessário
- a compatibilidade contextual foi avaliada
- a linha dominante foi restaurada sem falsa aplicação
- a resposta final trouxe:
  - onde paramos
  - o que já foi decidido
  - o próximo passo exato

## Fórmula canônica da correção

A `loadstateF9` deve localizar checkpoints pela pasta canônica `docs/checkpoints/`, complementar a busca pela trilha versionada do repositório quando a listagem direta for insuficiente e submeter a continuidade à governança complementar de `docs/masters/continuidade_verificavel.md` sempre que a rotina exigir prova formal antes da aplicação final do estado ao chat.

Além disso, a `loadstateF9` deve distinguir localização do checkpoint e aplicação do checkpoint. O estado salvo encontrado não deve sobrepor silenciosamente uma linha de raciocínio já viva no chat atual.

## Regra final

A `loadstateF9` existe para impedir que retomada dependa de:
- memória implícita
- reconstrução manual excessiva
- reexplicação repetida
- resumo genérico
- improviso
- plausibilidade em vez de prova
- fusão indevida entre checkpoint e contexto local
- sobrescrita silenciosa do andamento do chat evocador

Ela existe para transformar um novo chat em:
- continuidade
- reposicionamento
- recuperação fiel do ponto da linha
- retomada operacional confiável
- navegação consciente entre checkpoints quando houver múltiplas frentes
- aplicação correta do estado salvo ao contexto real do chat em que foi evocado

Não responder como resumidor.  
Não responder como se todo checkpoint plausível pudesse governar automaticamente qualquer chat.  
Responder como sistema de load state estrutural do Cérebro Tendoshk, com rigor versionado, continuidade verificável, compatibilidade contextual soberana e honestidade operacional.
