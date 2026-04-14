# Especificação Operacional do Módulo 3 — Decisão de Destino — V1

## 1. Natureza da peça
Este documento estabelece a especificação operacional do Módulo 3 do Cérebro Tendoshk na fase V1: **Decisão de Destino**.

Este módulo é o terceiro da ordem oficial de implementação do Cérebro Tendoshk e existe para definir como o cérebro decide o encaminhamento correto do que surge no fluxo dos chats após a leitura estrutural do presente e a consulta ao NPT soberano.

Seu papel não é apenas classificar ideias de modo abstrato. Seu papel é decidir o destino operacional correto daquilo que emerge, evitando dispersão, colisão documental, retrabalho e perda de valor estrutural.

---

## 2. Lugar do módulo dentro da arquitetura
O Módulo 3 existe dentro do seguinte regime já estabilizado:
- o NPT é soberano;
- o Cérebro Tendoshk não substitui o NPT;
- o Cérebro Tendoshk opera como camada pré-ingestão;
- a Curadoria Provisória Persistente está ativa;
- o Módulo 1 já define a Curadoria em Tempo Real;
- o Módulo 2 já define a Leitura do NPT Soberano;
- o Bootstrap Operacional já define a constituição da retomada;
- o Checkpoint Operacional já define o save state da fase atual.

Dentro desse regime, a Decisão de Destino é o elo que transforma percepção e leitura em encaminhamento concreto.

---

## 3. Missão central do módulo
A missão central do Módulo 3 é:

**decidir, com base estrutural e operacional, para onde cada conteúdo relevante deve ir dentro do sistema, distinguindo entre permanência no fluxo do chat, registro consolidado, peça integral, checkpoint, atualização do bootstrap, espelhamento em repositório ou simples contenção sem expansão.**

Síntese funcional: o módulo existe para impedir que valor estrutural fique sem destino e que conteúdos de naturezas diferentes disputem o mesmo lugar.

---

## 4. Problema que o módulo resolve
Sem Decisão de Destino, o sistema corre risco de:
- gerar boas formulações sem encaminhamento correto;
- registrar no lugar errado;
- duplicar ou sobrescrever peças;
- confundir consolidado com ativo integral;
- inflar checkpoint com conteúdo que não pertence a ele;
- transformar tudo em documento ou deixar tudo solto demais;
- perder continuidade por falta de organização do que surgiu.

Logo, o módulo resolve o problema de **encaminhamento incorreto ou ausente do valor estrutural**.

---

## 5. Função operacional do módulo
A função operacional do módulo é decidir o destino do conteúdo após a curadoria do presente e, quando necessário, após a leitura do NPT soberano.

Isso significa que ele deve ser capaz de:
1. reconhecer a natureza operacional do conteúdo;
2. avaliar se o conteúdo deve permanecer local ou persistir;
3. distinguir o tipo de persistência adequado;
4. evitar colisão entre camadas documentais;
5. preparar o encaminhamento correto para NPT, Drive, checkpoint ou repo.

---

## 6. Entradas do módulo
O Módulo 3 recebe como entrada:
- a leitura estrutural do Módulo 1;
- a leitura soberana do Módulo 2, quando necessária;
- a demanda atual do usuário;
- o regime ativo do chat;
- a arquitetura documental vigente;
- a distinção entre ativo integral, consolidado, checkpoint e repo;
- sinais de valor estrutural, valor local, risco de dispersão ou necessidade de persistência.

Ele não recebe como missão salvar tudo. Ele recebe como missão decidir corretamente o que persiste, onde persiste e o que não deve ser persistido agora.

---

## 7. Saídas possíveis do módulo
As saídas possíveis do módulo são as seguintes:

### 7.1. Permanência no fluxo do chat
Quando o conteúdo é útil ao trabalho presente, mas ainda não atingiu massa crítica para registro persistente.

### 7.2. Registro consolidado
Quando o conteúdo deve entrar como memória viva, sintética e cumulativa no NPT.

### 7.3. Peça integral
Quando o conteúdo já exige documento oficial completo e canônico.

