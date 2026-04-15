# CONTINUIDADE_VERIFICAVEL — Governança de Prova Formal da Continuidade no Cérebro Tendoshk

## Natureza

A `CONTINUIDADE_VERIFICAVEL` é uma peça complementar, permanente e crítica da arquitetura de retomada do Cérebro Externo Tendoshk.

Sua função não é substituir `loadstateF9`, `quickloadF9`, `curadoriav61`, `savestateF5`, checkpoint ou NPT, mas governar a validação formal da continuidade antes que qualquer rotina de load seja tratada como concluída.

Ela existe para impedir que o sistema:
- trate plausibilidade como prova
- confunda checkpoint coerente com checkpoint real
- aplique contexto antes de provar recência
- deixe a continuidade depender da memória recente do usuário
- produza falsa sensação de restauração correta

## Função

A `CONTINUIDADE_VERIFICAVEL` existe para definir, de forma estável:

- como provar recência real de checkpoint
- como distinguir checkpoint cronologicamente soberano de checkpoint apenas semanticamente próximo
- como separar localização do checkpoint de aplicação do checkpoint ao chat atual
- como impedir carga por plausibilidade estrutural
- como classificar o material novo do chat atual sem sequestrar o eixo salvo
- como exigir saída auditável antes de tratar continuidade como concluída
- como priorizar verificação determinística por caminho canônico e trilha cronológica verificável

## Separação dura

A `CONTINUIDADE_VERIFICAVEL`:

- não substitui `loadstateF9`
- não substitui `quickloadF9`
- não faz load state por si só
- não faz save state
- não gera checkpoint
- não faz curadoria
- não escolhe projeto
- não decide incorporação de ativos
- não altera repositório por si só
- não aplica o estado ao chat por si só

Ela apenas:
- verifica
- classifica
- valida
- autoriza ou bloqueia a declaração de continuidade concluída

## Dependência operacional ordinária

A `CONTINUIDADE_VERIFICAVEL` não é peça de acionamento livre por menção vaga.

Sua governança operacional ordinária ocorre sob `loadstateF9` ou `quickloadF9`, quando houver necessidade de validar formalmente a continuidade antes da aplicação do estado ao chat atual.

### Regra derivada

`loadstateF9` governa a retomada.  
`CONTINUIDADE_VERIFICAVEL` governa a prova formal da integridade dessa retomada.

### Regra crítica

É proibido tratar a `CONTINUIDADE_VERIFICAVEL` como substituta de `loadstateF9` ou `quickloadF9`.

## Problema que esta peça combate

Um sistema pode:

- localizar um checkpoint plausível
- interpretar corretamente seu conteúdo
- produzir resposta coerente
- parecer seguro
- e ainda assim estar carregando o checkpoint errado

Também pode:

- misturar checkpoint real com checkpoint semanticamente próximo
- aplicar compatibilidade contextual antes da prova cronológica
- depender da memória recente do usuário para correção
- usar busca ampla como se fosse prova suficiente

Essa peça existe para impedir exatamente essa degradação.

## Regra de acionamento

A `CONTINUIDADE_VERIFICAVEL` deve ser acionada quando houver necessidade de:

- provar qual é o checkpoint real mais recente
- validar integridade de uma rotina de load
- listar checkpoints recentes com segurança mínima
- distinguir recência cronológica de afinidade temática
- classificar material novo do chat atual sem invalidar automaticamente o eixo salvo
- declarar uma restauração como concluída

## Gatilho operacional ordinário

O gatilho ordinário desta peça ocorre quando coexistirem, de forma suficiente:

1. intenção real de retomar estado salvo
2. uso de `quickloadF9`, `loadstateF9` ou equivalente funcional
3. existência de checkpoint(s) rastreáveis no repositório
4. necessidade de provar a continuidade antes da aplicação final ao chat
5. risco relevante de confundir plausibilidade com recência real

### Regra crítica

Sem esses elementos, a peça pode ser lida, estudada ou usada como referência, mas não deve ser tratada como validação formal de continuidade operacionalmente em curso.

## Regra crítica central

É proibido tratar checkpoint plausível, coerente ou semanticamente compatível como prova suficiente de continuidade correta.

Coerência aparente não substitui prova cronológica.  
Compatibilidade temática não substitui soberania de recência.

## Regra de rastreio assertivo da continuidade

Quando a operação exigir validação de checkpoint, recência, existência de histórico de continuidade ou confirmação de artefato estrutural em caminho conhecido, a verificação deve priorizar consulta determinística por caminho exato e trilha cronológica verificável.

