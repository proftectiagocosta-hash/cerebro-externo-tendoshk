# PROTOCOLO EXPORT_CHAT_VIVO v0.1

## 0. Natureza

O `EXPORT_CHAT_VIVO` é um protocolo operacional do Cérebro Externo Tendoshk para registrar o conteúdo de um chat atual em arquivo Markdown versionado, por blocos sequenciais, sem depender exclusivamente da memória ativa do ChatGPT, da janela de contexto ou de exportações globais posteriores.

Este protocolo não é, inicialmente, um master soberano.

Ele deve nascer como protocolo operacional em:

```txt
docs/sistema/export_chat_vivo/
```

Sua função é criar uma ponte segura entre:

- conversa em andamento;
- conteúdo colado manualmente pelo usuário;
- arquivo Markdown persistido;
- índice de chats vivos;
- futura curadoria auditável.

## 1. Problema que este protocolo resolve

O ChatGPT não garante leitura integral confiável de chats longos dentro da própria plataforma.

A conversa ativa pode exceder a janela de contexto, fazendo com que partes importantes fiquem inacessíveis ou sejam apenas inferidas.

O `EXPORT_CHAT_VIVO` existe para impedir que o chat atual fique fora da infraestrutura de memória apenas porque ainda não entrou em uma exportação global do ChatGPT.

Formulação central:

```txt
CHAT_ATUAL_LONGO != FONTE_INTEGRAL_CONFIAVEL
SEM_REGISTRO_INCREMENTAL,
O_CHAT_ATUAL_CONTINUA_VULNERAVEL_A_PERDA_DE_CONTEXTO
```

## 2. Objetivo

Registrar o chat atual em Markdown de forma incremental, auditável e recuperável.

O objetivo não é curar, resumir ou interpretar o conteúdo durante a captura.

O objetivo é preservar a fonte.

```txt
EXPORTAR PRIMEIRO.
CURAR DEPOIS.
```

## 3. Regra central

Durante a captura do `EXPORT_CHAT_VIVO`, o sistema deve obedecer:

```txt
NÃO RESUMIR.
NÃO CURAR.
NÃO INTERPRETAR.
NÃO REESCREVER SENTIDO.
NÃO SOBRESCREVER.
APENAS REGISTRAR, FORMATAR MINIMAMENTE E ANEXAR.
```

A curadoria estrutural pertence a etapa posterior, governada por `curadoriav61` ou por protocolo de curadoria por blocos.

## 4. Local proposto no repositório

Estrutura inicial recomendada:

```txt
docs/sistema/export_chat_vivo/
├── protocolo_export_chat_vivo.md
├── index.md
├── index.json
├── inbox/
│   └── chat_atual.txt
├── raw/
│   └── AAAA/
│       └── MM/
│           └── chat_id__bloco_001.txt
└── chats/
    └── AAAA/
        └── MM/
            └── chat_AAAA_MM_DD_slug_curto.md
```

Exemplo:

```txt
docs/sistema/export_chat_vivo/chats/2026/04/chat_2026_04_24_memoria_governavel.md
```

## 5. Estados possíveis do chat vivo

Cada chat vivo deve ter um dos estados:

```txt
em_andamento
pausado
fechado
reconciliado
curado
arquivado
```

## 6. Metadados obrigatórios do arquivo de chat

Cada arquivo `.md` de chat vivo deve iniciar com cabeçalho:

```md
---
protocolo: EXPORT_CHAT_VIVO
versao_protocolo: v0.1
chat_id: 
titulo: 
slug: 
status: em_andamento
origem: copia_manual_usuario | janela_visivel_assistente | misto
cobertura: parcial | integral_declarada_pelo_usuario | desconhecida
criado_em: AAAA-MM-DD HH:MM
atualizado_em: AAAA-MM-DD HH:MM
ultimo_bloco: 000
arquivo_origem: chatgpt_web
observacoes: 
---
```

## 7. Unidade mínima: bloco de captura

A unidade mínima do `EXPORT_CHAT_VIVO` é o bloco.

Cada bloco deve ser registrado em sequência:

```md
## BLOCO 001

metadados_bloco:
- origem: ctrl_a_usuario | trecho_colado_usuario | janela_visivel_assistente
- cobertura_bloco: integral_declarada | parcial | desconhecida
- recebido_em: AAAA-MM-DD HH:MM
- hash_conteudo: 
- raw_file: 
- bloco_anterior: nenhum
- sobreposicao_tratada: sim | nao | nao_aplicavel

<!-- EXPORT_CHAT_VIVO_START:BLOCO_001 -->

conteudo: arquivo_externo
arquivo_raw: `docs/sistema/export_chat_vivo/raw/AAAA/MM/chat_id__bloco_001.txt`
hash_sha256: ``

<!-- EXPORT_CHAT_VIVO_END:BLOCO_001 -->
```

