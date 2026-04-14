# Especificação Operacional do Módulo 5 — Guardião de Coerência — V1

## 1. Natureza da peça
Este documento estabelece a especificação operacional do Módulo 5 do Cérebro Tendoshk na fase V1: **Guardião de Coerência**.

Este módulo é o quinto da ordem oficial de implementação do Cérebro Tendoshk e existe para definir como o sistema protege sua integridade conceitual, documental e operacional ao longo do tempo, evitando contradição entre peças, regressão de regime, conflito entre camadas e proliferação de decisões incompatíveis.

Seu papel não é burocratizar o fluxo. Seu papel é garantir que o sistema continue sendo o mesmo sistema mesmo quando cresce, muda de chat, cria novas peças e atualiza sua própria arquitetura.

---

## 2. Lugar do módulo dentro da arquitetura
O Módulo 5 existe dentro do seguinte regime já estabilizado:
- o NPT é soberano;
- o Cérebro Tendoshk não substitui o NPT;
- o Cérebro Tendoshk opera como camada pré-ingestão;
- a Curadoria Provisória Persistente está ativa;
- o Módulo 1 já define a Curadoria em Tempo Real;
- o Módulo 2 já define a Leitura do NPT Soberano;
- o Módulo 3 já define a Decisão de Destino;
- o Módulo 4 já define Continuidade e Retomada;
- o Bootstrap Operacional já define a constituição da retomada;
- o Checkpoint Operacional já define o save state da fase atual.

Dentro desse regime, o Guardião de Coerência é o elo que impede que a própria evolução do sistema destrua sua consistência interna.

---

## 3. Missão central do módulo
A missão central do Módulo 5 é:

**proteger a coerência do sistema ao longo do tempo, verificando se novas formulações, novas peças, novas decisões e novas retomadas permanecem compatíveis com o regime soberano já estabelecido, com a separação entre camadas e com a identidade estrutural do próprio Cérebro Tendoshk.**

Síntese funcional: o módulo existe para impedir que crescimento vire incoerência.

---

## 4. Problema que o módulo resolve
Sem Guardião de Coerência, o sistema corre risco de:
- criar peças que contradizem regras já aprovadas;
- regredir para fluxos que o próprio sistema já tinha corrigido;
- misturar camadas documentais novamente;
- aceitar deriva conceitual entre chats;
- atualizar bootstrap, checkpoint ou peças específicas de modo incompatível;
- crescer em volume, mas perder identidade operacional;
- transformar evolução em fragmentação.

Logo, o módulo resolve o problema de **inconsistência acumulativa do sistema**.

---

## 5. Função operacional do módulo
A função operacional do módulo é atuar como verificador estrutural de compatibilidade antes, durante e depois de mudanças relevantes no sistema.

Isso significa que ele deve ser capaz de:
1. comparar novas formulações com o regime vigente;
2. detectar contradições, colisões ou regressões;
3. sinalizar quando uma mudança exige atualização de bootstrap ou checkpoint;
4. impedir que exceções locais virem desordem sistêmica;
5. proteger a identidade operacional do cérebro ao longo do tempo.

---

## 6. Entradas do módulo
O Módulo 5 recebe como entrada:
- peças estruturais novas ou revisadas;
- mudanças de regra permanente;
- mudanças de checkpoint;
- decisões de destino relevantes;
- sinais de conflito entre documentos;
- retomadas em chat novo com risco de divergência;
- a arquitetura documental vigente do sistema;
- o bootstrap e o checkpoint ativos.

Ele não recebe como missão criar novidade. Ele recebe como missão testar se a novidade cabe no sistema sem quebrá-lo.

---

## 7. Saídas possíveis do módulo
As saídas possíveis do módulo são as seguintes:

### 7.1. Compatibilidade confirmada
Quando a nova peça ou decisão é coerente com o sistema vigente.