Busca semântica ampla, textual ou aproximativa pode servir como apoio exploratório, mas não deve ser tratada como prova principal de:

- presença
- ausência
- recência
- soberania cronológica
- integridade da continuidade

### Ordem correta da verificação documental

Sempre que possível, a validação deve obedecer a esta ordem:

1. verificar primeiro o caminho canônico exato
2. verificar depois a presença do checkpoint candidato
3. verificar depois a existência de checkpoint posterior rastreável
4. verificar trilha versionada quando a listagem direta não bastar
5. só usar busca ampla como apoio exploratório quando o caminho não for conhecido ou quando a verificação direta falhar
6. não concluir ausência, falha ou soberania apenas porque a busca ampla devolveu itens plausíveis porém não determinísticos

### Regra crítica

É proibido tratar busca genérica como prova principal de continuidade quando o sistema já possui convenção explícita de caminho ou trilha verificável.

### Regra crítica adicional

Plausibilidade sem verificação determinística não equivale a continuidade validada.

## Blocos obrigatórios de validação

Toda rotina de continuidade suficientemente sensível deve avaliar, no mínimo, quatro blocos.

### Bloco 1 — Recência

Pergunta central:

“Este é realmente o checkpoint cronologicamente soberano para o modo solicitado?”

Classificações permitidas:

- recência confirmada
- recência provável, mas não plena
- recência inconclusiva
- recência refutada

### Bloco 2 — Fonte da verificação

Pergunta central:

“De onde veio a prova de recência?”

Exemplos aceitáveis:

- caminho canônico direto
- pasta de checkpoints
- trilha cronológica verificável
- trilha versionada
- combinação entre os métodos acima

### Bloco 3 — Aplicação contextual

Pergunta central:

“Como o checkpoint validado entra no chat atual?”

Classificações permitidas:

- aplicação direta
- compatibilidade alta
- concatenação explícita
- deslocamento de eixo
- incompatibilidade relevante

### Bloco 4 — Material novo do chat atual

Pergunta central:

“O que surgiu no chat atual depois do checkpoint altera ou não altera o eixo salvo?”

Classificações permitidas:

- continuação direta
- complemento
- concatenação
- prospecção de ativo
- frente paralela
- divergência

## Regra crítica

Material novo do chat atual não invalida automaticamente o último checkpoint real.

Ele precisa ser classificado explicitamente.

## Regra de distinção entre checkpoint real e checkpoint mais próximo do assunto

A `CONTINUIDADE_VERIFICAVEL` deve distinguir com clareza:

### 1. Checkpoint real mais recente
Natureza:
- cronológica
- soberana para `quickloadF9`

### 2. Checkpoint mais próximo do assunto
Natureza:
- temática
- semântica
- relevante para navegação assistida
- não soberana por si só

### Regra derivada

- `quickloadF9` deve se orientar pelo checkpoint real mais recente
- `loadstateF9` assistido pode listar opções recentes
- `loadstateF9 <string>` pode listar checkpoints compatíveis com a pista textual
- afinidade temática não pode sequestrar soberania cronológica sem explicitação clara

## Relação com quickloadF9

`quickloadF9` governa a carga direta do último checkpoint real.

A `CONTINUIDADE_VERIFICAVEL` governa a prova de que esse checkpoint é realmente o último válido antes de a carga ser tratada como concluída.

### Regra crítica

Em `quickloadF9`, a exigência de prova cronológica é máxima.

## Relação com loadstateF9

`loadstateF9` governa carga assistida, listagem recente ou filtro textual.

A `CONTINUIDADE_VERIFICAVEL` governa:

- a integridade da listagem apresentada
- a distinção entre recência e afinidade
- a prova mínima antes da restauração final
- a separação entre navegação assistida e carga concluída

### Regra crítica

`loadstateF9` assistido não deve ser tratado como restauração concluída apenas porque exibiu opções coerentes.

## Ordem correta da continuidade

Quando a rotina de load exigir validação formal, a operação correta deve obedecer a esta ordem:

### 1. Identificar o modo de retomada

Determinar explicitamente se a rotina em curso é:

- carga direta
- carga assistida
- carga assistida por filtro textual

### 2. Localizar o checkpoint candidato

Identificar o checkpoint inicialmente compatível com o modo solicitado.

### 3. Validar a recência e a trilha

Acionar a `CONTINUIDADE_VERIFICAVEL` para provar:

- se o checkpoint é realmente o soberano
- se existe outro posterior
- se a listagem assistida está íntegra
- se a trilha usada para a prova é suficiente

### 4. Só depois avaliar a aplicação contextual

A análise do encaixe do checkpoint no chat atual só deve ocorrer depois da prova cronológica mínima.