## 8. Regra de cobertura

A cobertura nunca deve ser presumida.

Valores permitidos:

```txt
parcial
integral_declarada_pelo_usuario
desconhecida
```

## 9. Regra de append incremental

Ao receber novo conteúdo para um chat vivo já existente, o sistema deve:

1. localizar o arquivo do chat vivo pelo índice;
2. abrir o arquivo existente;
3. identificar o `ultimo_bloco`;
4. verificar se o novo conteúdo é bloco novo, repetição integral, repetição parcial com acréscimo ou trecho ambíguo;
5. não sobrescrever conteúdo anterior;
6. criar novo bloco sequencial;
7. registrar sobreposição, quando detectada;
8. atualizar metadados do arquivo;
9. atualizar `index.md` e `index.json`.

## 10. Regra de sobreposição

É proibido descartar conteúdo por suposição.

Se houver sobreposição clara entre bloco novo e bloco anterior, o sistema pode remover apenas a parte duplicada quando a equivalência for verificável.

Se houver dúvida, registrar o novo bloco integralmente e marcar:

```txt
sobreposicao_tratada: nao
observacao: possivel_duplicacao_a_revisar
```

## 11. Marcadores de segurança

Todo bloco deve conter marcadores explícitos:

```txt
<!-- EXPORT_CHAT_VIVO_START:BLOCO_XXX -->
<!-- EXPORT_CHAT_VIVO_END:BLOCO_XXX -->
```

Esses marcadores servem para delimitar conteúdo bruto, facilitar append, comparação, chunking posterior e impedir mistura entre metadados e conteúdo.

## 12. Índice obrigatório

Todo chat vivo deve ser registrado em:

```txt
docs/sistema/export_chat_vivo/index.md
docs/sistema/export_chat_vivo/index.json
```

Campos mínimos do índice:

```txt
chat_id
titulo
slug
arquivo
status
cobertura
ultimo_bloco
criado_em
atualizado_em
origem
observacoes
```

## 13. Gatilhos de uso

O protocolo pode ser acionado quando o usuário disser algo como:

```txt
exportar chat vivo
exportar chat atual
salvar chat atual em md
anexar bloco ao export vivo
atualizar export vivo
fechar export vivo
```

Esses gatilhos não devem ser tratados como `savestateF5`, `curadoriav61` ou `FRACTAL_KNOT`.

Eles pertencem à camada de preservação de fonte.

## 14. Separação entre export, curadoria e checkpoint

O `EXPORT_CHAT_VIVO` não substitui:

- `curadoriav61`;
- `savestateF5`;
- `loadstateF9`;
- `FRACTAL_KNOT`;
- NPT;
- checkpoint;
- export global do ChatGPT.

Diferença central:

```txt
EXPORT_CHAT_VIVO = preserva fonte do chat atual.
CURADORIA = interpreta e extrai valor.
CHECKPOINT = salva estado de continuidade.
KNOT = governa linha viva.
NPT = consolida memória persistente.
```

## 15. Relação com `EXECUCAO_REPO`

Quando o `EXPORT_CHAT_VIVO` exigir escrita real no GitHub, a operação deve respeitar `EXECUCAO_REPO`.

Isso significa:

- não dizer que salvou se apenas propôs;
- não substituir escrita real por instrução manual se a escrita estiver autorizada e disponível;
- declarar se o arquivo foi criado, atualizado, bloqueado ou apenas preparado;
- atualizar índice junto com o arquivo do chat.

## 16. Relação com `PRESENÇA VIVA` e consciência estrutural

Toda operação do `EXPORT_CHAT_VIVO` deve respeitar a regra de consciência estrutural.

O sistema deve distinguir:

```txt
[CONFIRMADO]
[INFERIDO]
[HIPÓTESE]
```

Aplicação prática:

- `[CONFIRMADO]`: conteúdo colado pelo usuário foi recebido e registrado.
- `[INFERIDO]`: conteúdo parece continuação do bloco anterior.
- `[HIPÓTESE]`: conteúdo pode estar duplicado, mas não há evidência suficiente para remover.

É proibido afirmar cobertura integral sem declaração do usuário ou evidência suficiente.

## 17. Relação com export global do ChatGPT

O `EXPORT_CHAT_VIVO` não substitui o export global.

Ele cobre o intervalo entre:

```txt
chat em andamento
↓
registro vivo incremental
↓
futuro export global
↓
reconciliação posterior
```

Quando o export global estiver disponível, o chat vivo pode ser reconciliado com ele.

## 18. Modo GitHub-first com GitHub Actions

Quando o usuário não possuir o repositório clonado localmente, o `EXPORT_CHAT_VIVO` pode operar em modo GitHub-first.

Nesse modo, o fluxo correto é:

