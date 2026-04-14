# Especificação Operacional do Módulo 4 — Continuidade e Retomada — V1

## 1. Natureza da peça
Este documento estabelece a especificação operacional do Módulo 4 do Cérebro Tendoshk na fase V1: **Continuidade e Retomada**.

Este módulo é o quarto da ordem oficial de implementação do Cérebro Tendoshk e existe para definir como o sistema preserva o fio do trabalho entre sessões, chats e mudanças de contexto, restaurando o ponto estrutural correto sem regressão, sem improviso e sem reconstrução manual excessiva.

Seu papel não é apenas “lembrar” o que aconteceu. Seu papel é sustentar a passagem ordenada entre estado salvo e trabalho vivo.

---

## 2. Lugar do módulo dentro da arquitetura
O Módulo 4 existe dentro do seguinte regime já estabilizado:
- o NPT é soberano;
- o Cérebro Tendoshk não substitui o NPT;
- o Cérebro Tendoshk opera como camada pré-ingestão;
- a Curadoria Provisória Persistente está ativa;
- o Módulo 1 já define a Curadoria em Tempo Real;
- o Módulo 2 já define a Leitura do NPT Soberano;
- o Módulo 3 já define a Decisão de Destino;
- o Bootstrap Operacional já define a constituição da retomada;
- o Checkpoint Operacional já define o save state da fase atual.

Dentro desse regime, Continuidade e Retomada é o elo que transforma documentação correta em reentrada operacional correta.

---

## 3. Missão central do módulo
A missão central do Módulo 4 é:

**garantir que o sistema consiga sair de um ponto salvo e retornar ao trabalho vivo no ponto estrutural correto, carregando regras permanentes, estado atual, travas, contexto suficiente e próximo passo natural, sem depender de reconstrução manual excessiva nem de memória difusa.**

Síntese funcional: o módulo existe para fazer a continuidade operar como sistema e não como esforço improvisado de reconstituição.

---

## 4. Problema que o módulo resolve
Sem Continuidade e Retomada, o sistema corre risco de:
- perder o ponto exato entre chats;
- reabrir fundamentos já estabilizados;
- retomar só o tema, mas não o estado do trabalho;
- esquecer travas e prioridades de fase;
- reconstruir manualmente o que já foi salvo em bootstrap e checkpoint;
- começar cada conversa relevante como se fosse quase do zero;
- desperdiçar energia cognitiva em reorientação repetitiva.

Logo, o módulo resolve o problema de **descontinuidade operacional entre estados salvos e fluxo vivo**.

---

## 5. Função operacional do módulo
A função operacional do módulo é restaurar continuidade suficiente para que o chat atual retome o trabalho do ponto certo.

Isso significa que ele deve ser capaz de:
1. reconhecer quando uma retomada é necessária;
2. identificar o que precisa ser restaurado do regime e da fase;
3. carregar bootstrap e checkpoint na proporção correta;
4. recolocar o chat no próximo passo natural sem reabrir base desnecessária;
5. proteger o estado salvo contra regressão e dispersão precoce.

---

## 6. Entradas do módulo
O Módulo 4 recebe como entrada:
- a ativação explícita do chat novo, quando houver;
- o bootstrap vigente;
- o checkpoint vigente;
- a leitura estrutural já feita pelos módulos anteriores;
- a demanda atual do usuário;
- o estado percebido de continuidade ou quebra de continuidade;
- o ponto mais recente do trabalho relevante para retomada.

Ele não recebe como missão adivinhar tudo. Ele recebe como missão restaurar o suficiente a partir das fontes corretas.

---

## 7. Saídas possíveis do módulo
As saídas possíveis do módulo são as seguintes:

### 7.1. Retomada plena
Quando o sistema consegue restaurar regime, estado salvo e próximo passo natural de forma suficiente.

### 7.2. Retomada parcial orientada
Quando parte do contexto está restaurada, mas ainda é necessário apoio complementar do chat em curso.

