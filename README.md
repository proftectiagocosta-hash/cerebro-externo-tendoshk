# Cérebro Externo Tendoshk

Arquitetura piloto do Cérebro Externo Tendoshk: memória operacional, roteamento de tarefas, curadoria NPT e copiloto estrutural do ecossistema.

## Objetivo

Criar um núcleo externo e versionável para apoiar o ecossistema Tendoshk com:

- memória organizada
- classificação de entradas
- sugestão de projeto canônico
- geração de blocos `[CHAT_INDEX]`
- geração de blocos `[NPT_ENTRY]`
- checkpoints locais de evolução

## Estrutura inicial

- `docs/` → visão, arquitetura, backlog e protocolos
- `memory/` → identidade, projetos, memória episódica e procedural
- `schemas/` → contratos de dados
- `src/` → núcleo, agentes, CLI e utilitários
- `tests/` → testes do piloto
- `logs/` → devlog e checkpoints operacionais

## Versão atual

Piloto v0.1

## Primeiro marco

Receber um texto bruto e retornar:

1. classificação
2. projeto sugerido
3. bloco `[CHAT_INDEX]`
4. bloco `[NPT_ENTRY]` quando aplicável
5. checkpoint local