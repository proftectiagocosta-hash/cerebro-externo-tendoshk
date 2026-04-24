# EXPORT_CHAT_VIVO — Roadmap e Rastreio de Evolução

## Natureza

Este documento registra o estado evolutivo do `EXPORT_CHAT_VIVO` após sua criação como protocolo operacional, script executor e workflow GitHub-first.

Ele existe para impedir que ideias de evolução do sistema fiquem apenas como conversa, sugestão solta ou escala retórica sem rastreio.

## Estado confirmado

Até este registro, existem no repositório:

```txt
docs/sistema/export_chat_vivo/protocolo_export_chat_vivo.md
docs/sistema/export_chat_vivo/index.md
docs/sistema/export_chat_vivo/index.json
tools/export_chat_vivo.py
.github/workflows/export_chat_vivo.yml
```

## Implementado

### 1. Protocolo operacional

`EXPORT_CHAT_VIVO` foi definido como protocolo operacional em `docs/sistema/export_chat_vivo/`, ainda não promovido a master soberano.

Função: preservar a fonte do chat atual antes de curadoria, checkpoint, Knot ou NPT.

### 2. Camada RAW

O executor local foi desenhado para salvar o conteúdo bruto em arquivos RAW antes de gerar o Markdown estruturado.

Regra central:

```txt
persistência não é referência;
persistência é armazenamento real.
```

### 3. Script executor

Criado:

```txt
tools/export_chat_vivo.py
```

Funções previstas:

```txt
init
append
close
```

Responsabilidades:

- salvar RAW;
- calcular hash SHA-256;
- criar/atualizar arquivo `.md` do chat vivo;
- criar blocos sequenciais;
- atualizar `index.md`;
- atualizar `index.json`.

### 4. Workflow GitHub-first

Criado:

```txt
.github/workflows/export_chat_vivo.yml
```

Função: permitir execução via GitHub Actions, sem depender de clone local do repositório.

Fluxo previsto:

```txt
usuário cria/atualiza arquivo de entrada no GitHub
↓
executa Action manualmente
↓
Action roda tools/export_chat_vivo.py
↓
RAW + .md + índices são atualizados
↓
Action commita alterações
```

## Limites atuais

### 1. Entrada ainda é manual

O workflow não captura automaticamente o conteúdo do navegador do ChatGPT.

Ele processa apenas o arquivo `.txt` que o usuário coloca no repositório.

Formulação:

```txt
GitHub Actions não copia o chat do navegador.
GitHub Actions processa o arquivo que o usuário colocou no repositório.
```

### 2. Init e append ainda exigem decisão do usuário

O modo atual exige escolher:

```txt
init
append
close
```

Ainda não há modo `auto` consolidado.

### 3. Deduplicação ainda não é destrutiva

O script v0.1 preserva blocos RAW integralmente.

Não remove sobreposição de forma agressiva, para evitar perda por suposição.

## Evoluções propostas registradas

As ideias abaixo foram mencionadas como próximos níveis, mas ainda não estão implementadas.

### EV-01 — Modo AUTO

Objetivo:

Permitir que o sistema decida automaticamente entre `init` e `append`.

Ideia inicial:

```txt
se não houver chat ativo → init
se houver chat ativo → append
```

Requisitos:

- ponteiro de chat ativo;
- arquivo de estado local ou versionado;
- regra de fechamento;
- tratamento de conflito quando houver mais de um chat em andamento.

Status:

```txt
proposto_nao_implementado
```

### EV-02 — Ponteiro de chat ativo

Objetivo:

Registrar o último `chat_id` ativo para evitar digitação manual no append.

Possível local:

```txt
docs/sistema/export_chat_vivo/current_chat.json
```

Campos possíveis:

```json
{
  "chat_id": "",
  "arquivo": "",
  "status": "em_andamento",
  "atualizado_em": ""
}
```

Status:

```txt
proposto_nao_implementado
```

### EV-03 — Deduplicação e sobreposição segura

Objetivo:

Detectar quando um novo CTRL+A contém conteúdo já salvo e adicionar apenas o trecho novo.

Regra de segurança:

```txt
não descartar conteúdo por suposição.
```

Estratégia possível:

- comparar hash integral;
- comparar sufixo do bloco anterior com prefixo do novo bloco;
- se confiança baixa, preservar RAW completo e marcar revisão.

Status:

```txt
proposto_nao_implementado
```

### EV-04 — Chunking automático posterior

Objetivo:

Dividir RAWs ou chats vivos em chunks curáveis.

Importante:

Chunking pertence a etapa posterior, não à captura.

Status:

```txt
proposto_nao_implementado
```

### EV-05 — Integração com curadoria auditável

Objetivo:

Permitir que um chat vivo fechado alimente uma curadoria por blocos, sem confundir exportação com interpretação.

Dependências:

- protocolo de curadoria exaustiva;
- índice de cobertura;
- regra clara de `resumo != curadoria`.

Status:

```txt
proposto_nao_implementado
```

### EV-06 — Integração com NPT

Objetivo:

Gerar candidatos a `[NPT_ENTRY]` após curadoria, não durante exportação.

Regra:

```txt
EXPORT_CHAT_VIVO preserva fonte.
NPT consolida memória.
```

Status:

```txt
proposto_nao_implementado
```

### EV-07 — Integração com FRACTAL_KNOT

Objetivo:

Permitir que chats vivos revelem candidatos a Knot após análise posterior.

Regra:

```txt
Exportar chat vivo não consolida NO_VIVO.
```

Status:

```txt
proposto_nao_implementado
```

### EV-08 — Promoção futura a master soberano

Objetivo:

Avaliar se `EXPORT_CHAT_VIVO` deve ser promovido de protocolo operacional para master soberano.

Condição mínima:

- teste real com `init`;
- teste real com `append`;
- teste real com `close`;
- evidência de que o fluxo não gera falsa persistência;
- evidência de que o índice é atualizado corretamente.

Status:

```txt
bloqueado_ate_teste_operacional
```

## Ordem recomendada de evolução

```txt
1. testar workflow atual com init
2. testar append
3. testar close
4. registrar falhas reais
5. só então implementar modo AUTO
6. só então considerar integração com curadoria
7. só então considerar promoção a master
```

## Regra de rastreio

Toda nova ideia de evolução do `EXPORT_CHAT_VIVO` deve ser registrada neste arquivo ou em documento sucessor antes de ser tratada como direção oficial.

Formulação:

```txt
EVOLUÇÃO SEM RASTREIO = SUGESTÃO SOLTA
EVOLUÇÃO COM RASTREIO = LINHA DE SISTEMA
```

## Estado final deste registro

O `EXPORT_CHAT_VIVO` está em fase operacional inicial.

Ele possui protocolo, executor e workflow, mas ainda depende de teste real para validar seu comportamento antes de evoluções mais ambiciosas.