### 7.4. Atualização de checkpoint
Quando o conteúdo altera o estado salvo da fase, o próximo passo natural, as travas ou o ponto exato do projeto.

### 7.5. Atualização do bootstrap
Quando o conteúdo cria ou altera uma regra permanente do regime.

### 7.6. Espelhamento em repo
Quando já existe ativo integral e ele deve ser espelhado no GitHub sob o rito contextual correto.

### 7.7. Registro e retorno
Quando o conteúdo tem valor, mas não deve abrir nova frente agora.

---

## 8. Pergunta interna central do módulo
A pergunta interna permanente do Módulo 3 é:

**“qual é o destino correto deste conteúdo dentro do sistema, considerando sua natureza, seu peso estrutural, seu efeito operacional e a separação entre camadas?”**

Essa pergunta impede dois erros:
- salvar tudo;
- deixar sem destino o que já deveria ter persistência.

Ela obriga o cérebro a decidir com critério.

---

## 9. Princípios da decisão de destino
Para fins operacionais da V1, a decisão de destino deve obedecer aos seguintes princípios:

### 9.1. Princípio da adequação
Cada conteúdo deve ir para a camada compatível com sua natureza.

### 9.2. Princípio da não colisão
Conteúdos de naturezas diferentes não devem disputar o mesmo destino lógico.

### 9.3. Princípio da suficiência
Deve-se persistir o necessário, não tudo.

### 9.4. Princípio da rastreabilidade
Quando algo estrutural persistir, seu encaminhamento deve ser legível e auditável.

### 9.5. Princípio da continuidade
A decisão de destino deve fortalecer a continuidade futura e não só organizar o presente.

---

## 10. Tipos principais de destino na V1
Na V1, o módulo deve saber distinguir pelo menos os seguintes destinos:

### 10.1. Fluxo local do chat
Para conteúdo útil, mas ainda não persistente.

### 10.2. Consolidado do núcleo
Para registro sintético, cumulativo e vivo em `consolidados/npt_nucleo_persistente_tendoshk.md`.

### 10.3. Ativo integral em Drive
Para peças canônicas completas em `ativos/contratos/`.

### 10.4. Checkpoint operacional
Para alteração do estado salvo da fase.

### 10.5. Bootstrap operacional
Para alteração de regra permanente do regime.

### 10.6. Repositório GitHub
Para espelhamento versionado do ativo integral em `docs/`.

A função do módulo é escolher corretamente entre esses destinos e não misturá-los.

---

## 11. Critérios de decisão de destino
Na V1, o módulo deve considerar pelo menos os seguintes critérios:

### 11.1. Peso estrutural
O conteúdo altera governança, continuidade, prioridade, arquitetura ou regra?

### 11.2. Escopo de validade
O conteúdo vale apenas para o chat atual ou para o sistema como um todo?

### 11.3. Grau de estabilidade
O conteúdo já está maduro o bastante para peça integral ou ainda está em consolidação?

### 11.4. Tipo de efeito
O conteúdo altera regra permanente, estado atual, memória viva ou apenas o fluxo local?

### 11.5. Risco de retrabalho
Deixar sem persistência ou persistir no lugar errado vai gerar perda, duplicação ou colisão?

---

## 12. Regra de decisão para peça integral
O conteúdo deve virar peça integral quando:
- já possui massa estrutural suficiente;
- merece formulação oficial completa;
- precisa existir como referência estável futura;
- não cabe mais como simples observação consolidada;
- sua ausência como documento completo geraria fragilidade operacional.

Nesses casos, o destino padrão do ativo integral do núcleo do cérebro é `ativos/contratos/`.

---

## 13. Regra de decisão para consolidado
O conteúdo deve ir para o consolidado quando:
- precisa persistir como memória viva do núcleo;
- tem implicação estrutural ou histórica relevante;
- não exige necessariamente documento integral próprio;
- deve ser acumulado de forma sintética e cumulativa.

Para o núcleo do cérebro, o destino padrão é `consolidados/npt_nucleo_persistente_tendoshk.md`.

O consolidado não substitui a peça integral.

---