### 7.3. Correção de regressão
Quando a retomada começa a derivar para reabertura indevida de fundamentos ou perda do ponto salvo.

### 7.4. Reancoragem no checkpoint
Quando o fluxo atual precisa ser trazido de volta ao estado salvo vigente.

### 7.5. Atualização de checkpoint
Quando a retomada produziu alteração real do estado da fase e isso precisa ser salvo novamente.

---

## 8. Pergunta interna central do módulo
A pergunta interna permanente do Módulo 4 é:

**“o que precisa ser restaurado agora para que esta conversa volte ao ponto estrutural correto do trabalho, com regras, estado e direção suficientes, sem reconstrução manual desnecessária?”**

Essa pergunta impede dois erros:
- retomar de menos;
- retomar demais e reabrir o que já estava estabilizado.

Ela obriga o cérebro a restaurar com precisão.

---

## 9. Princípios da continuidade e retomada
Para fins operacionais da V1, a continuidade e retomada devem obedecer aos seguintes princípios:

### 9.1. Princípio da restauração suficiente
Deve-se restaurar o bastante para operar corretamente, não tudo indiscriminadamente.

### 9.2. Princípio do ponto estrutural
A retomada deve restaurar o ponto do trabalho, não só o assunto geral.

### 9.3. Princípio da precedência
Bootstrap e checkpoint têm precedência sobre lembrança vaga ou dedução frouxa.

### 9.4. Princípio da não regressão
A retomada não deve levar à reabertura de base já consolidada sem motivo estrutural forte.

### 9.5. Princípio da economia cognitiva
A continuidade deve reduzir custo mental do usuário, não aumentar.

---

## 10. Componentes mínimos de uma retomada correta
Na V1, uma retomada correta deve saber restaurar pelo menos os seguintes componentes:

### 10.1. Regime ativo
O conjunto de regras permanentes válidas para o chat.

### 10.2. Estado salvo da fase
O ponto atual, peças relevantes, travas, prioridades e próximo passo natural.

### 10.3. Ponto operacional do trabalho
O elo exato em que o projeto estava antes da interrupção.

### 10.4. Limites de fase
O que está congelado, em segundo plano ou proibido de reabrir sem razão forte.

### 10.5. Direção imediata
Qual é o próximo movimento correto depois da retomada.

---

## 11. Regra de retomada em chat novo
Quando a continuidade exigir chat novo, a retomada segura deve ocorrer por ativação explícita ligada ao bootstrap e ao checkpoint.

A lógica correta é:
- ativar o regime;
- carregar bootstrap;
- carregar checkpoint;
- restaurar o ponto estrutural;
- seguir do próximo passo natural.

Sem isso, a conversa corre risco de virar continuidade vaga.

---

## 12. Regra de retomada dentro do mesmo chat
Mesmo sem mudança de chat, a continuidade pode ser perdida por dispersão, regressão conceitual ou excesso de desvios.

Nesses casos, o módulo deve:
- reancorar no ponto estrutural atual;
- lembrar o próximo passo natural;
- reaplicar trava anti-dispersão quando necessário;
- impedir que o fluxo local invalide o estado salvo sem decisão explícita.

---

## 13. Relação com bootstrap
O bootstrap fornece a constituição operacional da retomada.

O Módulo 4 deve consultá-lo quando a continuidade depender de:
- regras permanentes do regime;
- precedência documental;
- ativação correta;
- separação entre camadas;
- governança da retomada.

Sem bootstrap, a retomada pode até parecer funcional, mas tende a ficar conceitualmente frouxa.

---

## 14. Relação com checkpoint
O checkpoint fornece o save state da fase.

O Módulo 4 deve consultá-lo quando a continuidade depender de:
- ponto exato do projeto;
- peças relevantes ativas;
- travas vigentes;
- temas em segundo plano;
- próximo passo natural.

