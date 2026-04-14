# Especificação Operacional do Módulo 2 — Leitura do NPT Soberano — V1

## 1. Natureza da peça
Este documento estabelece a especificação operacional do Módulo 2 do Cérebro Tendoshk na fase V1: **Leitura do NPT Soberano**.

Este módulo é o segundo da ordem oficial de implementação do Cérebro Tendoshk e existe para definir como o cérebro consulta, respeita e utiliza o NPT sem substituir sua soberania.

Seu papel não é transformar o cérebro em banco de memória concorrente ao NPT. Seu papel é tornar a consulta ao NPT funcional, disciplinada e útil para continuidade, curadoria e decisão de destino.

---

## 2. Lugar do módulo dentro da arquitetura
O Módulo 2 existe dentro do seguinte regime já estabilizado:
- o NPT é soberano;
- o Cérebro Tendoshk não substitui o NPT;
- o Cérebro Tendoshk opera como camada pré-ingestão;
- a Curadoria Provisória Persistente está ativa;
- o Módulo 1 já define a Curadoria em Tempo Real;
- o Bootstrap Operacional já define a constituição da retomada;
- o Checkpoint Operacional já define o save state da fase atual.

Dentro desse regime, a Leitura do NPT Soberano é o elo que permite ao cérebro consultar a memória canônica do sistema antes de decidir continuidade, consolidação ou destino.

---

## 3. Missão central do módulo
A missão central do Módulo 2 é:

**ler o NPT soberano de forma disciplinada, suficiente e subordinada à sua função canônica, para que o cérebro possa orientar a continuidade do chat sem reinventar contexto, sem competir com a memória canônica e sem corromper a separação entre leitura, curadoria e registro.**

Síntese funcional: o módulo existe para transformar o NPT em referência consultada corretamente e não em pano de fundo vago.

---

## 4. Problema que o módulo resolve
Sem Leitura do NPT Soberano, o sistema corre risco de:
- depender demais de memória implícita do chat;
- reabrir decisões já consolidadas;
- perder precedência documental;
- reconstruir manualmente o que já estava salvo;
- responder com profundidade, mas sem base canônica suficiente;
- confundir contexto momentâneo com verdade estrutural;
- gerar continuidade fraca entre chats.

Logo, o módulo resolve o problema de **descontinuidade por ausência de consulta soberana**.

Ele não existe para aumentar burocracia. Existe para impedir regressão operacional.

---

## 5. Função operacional do módulo
A função operacional do módulo é consultar o NPT quando a continuidade do trabalho depender de base estrutural já registrada.

Isso significa que ele deve ser capaz de:
1. reconhecer quando o chat exige consulta ao NPT;
2. identificar qual camada do NPT é relevante para a demanda;
3. ler a fonte soberana suficiente para restaurar contexto estrutural;
4. distinguir regra permanente de estado atual;
5. devolver essa leitura ao fluxo do chat sem duplicar nem substituir o NPT.

---

## 6. Entradas do módulo
O Módulo 2 recebe como entrada:
- a demanda atual do usuário;
- o regime ativo do chat;
- a necessidade percebida de retomada, validação estrutural ou continuidade;
- checkpoints operacionais válidos;
- peças estruturais já aprovadas;
- o próprio NPT como fonte soberana consultável;
- a arquitetura documental vigente do sistema.

Ele não recebe como missão inventar contexto. Ele recebe como missão consultar contexto canônico quando necessário.

---

## 7. Saídas possíveis do módulo
As saídas possíveis do módulo são as seguintes:

### 7.1. Restauração de contexto estrutural
Quando o NPT oferece base suficiente para recolocar o chat no ponto certo.

### 7.2. Confirmação de precedência
Quando a leitura do NPT confirma que determinada regra, peça ou checkpoint já está consolidado.

### 7.3. Correção de deriva
Quando a leitura mostra que o chat começou a se afastar do regime já aprovado.

### 7.4. Preparação de continuidade
Quando a consulta ao NPT permite seguir do ponto certo sem reabrir base.

### 7.5. Sinalização de insuficiência
Quando a leitura do NPT não for suficiente sozinha e exigir complemento contextual do chat atual ou novo checkpoint.

---

## 8. Pergunta interna central do módulo
A pergunta interna permanente do Módulo 2 é:

**“qual fonte soberana do NPT precisa ser lida agora para que a continuidade desta conversa se apoie no que já foi decidido, e não em lembrança difusa ou reconstrução manual?”**

Essa pergunta impede dois erros:
- consultar o NPT de menos;
- consultar o NPT de forma excessiva e sem foco.

Ela obriga o cérebro a ler com finalidade.

---

## 9. Princípios de leitura soberana
Para fins operacionais da V1, a leitura do NPT deve obedecer aos seguintes princípios:

### 9.1. Princípio da soberania
O NPT é fonte canônica; o cérebro é leitor e preparador de destino.

### 9.2. Princípio da suficiência
Deve-se ler o suficiente para restaurar coerência, não tudo indiscriminadamente.

### 9.3. Princípio da precedência
Quando houver conflito entre lembrança implícita e registro canônico, prevalece o registro canônico do regime.

### 9.4. Princípio da não concorrência
A leitura do NPT não autoriza o cérebro a criar memória paralela concorrente.

### 9.5. Princípio da utilidade operacional
Toda leitura deve servir a uma decisão, retomada, validação ou correção concreta no fluxo do chat.

---

## 10. Camadas do NPT que o módulo deve saber distinguir
Na V1, o módulo deve distinguir pelo menos as seguintes camadas documentais:

### 10.1. Bootstrap
Regras permanentes do regime.

### 10.2. Checkpoint
Estado salvo atual da fase.

### 10.3. Peças estruturais integrais
Documentos canônicos completos em `ativos/contratos/`.

### 10.4. Consolidados
Memória viva cumulativa por projeto, especialmente `consolidados/npt_nucleo_persistente_tendoshk.md` para o núcleo do cérebro.

### 10.5. Fichas e materiais de projeto
Quando houver necessidade de leitura da camada `projetos/`.

A função do módulo é saber qual camada consultar conforme a natureza da demanda.

---

## 11. Critérios para acionar leitura do NPT
Na V1, o módulo deve acionar leitura do NPT quando houver, entre outros casos:
- retomada em chat novo;
- necessidade de confirmar ponto estrutural já definido;
- risco de reabrir fundamento estabilizado;
- dúvida sobre precedência entre peças;
- necessidade de recuperar o próximo passo natural;
- necessidade de verificar destino ou governança já registrados;
- necessidade de restaurar contexto canônico antes de produzir nova peça.

Quando a demanda for puramente local e presente, sem depender de base anterior, a leitura do NPT pode não ser necessária.

---

## 12. Regra de leitura mínima suficiente
O Módulo 2 não deve operar em modo de varredura indiscriminada.

A regra correta é:
- localizar a camada relevante;
- ler a menor porção suficiente para restaurar base;
- devolver a leitura ao fluxo do chat;
- seguir para curadoria, decisão ou produção.

Essa regra protege contra fadiga operacional e contra pseudo-sofisticação desnecessária.

---

## 13. Relação com o Módulo 1
A relação entre os dois módulos é complementar:

- o Módulo 1 lê o presente do chat e distingue estrutural de derivado;
- o Módulo 2 lê o NPT soberano para dar base canônica à continuidade;
- o Módulo 1 decide prioridade e destino no fluxo vivo;
- o Módulo 2 impede que essa decisão aconteça desconectada do que já foi consolidado.

Síntese:
Módulo 1 percebe.  
Módulo 2 confirma e ancora.

---

## 14. Relação com o bootstrap e com o checkpoint
O Módulo 2 deve tratar bootstrap e checkpoint como as duas primeiras leituras de precedência quando a demanda for de retomada.

### 14.1. Bootstrap
Deve ser consultado quando a dúvida for sobre regras permanentes, separação de camadas, ativação, precedência e governança.

### 14.2. Checkpoint
Deve ser consultado quando a dúvida for sobre estado atual da fase, peças relevantes ativas, travas, ponto do projeto e próximo passo natural.

Em retomadas de chat novo, a leitura correta tende a começar por essas duas peças.

---

## 15. Relação com consolidados e documentos integrais
Quando a necessidade for sobre memória viva acumulada, evolução do núcleo ou registro sintético cumulativo, o módulo deve consultar os consolidados.

Quando a necessidade for sobre formulação oficial completa de peça específica, o módulo deve consultar o documento integral correspondente em `ativos/contratos/`.

Isso impede dois erros:
- buscar detalhe integral em consolidado;
- buscar resumo de continuidade em documento integral sem necessidade.

---

## 16. Regra de saída para o chat
Ao utilizar o NPT como base, o módulo deve devolver ao fluxo do chat uma leitura útil, clara e operacional.

Ele não deve:
- despejar o NPT inteiro no chat;
- agir como se estivesse citando um arquivo por vaidade;
- inflar a resposta só porque houve leitura estrutural.

Ele deve:
- restaurar o contexto certo;
- indicar o ponto de continuidade;
- confirmar o que está estabilizado;
- ajudar a seguir sem regressão.

---

## 17. Limites da V1
Na V1, o Módulo 2 deve fazer bem o essencial:
- reconhecer quando a leitura do NPT é necessária;
- distinguir qual camada consultar;
- restaurar base canônica suficiente;
- devolver essa base ao fluxo do chat de modo útil;
- proteger precedência e continuidade.

A V1 não precisa ainda:
- leitura semântica complexa multi-arquivo em larga escala;
- painéis avançados;
- busca transversal sofisticada;
- automações pesadas;
- interpretação futurista além do necessário para continuidade operacional.

A regra da fase permanece:
**fazer o eixo mínimo operar com estabilidade antes de sofisticar o sistema.**

---

## 18. Critério de sucesso do módulo
O Módulo 2 será considerado funcionalmente bem-sucedido quando conseguir, de modo consistente:
- reduzir retomadas vagas;
- restaurar rapidamente contexto estrutural em chats novos;
- impedir reabertura desnecessária de fundamentos;
- ancorar novas decisões no que já foi consolidado;
- melhorar a qualidade da continuidade entre chats;
- fortalecer a soberania prática do NPT sem transformar o cérebro em concorrente do próprio NPT.

---

## 19. Formulação canônica do módulo
Formulação oficial resumida:

**O Módulo 2 — Leitura do NPT Soberano — é o mecanismo do Cérebro Tendoshk responsável por consultar a memória canônica do sistema de forma disciplinada, suficiente e útil, para restaurar contexto estrutural, preservar precedência documental e sustentar continuidade sem substituir o NPT nem criar memória paralela concorrente.**

---

## 20. Síntese final
Síntese canônica desta peça:

O cérebro não deve lembrar “de qualquer jeito”.  
Ele deve consultar a fonte certa, da forma certa, no momento certo.

E, na V1, isso significa:  
reconhecer quando ler,  
escolher o que ler,  
ler o suficiente,  
restaurar o contexto,  
e voltar ao fluxo com base canônica.