## 14. Regra de decisão para checkpoint
O conteúdo deve atualizar o checkpoint quando:
- altera o ponto exato do projeto;
- muda o próximo passo natural;
- muda o que está congelado ou em segundo plano;
- adiciona trava importante;
- redefine o estado salvo da fase.

O checkpoint não deve receber regra permanente que pertença ao bootstrap, nem documento integral que pertença a outra camada.

---

## 15. Regra de decisão para bootstrap
O conteúdo deve atualizar o bootstrap quando:
- cria regra permanente do regime;
- altera precedência documental;
- redefine a separação entre camadas;
- muda a forma soberana de retomada, curadoria ou governança do sistema.

O bootstrap não deve ser atualizado por mudanças apenas circunstanciais da fase atual.

---

## 16. Regra de decisão para repo
O conteúdo deve seguir para repo quando:
- já existe como ativo integral;
- o espelhamento versionado é desejado;
- o rito contextual do repositório no chat atual foi satisfeito.

A decisão de repo é subordinada à existência do ativo integral. O repo espelha a peça; ele não é a origem canônica da peça.

---

## 17. Relação com os módulos anteriores
A relação entre os três módulos é a seguinte:

- o Módulo 1 percebe e qualifica o que surgiu no presente;
- o Módulo 2 consulta a base soberana quando necessário;
- o Módulo 3 decide o destino operacional correto do que foi percebido e lido.

Síntese:
Módulo 1 percebe.  
Módulo 2 ancora.  
Módulo 3 encaminha.

---

## 18. Regra de prevenção de colisão documental
O Módulo 3 deve proteger explicitamente contra colisão entre camadas.

Fica vedado:
- usar NPT_ENTRY para recriar documento integral;
- apontar o registro consolidado para o mesmo arquivo do ativo integral;
- tratar checkpoint como arquivo de peça estrutural completa;
- tratar repo como consolidado;
- usar `conteudo=` de NPT_ENTRY como substituto do ativo canônico.

Essa trava é parte central da função do módulo.

---

## 19. Regra de saída para o fluxo do chat
Ao decidir o destino, o módulo deve devolver ao fluxo do chat uma orientação clara e operacional.

Ele deve dizer, em essência:
- o que é;
- para onde vai;
- por que vai para esse lugar;
- o que não deve ser feito com ele.

Ele não deve inflar a resposta com taxonomia excessiva quando a decisão já estiver clara.

---

## 20. Limites da V1
Na V1, o Módulo 3 deve fazer bem o essencial:
- reconhecer a natureza do conteúdo;
- distinguir os destinos principais do sistema;
- escolher o destino correto;
- prevenir colisão documental;
- fortalecer continuidade futura.

A V1 não precisa ainda:
- roteamento automatizado complexo;
- múltiplos destinos paralelos sofisticados;
- orquestração avançada de painéis e pipelines;
- automações pesadas de publicação e sincronização.

A regra da fase permanece:
**fazer o eixo mínimo operar com estabilidade antes de sofisticar o sistema.**

---

## 21. Critério de sucesso do módulo
O Módulo 3 será considerado funcionalmente bem-sucedido quando conseguir, de modo consistente:
- reduzir salvamentos errados ou ausentes;
- impedir duplicação e sobrescrita indevida;
- aumentar clareza do fluxo entre chat, NPT, Drive, checkpoint e repo;
- fortalecer a rastreabilidade das decisões estruturais;
- transformar conteúdo relevante em persistência correta sem inflar o sistema.

---

## 22. Formulação canônica do módulo
Formulação oficial resumida:

**O Módulo 3 — Decisão de Destino — é o mecanismo do Cérebro Tendoshk responsável por decidir o encaminhamento operacional correto do que emerge no fluxo dos chats, distinguindo entre fluxo local, memória consolidada, peça integral, checkpoint, bootstrap e espelhamento em repositório, sem colisão entre camadas e sem perda de valor estrutural.**

---

## 23. Síntese final
Síntese canônica desta peça:

Não basta perceber bem.  
Não basta lembrar bem.  
É preciso encaminhar corretamente.

E, na V1, isso significa:  
reconhecer a natureza do conteúdo,  
escolher o destino certo,  
persistir o necessário,  
evitar colisão,  
e sustentar continuidade.
