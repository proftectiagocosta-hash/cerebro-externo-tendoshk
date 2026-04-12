# Protocolo F5 / Save State, Checkpoint Rastreável e Retomada Diferencial do Cérebro Tendoshk — V1

## 1. Natureza da peça
Este documento estabelece o protocolo formal de save state do Cérebro Tendoshk na fase V1.

Sua função é fechar a lacuna entre:
- evocação operacional do regime;
- existência de checkpoint;
- rastreabilidade do estado salvo;
- verificação de mudanças posteriores;
- e reencontro preciso do ponto vigente da linha de trabalho.

Esta peça não substitui o Prompt-Mestre de Retomada Operacional do Cérebro Tendoshk — V1.1.
Ela também não substitui o Checkpoint Operacional da Fase Atual.

Ela existe para formalizar como o sistema salva, reencontra, compara e reentra no estado certo de trabalho.

---

## 2. Problema que a peça resolve
Antes desta peça, o sistema já sabia:
- evocar o regime corretamente;
- restaurar leitura estrutural;
- operar curadoria estrutural;
- produzir saída operacional.

A lacuna restante era:
- como salvar o estado de modo rastreável;
- como localizar checkpoint vigente;
- como verificar se houve mudanças desde ele;
- como classificar a retomada como limpa, ajustada ou alterada;
- e como agir quando não houver checkpoint válido.

Logo, esta peça resolve o problema de **persistência rastreável do estado operacional**.

---

## 3. Missão central do protocolo
A missão central deste protocolo é:

**definir o que é um save state válido, como ele deve ser registrado, como ele deve ser reencontrado e como deve ser comparado com mudanças posteriores para permitir retomada diferencial precisa, sem improviso e sem falsa continuidade.**

---

## 4. Conceitos fundamentais

### 4.1. Save state
É o estado operacional salvo de uma linha de trabalho em determinado ponto relevante.

### 4.2. Checkpoint rastreável
É o documento ou registro suficientemente identificável que preserva esse save state de forma utilizável em retomadas futuras.

### 4.3. Linha de trabalho
É um eixo coerente de continuidade operacional. Exemplos:
- arquitetura do cérebro;
- revisão de prompt mestre;
- modelagem de módulo;
- protocolo específico;
- revisão de sistema.

### 4.4. Retomada diferencial
É a retomada que não apenas carrega o regime, mas também compara o checkpoint salvo com mudanças posteriores e classifica o estado atual da continuidade.

### 4.5. Rastro documental
É o conjunto mínimo de documentos e registros que permite ao sistema reencontrar o estado vigente da linha de trabalho.

---

## 5. O que é um save state válido
Na V1, um save state só é considerado válido quando preserva, no mínimo:
- a linha de trabalho em questão;
- o ponto estrutural exato em que ela está;
- o que já foi estabilizado;
- o que não deve ser reaberto sem motivo forte;
- o próximo passo natural;
- as travas relevantes;
- a data ou momento lógico do salvamento;
- referência suficiente para rastrear mudanças posteriores.

Sem esses elementos, pode haver memória de contexto, mas não save state confiável.

---

## 6. O que compõe um checkpoint rastreável
Um checkpoint rastreável da V1 deve conter, no mínimo:

1. identificação da linha de trabalho
2. ponto exato do trabalho
3. peças relevantes vigentes
4. estado de estabilização do que já foi fechado
5. travas ativas
6. o que está em segundo plano
7. o que não deve ser reaberto sem motivo forte
8. próximo passo natural
9. indicação de necessidade ou não de verificação de mudanças posteriores
10. referência documental suficiente para rastreio

---

## 7. Onde vive o checkpoint
Na arquitetura atual, o checkpoint pode ter existência em mais de uma camada, mas com papéis distintos.

### 7.1. Ativo integral
O documento integral do checkpoint deve viver em:
- `ativos/contratos/`

### 7.2. Registro consolidado
A existência e implicação do checkpoint devem alimentar:
- `consolidados/npt_nucleo_persistente_tendoshk.md`

### 7.3. Logs operacionais
Sinais auxiliares de checkpoint e fechamento podem aparecer em:
- `logs/checkpoints.md`
- `data/inbox/checkpoints.json`

### 7.4. Regra de precedência
Se houver conflito:
- o ativo integral do checkpoint prevalece como referência principal do save state;
- logs e inbox funcionam como apoio rastreável, não como substituto do checkpoint integral.

---

