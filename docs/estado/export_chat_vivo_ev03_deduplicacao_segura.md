# EXPORT_CHAT_VIVO — EV-03 Deduplicação Segura

## Natureza

Este documento especifica a evolução EV-03 do `EXPORT_CHAT_VIVO`.

Objetivo: impedir que o sistema anexe blocos duplicados quando o mesmo conteúdo de entrada for enviado mais de uma vez.

## Problema observado

Durante o teste do ponteiro `current_chat.json`, o sistema criou `BLOCO 001` e `BLOCO 002` com o mesmo hash SHA-256.

Isso confirmou que o ponteiro ativo funciona, mas revelou uma lacuna:

```txt
O sistema sabe QUAL chat usar,
mas ainda não sabe O QUE já foi salvo.
```

## Regra central

```txt
NÃO DUPLICAR CONTEÚDO IDÊNTICO.
NÃO DESCARTAR CONTEÚDO POR SUPOSIÇÃO.
```

## Fase EV-03.1 — Hash exato

A primeira implementação de deduplicação deve ser conservadora.

Ela só deve impedir append quando o hash SHA-256 do novo conteúdo for exatamente igual ao hash de bloco já registrado no arquivo do chat.

### Comportamento esperado

Se o novo hash já existir no arquivo `.md` do chat:

```txt
status_operacao: duplicado_detectado
acao: nao_criar_novo_bloco
```

O sistema não deve:

- criar novo RAW;
- criar novo BLOCO;
- atualizar `ultimo_bloco`;
- sobrescrever conteúdo existente.

## Fase EV-03.2 — Sobreposição parcial

A sobreposição parcial fica bloqueada para implementação futura.

Motivo:

```txt
remover texto por aproximação pode causar perda de conteúdo válido.
```

Antes de remover sobreposição parcial, o sistema precisa de teste controlado e regra de confiança.

## Critério de sucesso EV-03.1

1. Enviar o mesmo arquivo de entrada duas vezes.
2. O segundo envio deve detectar hash duplicado.
3. Nenhum bloco novo deve ser criado.
4. O índice não deve avançar `ultimo_bloco`.
5. O workflow pode concluir sem alterações para commit.

## Estado

```txt
EV-03.1 liberado para implementação
EV-03.2 bloqueado para especificação futura
```