### 5. Classificar o material novo do chat atual

Determinar se o que surgiu depois do checkpoint é:

- continuação
- complemento
- concatenação
- prospecção
- frente paralela
- divergência

### 6. Só então tratar a continuidade como concluída

A continuidade não deve ser apresentada como concluída enquanto recência, integridade da trilha e classificação contextual não tiverem sido suficientemente validadas.

## Regra crítica

É proibido inverter a ordem e aplicar contexto antes da prova cronológica.

## Saída auditável obrigatória

Nenhuma rotina de continuidade suficientemente sensível deve ser tratada como plenamente concluída sem emitir, de forma explícita ou estruturalmente equivalente, algo como:

```text
VERIFICACAO_DE_CONTINUIDADE
modo=
checkpoint_candidato=
checkpoint_confirmado=
fonte_de_verificacao=
pasta_canonica_consultada=
trilha_versionada_consultada=
ha_checkpoint_posterior_rastreavel=
classificacao_de_recencia=
classificacao_contextual=
material_novo_no_chat=
tratamento_do_material_novo=
estado_aplicado_como=
```

### Regra crítica

O usuário não deve precisar depender da própria memória recente para auditar se a continuidade foi corretamente estabelecida.

## Regra de rastreabilidade mínima da continuidade

Sempre que houver validação formal de continuidade, a operação deve deixar auditável, de forma suficiente:

- qual checkpoint foi considerado candidato
- qual checkpoint foi confirmado
- por que ele foi confirmado
- qual foi a fonte de verificação principal
- se houve consulta a caminho canônico
- se houve necessidade de trilha versionada
- se havia checkpoint posterior rastreável
- como o checkpoint entra no chat atual
- como o material novo do chat atual foi classificado

## Regra crítica

Continuidade sem prova mínima pode produzir confiança falsa.

## Critério de sucesso

Uma rotina de continuidade é considerada suficientemente segura quando:

- a recência foi corretamente classificada
- a fonte de verificação foi explicitada
- a aplicação contextual foi avaliada depois da prova cronológica
- o material novo do chat atual foi classificado
- a continuidade não dependeu apenas de plausibilidade
- a validação final não se apoiou apenas em busca ampla

## Critério de falha

Não considerar a continuidade suficientemente segura quando:

- o checkpoint foi assumido por coerência aparente
- a listagem assistida pode estar omitindo candidatos mais novos
- a aplicação contextual veio antes da prova cronológica
- o material novo do chat atual foi fundido silenciosamente ao eixo salvo
- a validação final se apoiou apenas em busca genérica quando havia caminho ou trilha verificável
- o usuário precisou corrigir com memória recente um erro que a própria rotina deveria detectar

## Relação com EVOLUCAO_MASTERS_SOBERANOS

A `CONTINUIDADE_VERIFICAVEL` não substitui `EVOLUCAO_MASTERS_SOBERANOS`.

A `EVOLUCAO_MASTERS_SOBERANOS` governa a transição documental de masters.  
A `CONTINUIDADE_VERIFICAVEL` governa a prova formal da continuidade de estados e checkpoints.

### Regra derivada

Ambas compartilham o princípio metodológico de rastreio assertivo por caminho exato, mas aplicam esse princípio em domínios diferentes.

## Relação com TGM

`TGM` governa o regime soberano.  
`CONTINUIDADE_VERIFICAVEL` protege a integridade da continuidade sob esse regime quando a retomada exigir prova formal.

## Relação com curadoria

A `CONTINUIDADE_VERIFICAVEL` não decide incorporação de ativo.

Mas pode classificar o material novo do chat atual como:
- complemento
- concatenação
- prospecção de ativo
- frente paralela
- divergência

Essa classificação não é curadoria plena.  
É apenas governança de continuidade.

## Formulação canônica da correção

Nenhuma rotina de continuidade do Cérebro Tendoshk deve ser tratada como concluída apenas por plausibilidade estrutural, afinidade semântica ou coerência aparente do checkpoint.

A prova de recência e integridade da retomada deve preceder qualquer aplicação contextual do estado ao chat.

Quando houver caminho canônico verificável, a validação da continuidade deve priorizar verificação determinística por caminho exato e trilha cronológica verificável, usando busca ampla apenas como apoio exploratório.

## Regra final

A `CONTINUIDADE_VERIFICAVEL` existe para impedir que o sistema pareça ter restabelecido continuidade correta quando apenas encontrou um checkpoint plausível.

Quando corretamente preservada, a continuidade não parece apenas convincente.  
Parece provada.

E essa diferença é parte da integridade do sistema.