## 8. O que constitui o rastro mínimo de uma linha de trabalho
Na V1, o rastro mínimo de uma linha de trabalho deve buscar, quando possível:
- bootstrap vigente;
- checkpoint vigente da linha;
- registros de mudança posteriores ao checkpoint;
- peças específicas relacionadas;
- contexto atual do chat.

A ordem correta é:
1. regime
2. estado salvo
3. mudanças posteriores
4. peças específicas
5. fluxo atual

---

## 9. Como verificar se já existe checkpoint
Quando o sistema entrar em retomada de uma linha de trabalho, ele deve verificar, nesta ordem:

1. se existe checkpoint integral conhecido para a linha;
2. se existe registro consolidado apontando para esse checkpoint;
3. se há logs ou inbox que indiquem checkpoint mais recente ou mudança posterior;
4. se o chat atual já contém referência suficiente a um checkpoint válido.

### Regra crítica
Não presumir inexistência de checkpoint apenas porque ele não está imediatamente visível no contexto superficial do chat.

---

## 10. Como agir quando já existe checkpoint válido
Se houver checkpoint válido e rastreável, o sistema deve:

1. identificar a linha de trabalho correta;
2. restaurar o checkpoint como save state da linha;
3. verificar se houve mudanças posteriores;
4. classificar a qualidade da continuidade;
5. restaurar o próximo passo natural;
6. seguir sem reabrir base indevidamente.

---

## 11. Como agir quando NÃO existe checkpoint válido
Se não houver checkpoint válido, o sistema não deve fingir retomada plena.

Ele deve:
1. declarar que não há checkpoint rastreável suficiente;
2. operar por evocação textual e contexto atual, se possível;
3. seguir do ponto estrutural inferível com honestidade operacional;
4. e, ao final de ciclo relevante, gerar novo checkpoint rastreável.

### Regra crítica
Ausência de checkpoint não impede operação.
Mas impede fingir reencontro preciso do estado salvo.

---

## 12. Verificação de mudanças posteriores
Depois de localizar o checkpoint, o sistema deve verificar se houve mudanças posteriores relevantes.

### 12.1. Mudanças gerais
- adição de arquivos
- criação de projetos
- mudança estrutural
- mudança de pastas
- mudança de backend ou fonte
- mudança de governança
- mudança de precedência

### 12.2. Mudanças específicas
- alteração em bootstrap
- alteração em checkpoint
- alteração em protocolo, módulo ou peça específica
- alteração em destino documental
- alteração em regra operacional
- alteração em prompt mestre
- alteração em parser safety ou serialização

### 12.3. Estabilidade confirmada
Se não houve mudança, isso também deve ser registrado como informação operacional válida.

---

## 13. Classificação da retomada diferencial
Após comparar checkpoint e mudanças posteriores, o sistema deve classificar a retomada em uma destas categorias:

### 13.1. Continuidade limpa
Quando o checkpoint continua vigente e não houve mudança posterior relevante.

### 13.2. Continuidade com ajuste incremental
Quando houve pequenas mudanças posteriores que não invalidam o estado salvo, apenas ajustam o contexto.

### 13.3. Continuidade com mudança estrutural relevante
Quando houve mudança que altera significativamente o estado salvo da linha.

### 13.4. Continuidade com necessidade de atualizar checkpoint
Quando o estado salvo ainda ajuda, mas já está parcialmente defasado.

### 13.5. Continuidade com necessidade de atualizar bootstrap ou peça específica
Quando a mudança afetou regra permanente, precedência ou arquitetura do regime.

---

## 14. Critério de falsa retomada
É falsa retomada quando o sistema:
- apenas lembra o tema geral;
- não verifica se existe checkpoint;
- não verifica mudanças posteriores;
- não distingue evocação textual de rastreabilidade documental;
- restaura contexto vago sem restaurar estado salvo;
- segue sem classificar a qualidade da continuidade.

A V1 deste protocolo existe justamente para impedir isso.

---

## 15. Relação com o Prompt-Mestre de Retomada
O Prompt-Mestre de Retomada Operacional do Cérebro Tendoshk — V1.1 continua sendo a peça que:
- carrega o regime;
- restaura enquadramento;
- restaura regras mínimas de operação;
- reduz genericidade.

Este protocolo complementa o Prompt-Mestre ao definir:
- o que é save state válido;
- como localizar checkpoint;
- como seguir o rastro documental;
- como verificar mudanças posteriores;
- como classificar a retomada diferencial.

### Síntese
O Prompt-Mestre de Retomada restaura o regime.  
Este Protocolo F5 restaura a rastreabilidade do estado.

---

