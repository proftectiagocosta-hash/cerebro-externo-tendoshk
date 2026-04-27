# EXPORT_CHAT_VIVO — Validação Operacional v0.1

## Natureza

Este documento registra a validação operacional mínima do `EXPORT_CHAT_VIVO`.

Ele complementa o roadmap em:

```txt
docs/estado/export_chat_vivo_roadmap_e_rastreio.md
```

## Ciclo testado

```txt
init -> append -> close
```

## Status

```txt
validado
```

## Evidência observada

Arquivo validado pelo usuário:

```txt
docs/sistema/export_chat_vivo/chats/2026/04/2026_04_24_teste_export_chat_vivo.md
```

Conteúdo estrutural observado:

```txt
status: fechado
ultimo_bloco: 002
BLOCO 001 presente
BLOCO 002 presente
raw_file registrado em cada bloco
hash SHA-256 registrado em cada bloco
```

## Resultado

O `EXPORT_CHAT_VIVO` deixou de ser apenas protocolo planejado e passou a ter ciclo operacional mínimo validado.

## Observação técnica

Durante os testes, foi observado warning futuro do GitHub Actions sobre Node.js 20. O warning não bloqueou o fluxo validado.

## Próxima evolução recomendada

```txt
1. especificar current_chat.json
2. implementar modo auto
3. testar modo auto
4. só depois avançar para curadoria/NPT/Knot
```

## Regra de rastreio aplicada

```txt
EVOLUCAO SEM RASTREIO = SUGESTAO SOLTA
EVOLUCAO COM RASTREIO = LINHA DE SISTEMA
```
