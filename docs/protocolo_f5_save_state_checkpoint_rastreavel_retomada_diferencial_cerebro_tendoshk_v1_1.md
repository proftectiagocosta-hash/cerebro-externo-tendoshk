# Protocolo F5 / Save State, Checkpoint Rastreável e Retomada Diferencial do Cérebro Tendoshk — V1.1

## 1. Natureza da peça
Este documento estabelece o protocolo formal de save state do Cérebro Tendoshk na fase V1.1.

Sua função é fechar a lacuna entre:
- evocação operacional do regime;
- existência de checkpoint;
- rastreabilidade do estado salvo;
- verificação de mudanças posteriores;
- e reencontro preciso do ponto vigente da linha de trabalho.

Esta peça não substitui o Prompt-Mestre de Retomada Operacional do Cérebro Tendoshk.
Ela também não substitui o Checkpoint Operacional da Fase Atual.

Ela existe para formalizar como o sistema salva, reencontra, compara e reentra no estado certo de trabalho.

---

## 2. Repositório oficial do Cérebro Tendoshk
Repositório oficial de referência desta arquitetura:

`https://github.com/proftectiagocosta-hash/cerebro-externo-tendoshk/tree/main`

### Regra soberana derivada
Quando a retomada ocorrer em chat novo e houver acesso ao GitHub, este repositório deve ser tratado como fonte versionada prioritária para localizar:
- protocolos vigentes;
- prompts mestres vigentes;
- checkpoints rastreáveis;
- e peças integrais correlatas da linha de trabalho.

---

## 3. Problema que a peça resolve
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

## 4. Missão central do protocolo
A missão central deste protocolo é:

**definir o que é um save state válido, como ele deve ser registrado, como ele deve ser reencontrado e como deve ser comparado com mudanças posteriores para permitir retomada diferencial precisa, sem improviso e sem falsa continuidade.**

---

## 5. Conceitos fundamentais

### 5.1. Save state
É o estado operacional salvo de uma linha de trabalho em determinado ponto relevante.

### 5.2. Checkpoint rastreável
É o documento ou registro suficientemente identificável que preserva esse save state de forma utilizável em retomadas futuras.

### 5.3. Linha de trabalho
É um eixo coerente de continuidade operacional.

### 5.4. Retomada diferencial
É a retomada que não apenas carrega o regime, mas também compara o checkpoint salvo com mudanças posteriores e classifica o estado atual da continuidade.

### 5.5. Rastro documental
É o conjunto mínimo de documentos e registros que permite ao sistema reencontrar o estado vigente da linha de trabalho.

---

## 6. O que é um save state válido
Na V1.1, um save state só é considerado válido quando preserva, no mínimo:
- a linha de trabalho em questão;
- o ponto estrutural exato em que ela está;
- o que já foi estabilizado;
- o que não deve ser reaberto sem motivo forte;
- o próximo passo natural;
- as travas relevantes;
- a data ou momento lógico do salvamento;
- referência suficiente para rastrear mudanças posteriores.

---

## 7. O que compõe um checkpoint rastreável
Um checkpoint rastreável da V1.1 deve conter, no mínimo:
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

## 8. Onde vive o checkpoint
### 8.1. Ativo integral
O documento integral do checkpoint deve viver em:
- `ativos/contratos/`

### 8.2. Registro consolidado
A existência e implicação do checkpoint devem alimentar:
- `consolidados/npt_nucleo_persistente_tendoshk.md`

### 8.3. Logs operacionais
Sinais auxiliares de checkpoint e fechamento podem aparecer em:
- `logs/checkpoints.md`
- `data/inbox/checkpoints.json`

### 8.4. Espelho versionado oficial
O checkpoint deve, quando aplicável, ser espelhado no repositório oficial do cérebro em `docs/`.

### 8.5. Regra de precedência
Se houver conflito:
- o ativo integral do checkpoint prevalece como referência principal do save state;
- o repositório oficial funciona como espelho versionado prioritário acessível entre chats;
- logs e inbox funcionam como apoio rastreável, não como substituto do checkpoint integral.

