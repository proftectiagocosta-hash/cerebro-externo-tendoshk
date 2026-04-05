# Cérebro Externo Tendoshk — v1 Piloto

## Status

Piloto local validado.

## Natureza

O Cérebro Externo Tendoshk, nesta v1, é uma camada inteligente anterior à ingestão oficial do NPT. Sua função atual não é substituir o NPT/Colab, mas preparar melhor o material antes da entrada no fluxo oficial.

---

## Objetivo da v1

Validar um piloto local capaz de:

- receber texto direto ou arquivo
- classificar conteúdo
- priorizar
- curar
- rotear
- empacotar saída útil
- exportar material reutilizável para etapas posteriores do ecossistema

---

## Escopo atual

### Ambiente validado
- WSL / Ubuntu
- VS Code
- workspace Linux em `~/code/cerebro-externo-tendoshk`
- repositório Git próprio
- sincronização com GitHub

### Componentes implementados
- `memory_loader.py`
- `priority_engine.py`
- `classifier.py`
- `curator.py`
- `router.py`
- `pipeline.py`
- `src/cli/main.py`

### Capacidades atuais da CLI
- `--text`
- `--file`
- `--output`
- `--format text/json`
- `--save-run`
- `--export-blocks`

### Cobertura atual
Já existem testes para:
- módulos centrais
- pipeline
- CLI
- persistência
- exportação

### Ajuste estrutural já feito
`.gitignore` corrigido para ignorar:
- `data/runs/`
- `data/exports/`

---

## Papel estratégico atual

O Cérebro Externo Tendoshk deve ser entendido, neste estágio, como:

- pré-processador inteligente
- camada auxiliar de triagem e curadoria
- ponte entre material bruto e ingestão disciplinada
- experimento arquitetural com potencial sistêmico futuro

Ele ainda não deve ser tratado como substituto do NPT/Colab.

---

## O que esta v1 já prova

A v1 já prova que é possível:

1. separar o piloto do restante do ecossistema em repositório próprio
2. executar localmente uma camada de inteligência útil
3. testar CLI, pipeline e persistência de forma organizada
4. gerar uma base concreta para futura aproximação com o NPT

---

## O que esta v1 ainda não deve fazer

A v1 ainda não deve:

- redefinir a arquitetura oficial do NPT
- substituir ingestão manual/curada
- criar novo projeto canônico no Drive
- assumir governança documental própria dentro do ecossistema

---

## Limite arquitetural atual

O Cérebro Externo ainda está em fase de piloto. Por isso, seu valor deve ser absorvido pela estrutura já existente, especialmente nas camadas:

- `AMBIENTES_RETOMADA`
- `NPT_NUCLEO_PERSISTENTE_TENDOSHK`
- `SISTEMA_MEMORIA_AUDITORIA`

---

## Próximo passo recomendado

O próximo passo mais inteligente após a validação da v1 é:

1. documentar formalmente o piloto
2. consolidar a governança do Drive/NPT
3. mapear integrações progressivas com o fluxo NPT
4. só depois ampliar inteligência ou formalizar nova frente

---

## Critérios para evolução futura

A próxima evolução do Cérebro Externo deve ser avaliada com base em:

- robustez da saída gerada
- aderência ao fluxo real do NPT
- redução de atrito operacional
- capacidade de gerar blocos/artefatos consistentes
- clareza de seu papel dentro do ecossistema

---

## Decisão vigente

A v1 do Cérebro Externo Tendoshk está validada como piloto local e deve seguir, por enquanto, como camada inteligente anterior à ingestão oficial, sem institucionalização canônica própria.