```txt
1. usuário cria ou atualiza um arquivo .txt no GitHub;
2. arquivo preferencial: docs/sistema/export_chat_vivo/inbox/chat_atual.txt;
3. usuário executa manualmente a GitHub Action EXPORT_CHAT_VIVO;
4. a Action roda tools/export_chat_vivo.py;
5. o script cria RAW, chat .md e atualiza index.md/index.json;
6. a Action commita e envia as alterações para a branch principal.
```

### 18.1 Arquivo de entrada no GitHub

O arquivo de entrada padrão no modo GitHub-first é:

```txt
docs/sistema/export_chat_vivo/inbox/chat_atual.txt
```

Esse arquivo é área de entrada, não memória final.

A fonte preservada passa a ser o RAW gerado em:

```txt
docs/sistema/export_chat_vivo/raw/AAAA/MM/
```

### 18.2 Workflow canônico

O workflow canônico deve viver em:

```txt
.github/workflows/export_chat_vivo.yml
```

Ele deve aceitar, no mínimo:

```txt
mode: init | append | close
title
chat_id
input_file
coverage
origin
observations
```

### 18.3 Regra de commit automático

A Action só deve commitar se houver alterações reais.

Se não houver alterações, deve declarar explicitamente:

```txt
[CONFIRMADO] Nenhuma alteração detectada para commit.
```

### 18.4 Limite do modo GitHub-first

O modo GitHub-first não elimina a necessidade de o usuário inserir o conteúdo inicial em um arquivo `.txt` no repositório.

Ele elimina a necessidade de clone local e execução local de Python.

Formulação:

```txt
GitHub Actions não copia o chat do navegador.
GitHub Actions processa o arquivo que o usuário colocou no repositório.
```

## 19. Regras de fechamento do chat vivo

Quando o usuário declarar fechamento, o sistema deve:

1. marcar `status: fechado`;
2. atualizar índice;
3. registrar último bloco;
4. declarar cobertura final;
5. indicar se o chat ainda precisa de curadoria;
6. indicar se deve gerar `[CHAT_INDEX]`, `[NPT_ENTRY]`, checkpoint ou Knot em etapa posterior.

## 20. Regras de erro

Se o sistema não conseguir acessar o arquivo existente:

```txt
status_operacao: bloqueado
motivo: arquivo_nao_acessivel
```

Se houver conflito entre índice e arquivo:

```txt
status_operacao: inconsistencia_detectada
acao: verificar_index_e_arquivo_antes_de_append
```

Se houver risco de duplicação:

```txt
status_operacao: append_com_alerta
observacao: possivel_duplicacao_a_revisar
```

## 21. Critério de sucesso

A operação de export vivo é bem-sucedida quando:

- o arquivo de chat existe;
- o bloco foi adicionado sem sobrescrever bloco anterior;
- a cobertura foi declarada corretamente;
- o índice foi atualizado;
- o estado final da operação foi informado honestamente.

## 22. Critério de falha

A operação falha quando:

- o sistema afirma ter salvo sem ter escrito;
- o conteúdo é resumido em vez de registrado;
- o conteúdo anterior é sobrescrito sem autorização;
- a cobertura é presumida;
- o índice não é atualizado;
- o bloco novo é misturado ao anterior sem delimitação.

## 23. Fluxo mínimo de uso

### 23.1 Criar novo chat vivo

1. Usuário solicita exportação do chat atual.
2. Usuário cola conteúdo inicial ou envia arquivo de entrada.
3. Sistema cria arquivo `.md`.
4. Sistema cria BLOCO 001.
5. Sistema atualiza índice.
6. Sistema declara resultado.

### 23.2 Atualizar chat vivo

1. Usuário cola novo trecho ou atualiza arquivo de entrada.
2. Sistema identifica arquivo existente.
3. Sistema cria BLOCO seguinte.
4. Sistema verifica sobreposição.
5. Sistema atualiza índice.
6. Sistema declara resultado.

### 23.3 Fechar chat vivo

1. Usuário solicita fechamento.
2. Sistema marca `status: fechado`.
3. Sistema atualiza índice.
4. Sistema recomenda próxima etapa.

## 24. Próxima etapa após este protocolo

Antes de promover este protocolo a master soberano, deve haver teste real com pelo menos um chat atual.

Teste mínimo:

```txt
1. criar arquivo vivo do chat atual;
2. adicionar BLOCO 001 por conteúdo colado ou arquivo de entrada;
3. adicionar BLOCO 002 com conteúdo posterior;
4. verificar duplicação;
5. atualizar índice;
6. declarar cobertura;
7. fechar ou manter em andamento.
```

## 25. Regra final

O `EXPORT_CHAT_VIVO` existe para transformar conversa em fonte preservada antes que ela se perca na limitação da janela de contexto.

Ele não cria memória por interpretação.

Ele cria base auditável para que memória, curadoria, checkpoint e Knot possam existir depois com mais confiança.
