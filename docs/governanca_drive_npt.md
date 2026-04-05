# Governança do Drive/NPT

## Objetivo

Definir de forma objetiva a função de cada camada documental da infraestrutura NPT/Drive, reduzindo duplicação, ambiguidade e dispersão estrutural.

---

## Princípio central

A estrutura deve separar claramente:

- o que é regra/transversal
- o que é ficha de projeto
- o que é arquivo de apoio, navegação ou fluxo

A pergunta operacional para decidir o destino de qualquer conteúdo é:

> esta informação normatiza o sistema, descreve uma frente específica, ou apenas apoia a navegação/operação?

---

## 1. Arquivos centrais numerados

### Função
Camada canônica e transversal do ecossistema.

### Devem conter
- arquitetura do sistema
- regras estruturais
- protocolos recorrentes
- memória persistente de alto valor transversal
- decisões-mãe
- critérios oficiais
- governança
- relação entre camadas do ecossistema

### Devem responder
- como o sistema funciona
- quais são as regras
- quais decisões valem para múltiplos projetos
- como a arquitetura oficial está organizada

### Não devem conter
- dump bruto de conversas
- dev log granular de um único projeto
- brainstorming cru
- material provisório ainda não consolidado

---

## 2. Pasta `projetos/`

### Função
Camada de identidade, escopo e estado de cada frente/projeto.

### Devem conter
- ficha oficial do projeto
- propósito
- escopo
- status atual
- componentes principais
- entregáveis
- vínculos com outras frentes
- próximos passos

### Devem responder
- o que é este projeto
- para que ele existe
- em que estado está
- quais são seus blocos principais
- para onde ele evolui

### Não devem conter
- regras gerais do ecossistema
- protocolos transversais
- dump integral de histórico
- duplicação dos arquivos centrais numerados

---

## 3. Arquivos soltos na raiz

### Função
Apoio institucional, navegação, indexação, fluxo ou transição.

### Devem conter apenas
- mapa mestre
- README estrutural
- índice geral
- registro de chats indexados
- arquivos de entrada/saída de fluxo
- artefatos especiais com justificativa clara

### Regra
A raiz não deve virar estacionamento documental.

Se um arquivo solto não for:
- institucional
- navegacional
- de fluxo
- ou transitório com justificativa

então ele está no lugar errado.

---

## Regra de decisão resumida

### Vai para arquivo central numerado quando:
é regra, protocolo, arquitetura, decisão transversal ou memória canônica do sistema.

### Vai para `projetos/` quando:
é a ficha-identidade e o estado de uma frente específica.

### Vai para a raiz quando:
é um artefato de navegação, indexação, fluxo ou apoio institucional especial.

---

## Tratamento atual do Cérebro Externo Tendoshk

No estágio atual, o Cérebro Externo Tendoshk não deve ser formalizado ainda como projeto canônico próprio dentro da infraestrutura NPT/Drive.

### Enquadramento atual
- piloto estratégico-operacional
- camada inteligente anterior à ingestão
- sistema auxiliar de triagem, curadoria, priorização e exportação
- apoio ao fluxo oficial, sem substituí-lo

### Destino atual do seu valor
O valor gerado pelo Cérebro Externo deve ser distribuído, por enquanto, entre:

- `AMBIENTES_RETOMADA`
- `NPT_NUCLEO_PERSISTENTE_TENDOSHK`
- `SISTEMA_MEMORIA_AUDITORIA` (quando o foco for arquitetura, consistência e governança)

### Regra atual
- não criar ainda 12º projeto canônico
- não abrir ainda destino oficial próprio
- registrar seu papel arquitetural na camada central
- registrar sua operação piloto nos destinos já existentes

---

## Critério para futura promoção de status

O Cérebro Externo só deve ganhar frente própria quando atender claramente a um ou mais destes critérios:

1. deixar de ser apenas pré-ingestão e passar a ter função sistêmica autônoma
2. possuir governança própria estável
3. gerar artefatos recorrentes que não caibam bem nos destinos atuais
4. exigir rastreabilidade independente dentro do ecossistema
5. demonstrar valor contínuo além do piloto técnico

---

## Decisão vigente

A governança atual reconhece o Cérebro Externo Tendoshk como camada piloto de inteligência anterior ao NPT, ainda integrada conceitualmente ao núcleo persistente e aos ambientes/retomada, sem formalização canônica independente neste estágio.