### 7.2. Incompatibilidade detectada
Quando há contradição com regra, precedência, separação de camadas ou identidade operacional do sistema.

### 7.3. Ajuste localizado
Quando a incoerência pode ser corrigida sem alterar o regime geral.

### 7.4. Necessidade de atualização estrutural
Quando a mudança é válida, mas exige atualização explícita de bootstrap, checkpoint ou peça específica.

### 7.5. Bloqueio de regressão
Quando a mudança tentaria reabrir erro já corrigido ou reinstalar lógica inadequada.

---

## 8. Pergunta interna central do módulo
A pergunta interna permanente do Módulo 5 é:

**“isso que está sendo proposto, decidido ou criado permanece coerente com o sistema já estabilizado, ou está introduzindo contradição, regressão ou colisão que precisa ser contida?”**

Essa pergunta impede dois erros:
- aceitar toda novidade como progresso;
- congelar o sistema sem permitir evolução legítima.

Ela obriga o cérebro a evoluir com consistência.

---

## 9. Princípios do guardião de coerência
Para fins operacionais da V1, o Guardião de Coerência deve obedecer aos seguintes princípios:

### 9.1. Princípio da identidade sistêmica
O sistema deve continuar reconhecível para si mesmo ao longo de sua evolução.

### 9.2. Princípio da não contradição
Peças novas não devem contradizer regras soberanas sem atualização explícita do regime.

### 9.3. Princípio da separação preservada
Mudanças novas não devem reintroduzir colisão entre integral, consolidado, checkpoint e repo.

### 9.4. Princípio da evolução legítima
O sistema pode mudar, desde que a mudança seja explicitada, compatibilizada e registrada corretamente.

### 9.5. Princípio da rastreabilidade de conflito
Quando houver tensão entre documentos, a incompatibilidade deve ser nomeada com clareza e não mascarada.

---

## 10. Tipos de coerência que o módulo deve proteger
Na V1, o módulo deve proteger pelo menos os seguintes tipos de coerência:

### 10.1. Coerência de regime
Compatibilidade com bootstrap, precedência e governança.

### 10.2. Coerência de fase
Compatibilidade com checkpoint, travas, prioridades e próximo passo natural.

### 10.3. Coerência documental
Compatibilidade entre peças integrais, NPT_ENTRYs, consolidado e repo.

### 10.4. Coerência operacional
Compatibilidade entre o que o sistema diz que faz e o que ele realmente faz.

### 10.5. Coerência evolutiva
Compatibilidade entre crescimento do sistema e sua identidade estrutural.

---

## 11. Critérios para acionar o guardião de coerência
Na V1, o módulo deve ser acionado quando houver, entre outros casos:
- criação de nova peça estrutural;
- revisão de peça já existente;
- atualização de bootstrap;
- atualização de checkpoint;
- dúvida sobre se uma exceção local é aceitável;
- suspeita de contradição entre duas peças;
- reintrodução de erro já corrigido;
- mudança de destino documental relevante.

Quando não houver risco estrutural nem mudança relevante, o acionamento explícito pode não ser necessário.

---

## 12. Regra de verificação mínima suficiente
O Módulo 5 não deve transformar toda decisão em auditoria pesada.

A regra correta é:
- verificar a menor superfície suficiente de conflito;
- testar compatibilidade com regime, fase e separação de camadas;
- sinalizar incoerência ou confirmar compatibilidade;
- devolver o resultado ao fluxo do chat de forma útil.

Isso protege contra burocratização sem perder rigor.

---

## 13. Relação com bootstrap e checkpoint
O Módulo 5 deve tratar bootstrap e checkpoint como seus dois referenciais principais de verificação.

### 13.1. Bootstrap
Deve ser consultado quando houver risco de contradição com regra permanente, precedência, ativação, separação entre camadas ou governança soberana.

### 13.2. Checkpoint
Deve ser consultado quando houver risco de desvio do estado atual da fase, do próximo passo natural, das travas vigentes ou dos limites de fase.

