## Cláusula de busca expandida por trilha versionada

Se a listagem direta de `docs/checkpoints/` não for suficiente para localizar, listar ou carregar checkpoints válidos, o sistema **não deve concluir ausência real de checkpoint imediatamente**.

Antes de declarar que não há checkpoint utilizável, deve executar uma **busca expandida pela trilha versionada do repositório**.

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
Insuficiência de listagem **não equivale** a ausência real de checkpoint.

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
Quando a trilha versionada revelar de forma clara a existência de um checkpoint canônico em `docs/checkpoints/`, o sistema **não deve** continuar afirmando ausência de checkpoint apenas porque a listagem direta da pasta falhou.

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
No `quickloadF9`, a cronologia soberana deve ser aplicada sobre o **melhor rastro confiável disponível** do checkpoint canônico, e não apenas sobre a primeira listagem estrutural da pasta.

## Regra de honestidade reforçada

Quando usar busca expandida, o sistema deve dizer explicitamente:
- que a listagem direta foi insuficiente
- que recorreu à trilha versionada do repositório
- se encontrou checkpoint por commit, diff ou arquivo
- qual modo de verificação foi usado
- e se a restauração final ocorreu com base nessa trilha expandida

## Formulação canônica da correção

A `loadstateF9` deve buscar checkpoints primeiro pela pasta canônica `docs/checkpoints/`, mas, se a listagem direta for insuficiente, deve obrigatoriamente recorrer à trilha versionada do repositório oficial antes de concluir ausência real de checkpoint. Em `quickloadF9`, essa busca expandida é parte do próprio dever de restaurar o último estado salvo válido sem depender de apontamento manual do usuário quando o rastro já existir no GitHub.