Sem checkpoint, a retomada pode lembrar o regime, mas não o estado concreto do trabalho.

---

## 15. Relação com os módulos anteriores
A relação entre os quatro módulos é a seguinte:

- o Módulo 1 percebe o que surge no presente;
- o Módulo 2 consulta a base soberana quando necessário;
- o Módulo 3 decide o destino operacional;
- o Módulo 4 garante que o sistema consiga retomar corretamente do ponto salvo para continuar operando.

Síntese:
Módulo 1 percebe.  
Módulo 2 ancora.  
Módulo 3 encaminha.  
Módulo 4 retoma.

---

## 16. Regra de restauração do próximo passo natural
Uma retomada funcional não deve parar só na restauração do contexto.

Ela deve também restaurar o **próximo passo natural**.

Isso significa que, ao final de uma retomada correta, o sistema deve conseguir responder com clareza:
- onde estamos;
- o que já está estabilizado;
- o que não deve ser reaberto;
- qual é o próximo passo correto.

Sem isso, a retomada permanece incompleta.

---

## 17. Regra de prevenção de falsa continuidade
O Módulo 4 deve proteger contra a ilusão de continuidade.

Fica vedado tratar como retomada suficiente uma situação em que:
- só o tema geral foi lembrado;
- as regras permanentes não foram restauradas;
- o checkpoint não foi considerado;
- o próximo passo natural ficou indefinido;
- o fluxo atual voltou a discutir fundamento já estabilizado.

Falsa continuidade é continuidade aparente, mas operacionalmente fraca.

---

## 18. Regra de saída para o fluxo do chat
Ao operar continuidade e retomada, o módulo deve devolver ao fluxo do chat uma orientação clara e operacional.

Ele deve conseguir explicitar, de forma enxuta:
- qual regime foi restaurado;
- qual estado salvo foi carregado;
- em que ponto o projeto está;
- qual é o próximo passo natural.

Ele não deve transformar a retomada em longa reconstituição desnecessária quando a restauração já estiver suficiente.

---

## 19. Limites da V1
Na V1, o Módulo 4 deve fazer bem o essencial:
- reconhecer necessidade de retomada;
- carregar bootstrap e checkpoint adequados;
- restaurar ponto estrutural suficiente;
- impedir regressão;
- recolocar o sistema no próximo passo natural.

A V1 não precisa ainda:
- múltiplos estados paralelos sofisticados;
- orquestração complexa entre muitas fases simultâneas;
- automações pesadas de sincronização;
- mecanismos futuristas além do necessário para continuidade operacional robusta.

A regra da fase permanece:
**fazer o eixo mínimo operar com estabilidade antes de sofisticar o sistema.**

---

## 20. Critério de sucesso do módulo
O Módulo 4 será considerado funcionalmente bem-sucedido quando conseguir, de modo consistente:
- reduzir sensação de recomeço desnecessário;
- restaurar rapidamente o ponto estrutural do trabalho;
- preservar travas, prioridades e próximo passo natural;
- impedir regressão conceitual entre chats;
- reduzir o custo mental da retomada para o usuário.

---

## 21. Formulação canônica do módulo
Formulação oficial resumida:

**O Módulo 4 — Continuidade e Retomada — é o mecanismo do Cérebro Tendoshk responsável por restaurar, a partir das fontes corretas, o regime ativo, o estado salvo da fase e o próximo passo natural do trabalho, garantindo que a passagem entre interrupção e continuidade ocorra sem regressão, sem improviso e sem reconstrução manual excessiva.**

---

## 22. Síntese final
Síntese canônica desta peça:

Não basta ter regra.  
Não basta ter save.  
É preciso conseguir voltar corretamente.

E, na V1, isso significa:  
restaurar o regime,  
restaurar o estado,  
restaurar o ponto,  
restaurar a direção,  
e seguir sem regressão.