## 16. Relação com o Prompt Mestre de Curadoria V6.1
O Prompt Mestre de Curadoria Estrutural V6.1 continua sendo a peça que:
- lê o chat estruturalmente;
- decide incorporação;
- gera NPT_ENTRY e CHAT_INDEX;
- classifica e indexa o conteúdo.

Este protocolo o complementa ao dizer:
- se existe ou não checkpoint daquela linha;
- se a curadoria está operando em continuidade limpa, ajustada ou alterada;
- se ao final deve ser criado ou atualizado checkpoint.

---

## 17. Regra de fechamento com save state
Ao final de sessão estruturalmente relevante, o sistema deve verificar se o ciclo exige:
- criação de novo checkpoint;
- atualização de checkpoint existente;
- apenas registro de mudança sem novo checkpoint;
- ou confirmação explícita de estabilidade sem mudança.

### Regra de decisão
Gerar ou atualizar checkpoint quando houver alteração real em:
- ponto da linha de trabalho;
- próximo passo natural;
- travas relevantes;
- peças vigentes;
- governança local da linha;
- ou entendimento operacional da continuidade.

---

## 18. Conteúdo mínimo do fechamento com F5
Quando houver fechamento relevante, o sistema deve registrar, no mínimo:
- linha de trabalho;
- houve ou não houve mudança;
- mudanças gerais;
- mudanças específicas;
- classificação da continuidade;
- checkpoint usado ou inexistente;
- necessidade ou não de atualizar checkpoint;
- próximo passo natural.

---

## 19. Regra de acionamento do F5
Este protocolo deve ser acionado quando houver:
- retomada de linha de trabalho relevante;
- dúvida sobre estado salvo;
- dúvida sobre continuidade real;
- necessidade de fechar ciclo com rastreabilidade;
- mudança estrutural importante;
- necessidade de saber se já existe checkpoint válido.

Ele não precisa ser acionado para conversas casuais sem impacto estrutural.

---

## 20. Modo de verificação
Ao aplicar este protocolo, o assistente deve explicitar qual modo está usando:

### 20.1. Evocação textual
Quando opera com base em prompt e contexto do chat, sem checkpoint externo rastreável confirmado.

### 20.2. Verificação documental parcial
Quando consegue acessar parte das fontes soberanas, mas não todas.

### 20.3. Verificação documental plena
Quando consegue acessar checkpoint, mudanças posteriores e peças relevantes suficientes para classificar a retomada com alta confiança.

---

## 21. Fórmula operacional do F5
A fórmula operacional da V1 é:

1. identificar a linha de trabalho
2. verificar se existe checkpoint
3. localizar o rastro documental mínimo
4. verificar mudanças posteriores
5. classificar a retomada
6. restaurar o próximo passo natural
7. operar
8. fechar com novo registro ou novo checkpoint quando necessário

---

## 22. Critério de sucesso do protocolo
O protocolo será considerado funcionalmente bem-sucedido quando conseguir, de modo consistente:
- impedir falsa continuidade;
- distinguir evocação boa de save state real;
- permitir reencontro preciso do ponto da linha;
- reduzir reconstrução manual do estado;
- registrar mudanças e estabilidade com clareza;
- atualizar checkpoints quando necessário.

---

## 23. Cláusula de realidade operacional
Esta versão passa a valer mesmo reconhecendo que ainda podem existir lacunas de implementação, rastreabilidade incompleta ou trechos do sistema ainda não plenamente conectados.

Essas lacunas não invalidam a entrada em vigor desta peça.
Elas devem gerar:
- registros de mudança;
- correções localizadas;
- novos checkpoints;
- e futuras revisões do próprio protocolo.

A regra não é voltar ao escuro.
A regra é: localizar, comparar, classificar, registrar e corrigir.

---

## 24. Formulação canônica final
Formulação oficial resumida:

**O Protocolo F5 / Save State, Checkpoint Rastreável e Retomada Diferencial do Cérebro Tendoshk — V1 é a peça responsável por formalizar como o sistema salva o estado de uma linha de trabalho, reencontra esse estado de forma rastreável, compara mudanças posteriores e classifica a continuidade antes de seguir operando.**

---

## 25. Síntese final
Síntese canônica desta peça:

O sistema já sabe evocar o regime.  
Agora ele precisa saber salvar e reencontrar o estado.  

E, na V1, isso significa:
- saber o que é checkpoint válido;
- saber onde ele vive;
- saber segui-lo;
- saber comparar mudanças;
- e saber classificar a qualidade real da retomada.