Sem esses dois referenciais, a verificação tende a ficar frouxa ou arbitrária.

---

## 14. Relação com os módulos anteriores
A relação entre os cinco módulos é a seguinte:

- o Módulo 1 percebe o presente;
- o Módulo 2 consulta a base soberana;
- o Módulo 3 decide o destino;
- o Módulo 4 restaura a continuidade;
- o Módulo 5 verifica se tudo isso permanece coerente com o sistema ao longo do tempo.

Síntese:
Módulo 1 percebe.  
Módulo 2 ancora.  
Módulo 3 encaminha.  
Módulo 4 retoma.  
Módulo 5 protege a coerência.

---

## 15. Regra de bloqueio de regressão estrutural
O Módulo 5 deve possuir autoridade funcional para bloquear regressões já conhecidas.

Fica vedado permitir o retorno, sem justificativa estrutural explícita, de práticas como:
- apontar NPT_ENTRY para o mesmo destino do ativo integral;
- usar `conteudo=` como substituto de documento completo;
- tratar repo como origem canônica da peça;
- reabrir fundamentos já estabilizados por simples esquecimento de continuidade;
- relativizar a soberania do NPT ou a separação entre camadas.

Essa trava é uma das funções centrais do módulo.

---

## 16. Regra de evolução compatível
Quando uma mudança legítima exigir alteração do sistema, o módulo não deve tratá-la como incoerência por padrão.

A regra correta é:
- distinguir evolução legítima de contradição desordenada;
- identificar qual peça precisa ser atualizada;
- garantir que a mudança seja explicitada e registrada no nível correto.

Isso impede que a coerência vire rigidez cega.

---

## 17. Regra de saída para o fluxo do chat
Ao operar como guardião de coerência, o módulo deve devolver ao fluxo do chat uma leitura clara e operacional.

Ele deve conseguir explicitar, de forma enxuta:
- o que está coerente;
- o que está em conflito;
- o que precisa ser ajustado;
- se a mudança exige atualização estrutural ou apenas correção local.

Ele não deve esconder conflito real atrás de formulação vaga.

---

## 18. Limites da V1
Na V1, o Módulo 5 deve fazer bem o essencial:
- detectar contradição relevante;
- proteger separação entre camadas;
- bloquear regressão estrutural;
- permitir evolução legítima com atualização explícita;
- preservar identidade operacional do sistema.

A V1 não precisa ainda:
- mecanismos formais complexos de validação automática;
- malhas sofisticadas de auditoria multi-documental;
- sistemas avançados de diff semântico;
- automações pesadas de consistência.

A regra da fase permanece:
**fazer o eixo mínimo operar com estabilidade antes de sofisticar o sistema.**

---

## 19. Critério de sucesso do módulo
O Módulo 5 será considerado funcionalmente bem-sucedido quando conseguir, de modo consistente:
- reduzir contradições entre peças;
- impedir regressões já corrigidas;
- manter compatibilidade entre bootstrap, checkpoint, documentos integrais e consolidado;
- permitir crescimento do sistema sem perda de identidade;
- tornar conflitos estruturais visíveis antes que virem retrabalho maior.

---

## 20. Formulação canônica do módulo
Formulação oficial resumida:

**O Módulo 5 — Guardião de Coerência — é o mecanismo do Cérebro Tendoshk responsável por verificar se novas decisões, novas peças, novas retomadas e novas evoluções permanecem compatíveis com o regime soberano do sistema, protegendo identidade operacional, separação entre camadas e continuidade sem contradição acumulativa.**

---

## 21. Síntese final
Síntese canônica desta peça:

Não basta crescer.  
Não basta organizar.  
É preciso continuar coerente.

E, na V1, isso significa:  
comparar com o regime,  
detectar conflito,  
impedir regressão,  
permitir evolução legítima,  
e preservar a identidade do sistema.