---

## 9. Regra de busca do último checkpoint
Quando o sistema entrar em retomada de uma linha de trabalho e houver acesso ao GitHub, ele deve buscar primeiro no repositório oficial do cérebro.

### Ordem obrigatória de busca
1. localizar no repositório oficial arquivos de checkpoint em `docs/` cujo nome siga padrão próximo de `checkpoint_operacional_*.md`;
2. selecionar primeiro os checkpoints semanticamente compatíveis com a linha de trabalho atual;
3. entre checkpoints compatíveis, priorizar a versão mais recente e mais específica;
4. verificar se existe peça posterior que atualize o entendimento da linha;
5. só depois complementar com consolidado, logs, inbox e contexto do chat.

### Regra crítica
Se o repositório estiver acessível, o sistema **não deve** começar a retomada apenas por evocação textual sem antes tentar localizar o último checkpoint relevante no repo oficial.

---

## 10. Como verificar se já existe checkpoint
Quando o sistema entrar em retomada de uma linha de trabalho, ele deve verificar, nesta ordem:
1. se existe checkpoint integral conhecido para a linha no repositório oficial;
2. se existe checkpoint integral conhecido fora do repo, mas referenciado na arquitetura;
3. se existe registro consolidado apontando para esse checkpoint;
4. se há logs ou inbox que indiquem checkpoint mais recente ou mudança posterior;
5. se o chat atual já contém referência suficiente a um checkpoint válido.

### Regra crítica
Não presumir inexistência de checkpoint apenas porque ele não está imediatamente visível no contexto superficial do chat.

---

## 11. Como agir quando já existe checkpoint válido
Se houver checkpoint válido e rastreável, o sistema deve:
1. identificar a linha de trabalho correta;
2. restaurar o checkpoint como save state da linha;
3. verificar se houve mudanças posteriores;
4. classificar a qualidade da continuidade;
5. restaurar o próximo passo natural;
6. seguir sem reabrir base indevidamente.

---

## 12. Como agir quando NÃO existe checkpoint válido
Se não houver checkpoint válido, o sistema não deve fingir retomada plena.

Ele deve:
1. declarar que não há checkpoint rastreável suficiente;
2. declarar se o repo foi ou não consultado;
3. operar por evocação textual e contexto atual, se possível;
4. seguir do ponto estrutural inferível com honestidade operacional;
5. e, ao final de ciclo relevante, gerar novo checkpoint rastreável.

---

## 13. Verificação de mudanças posteriores
Depois de localizar o checkpoint, o sistema deve verificar se houve mudanças posteriores relevantes.

### 13.1. Mudanças gerais
- adição de arquivos
- criação de projetos
- mudança estrutural
- mudança de pastas
- mudança de backend ou fonte
- mudança de governança
- mudança de precedência

### 13.2. Mudanças específicas
- alteração em bootstrap
- alteração em checkpoint
- alteração em protocolo, módulo ou peça específica
- alteração em destino documental
- alteração em regra operacional
- alteração em prompt mestre
- alteração em parser safety ou serialização

### 13.3. Estabilidade confirmada
Se não houve mudança, isso também deve ser registrado como informação operacional válida.

---

## 14. Classificação da retomada diferencial
Após comparar checkpoint e mudanças posteriores, o sistema deve classificar a retomada em uma destas categorias:
- continuidade limpa
- continuidade com ajuste incremental
- continuidade com mudança estrutural relevante
- continuidade com necessidade de atualizar checkpoint
- continuidade com necessidade de atualizar bootstrap ou peça específica

---

## 15. Critério de falsa retomada
É falsa retomada quando o sistema:
- apenas lembra o tema geral;
- não verifica se existe checkpoint;
- não consulta o repositório oficial quando ele está acessível;
- não verifica mudanças posteriores;
- não distingue evocação textual de rastreabilidade documental;
- restaura contexto vago sem restaurar estado salvo;
- segue sem classificar a qualidade da continuidade.

---

