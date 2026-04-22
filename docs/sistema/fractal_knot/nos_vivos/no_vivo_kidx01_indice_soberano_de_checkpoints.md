# NO_VIVO — INDICE_SOBERANO_DE_CHECKPOINTS

## Identidade
- id_curto=KIDX01
- nome_funcional=INDICE_SOBERANO_DE_CHECKPOINTS
- estado=ativo

## Eixo
Criar uma camada canônica de inventário e ponteiro de último checkpoint para blindar `quickloadF9` e `loadstateF9` contra falhas da busca indexada e ausência de listagem bruta confiável da pasta `docs/checkpoints/`.

## Origem
Linha viva consolidada a partir da investigação estrutural sobre:
- busca indexada do conector GitHub não equivaler a listagem bruta de diretório
- retorno parcial de checkpoints via `search`
- risco de o `quickload` localizar apenas o último checkpoint visível para a busca, e não o último checkpoint existente na pasta
- necessidade de transformar `search` em fallback, e não em fonte soberana da retomada
- proposta de acoplamento entre `savestateF5`, índice de checkpoints e ponteiro canônico do último checkpoint

## Checkpoint
- checkpoint_referencia=
- ancorada_em_checkpoint=nao

## Capturas transversais
- acao_principal: definir um índice soberano de checkpoints como inventário canônico da pasta
  efeito_lateral: retira da busca indexada a soberania indevida sobre a listagem de checkpoints
  linha_afetada: loadstateF9

- acao_principal: definir um ponteiro canônico para o último checkpoint válido
  efeito_lateral: permite ao quickload ler uma verdade registrada em vez de inferir o último checkpoint por busca parcial
  linha_afetada: quickloadF9

- acao_principal: acoplar a atualização do índice e do ponteiro ao rito do savestate
  efeito_lateral: checkpoint salvo sem atualização do índice passa a ser considerado save incompleto do ponto de vista sistêmico
  linha_afetada: savestateF5

- acao_principal: permitir futura segmentação do inventário por volume, preservando um índice mestre
  efeito_lateral: evita inflacao operacional quando o histórico de checkpoints crescer demais
  linha_afetada: governanca_de_checkpoints

## Baixa auditavel
- status=
- motivo=
- destino=
- contexto=

## Notas de governanca
Esta linha não se confunde com checkpoint.
Esta linha não se confunde com loadstate.
Esta linha não se confunde com curadoria.

Trata-se de uma linha viva sobre a própria governança do mecanismo de retomada entre chats.

## Formula minima persistida
```txt
NO_VIVO
id_curto=KIDX01
nome_funcional=INDICE_SOBERANO_DE_CHECKPOINTS
estado=ativo
eixo=criar uma camada canônica de inventário e ponteiro de ultimo checkpoint para blindar quickload e loadstate contra falhas da busca indexada
origem=investigacao sobre a busca parcial em docs/checkpoints e proposta de indice soberano com ponteiro canonico
checkpoint_referencia=
ancorada_em_checkpoint=nao

capturas_transversais=
- acao_principal: definir um índice soberano de checkpoints como inventário canônico da pasta
- efeito_lateral: retira da busca indexada a soberania indevida sobre a listagem de checkpoints
- linha_afetada: loadstateF9

- acao_principal: definir um ponteiro canônico para o último checkpoint válido
- efeito_lateral: permite ao quickload ler uma verdade registrada em vez de inferir o último checkpoint por busca parcial
- linha_afetada: quickloadF9

- acao_principal: acoplar a atualização do índice e do ponteiro ao rito do savestate
- efeito_lateral: checkpoint salvo sem atualização do índice passa a ser considerado save incompleto do ponto de vista sistêmico
- linha_afetada: savestateF5

- acao_principal: permitir futura segmentação do inventário por volume, preservando um índice mestre
- efeito_lateral: evita inflacao operacional quando o histórico de checkpoints crescer demais
- linha_afetada: governanca_de_checkpoints

baixa_auditavel=
- status:
- motivo:
- destino:
- contexto:
```