## 16. Relação com o Prompt-Mestre de Retomada
O Prompt-Mestre de Retomada restaura o regime.
Este Protocolo F5 restaura a rastreabilidade do estado.

A regra de integração passa a ser:
- o Prompt-Mestre de Retomada deve saber que este protocolo existe;
- e deve, quando possível, buscar o último checkpoint relevante no repositório oficial antes de depender apenas da evocação textual.

---

## 17. Relação com o Prompt Mestre de Curadoria V6.1
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

## 18. Regra de fechamento com save state
Ao final de sessão estruturalmente relevante, o sistema deve verificar se o ciclo exige:
- criação de novo checkpoint;
- atualização de checkpoint existente;
- apenas registro de mudança sem novo checkpoint;
- ou confirmação explícita de estabilidade sem mudança.

---

## 19. Conteúdo mínimo do fechamento com F5
Quando houver fechamento relevante, o sistema deve registrar, no mínimo:
- linha de trabalho;
- houve ou não houve mudança;
- mudanças gerais;
- mudanças específicas;
- classificação da continuidade;
- checkpoint usado ou inexistente;
- se o repositório oficial foi consultado ou não;
- necessidade ou não de atualizar checkpoint;
- próximo passo natural.

---

## 20. Regra de acionamento do F5
Este protocolo deve ser acionado quando houver:
- retomada de linha de trabalho relevante;
- dúvida sobre estado salvo;
- dúvida sobre continuidade real;
- necessidade de fechar ciclo com rastreabilidade;
- mudança estrutural importante;
- necessidade de saber se já existe checkpoint válido.

---

## 21. Modo de verificação
Ao aplicar este protocolo, o assistente deve explicitar qual modo está usando:
- evocação textual
- verificação documental parcial
- verificação documental plena

E deve dizer, quando aplicável, se o repositório oficial foi consultado.

---

## 22. Fórmula operacional do F5
A fórmula operacional da V1.1 é:
1. identificar a linha de trabalho
2. buscar o último checkpoint relevante no repositório oficial, quando acessível
3. verificar se existe checkpoint
4. localizar o rastro documental mínimo
5. verificar mudanças posteriores
6. classificar a retomada
7. restaurar o próximo passo natural
8. operar
9. fechar com novo registro ou novo checkpoint quando necessário

---

## 23. Critério de sucesso do protocolo
O protocolo será considerado funcionalmente bem-sucedido quando conseguir, de modo consistente:
- impedir falsa continuidade;
- distinguir evocação boa de save state real;
- permitir reencontro preciso do ponto da linha;
- reduzir reconstrução manual do estado;
- registrar mudanças e estabilidade com clareza;
- atualizar checkpoints quando necessário;
- e usar o repositório oficial como trilha de busca versionada entre chats.

---

## 24. Cláusula de realidade operacional
Esta versão passa a valer mesmo reconhecendo que ainda podem existir lacunas de implementação, rastreabilidade incompleta ou trechos do sistema ainda não plenamente conectados.

Essas lacunas não invalidam a entrada em vigor desta peça.
Elas devem gerar:
- registros de mudança;
- correções localizadas;
- novos checkpoints;
- e futuras revisões do próprio protocolo.

---

## 25. Formulação canônica final
**O Protocolo F5 / Save State, Checkpoint Rastreável e Retomada Diferencial do Cérebro Tendoshk — V1.1 é a peça responsável por formalizar como o sistema salva o estado de uma linha de trabalho, reencontra esse estado de forma rastreável, busca prioritariamente o último checkpoint relevante no repositório oficial do cérebro quando ele estiver acessível, compara mudanças posteriores e classifica a continuidade antes de seguir operando.**

---

## 26. Síntese final
O sistema já sabe evocar o regime.
Agora ele deve saber salvar e reencontrar o estado.

E, na V1.1, isso significa:
- saber o que é checkpoint válido;
- saber onde ele vive;
- saber que o repositório oficial do cérebro é a trilha versionada prioritária para buscar o último checkpoint entre chats;
- saber comparar mudanças;
- e saber classificar a qualidade real da retomada.