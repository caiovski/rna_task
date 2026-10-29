# 🎮 Roteiro Completo de Apresentação (15 Minutos)
**Tema:** IA de Sobrevivência para NPCs em Jogos de RPG usando o Perceptron Simples  
**Disciplina:** Inteligência Artificial I  
**Tempo Total:** 15 Minutos (12 min apresentação + 3 min perguntas)

---

## Estrutura Geral dos 15 Minutos

```
  00:00 ──── 02:00   SLIDE 1 & 2: Gancho & O Meme do Skyrim
  02:00 ──── 05:00   SLIDE 3 & 4: O Que é o Perceptron & A Lógica das Entradas
  05:00 ──── 07:30   SLIDE 5: A Matemática Descomplicada (Sem Derivadas!)
  07:30 ──── 11:30   SLIDE 6 & 7: Demonstração ao Vivo (Código do Zero + Scikit-Learn + Gráfico)
  11:30 ──── 13:30   SLIDE 8: Por que o Perceptron basta? (Separação Linear vs MLP)
  13:30 ──── 15:00   SLIDE 9: Conclusão & Perguntas do Professor
```

---

## SLIDE 1: Capa e Introdução (Tempo: ~1 min)

* **Título do Slide:** IA de Sobrevivência para NPCs em RPGs: Tomada de Decisão com Perceptron Simples
* **Subtítulo:** Aplicação Prática, Implementação do Zero e Comparação com Scikit-Learn
* **Elementos Visuais:** Logo da faculdade, seu nome e uma imagem de jogo RPG / Skyrim.
* **O que você fala:**
  > *"Boa tarde professor, boa tarde turma! Hoje vou apresentar a aplicação prática de um dos pilares mais fundamentais da Inteligência Artificial: o **Perceptron Simples** de Rosenblatt. Para demonstrar o modelo em ação, escolhi um tema que todo mundo que joga videogame já vivenciou: a tomada de decisão e instinto de sobrevivência de inimigos em jogos de RPG."*

---

## SLIDE 2: O Problema - O Meme do Bandido no Skyrim (Tempo: ~1.5 min)

* **Título do Slide:** O Problema: A Falta de Instinto de Sobrevivência nos NPCs
* **Tópicos no Slide:**
  - Inimigos com 5% de HP atacando jogadores invencíveis.
  - Scripts rígidos e árvores de decisão manuais cheias de bugs.
  - Falta de percepção de contexto (Vida vs Proximidade do Perigo).
* **Elementos Visuais:** Meme de Skyrim com um bandido correndo para cima do Dragonborn de armadura completa.
* **O que você fala:**
  > *"Quem aqui já jogou Skyrim ou outro RPG clássico? Você está com o seu personagem no nível máximo, com a melhor armadura do jogo e um machado colossal. De repente, surge um bandido de adaga, com apenas 5% de vida restante, grita 'Nunca deveria ter vindo aqui!' e corre de peito aberto para morrer em um único golpe. Isso acontece porque a IA desses jogos antigos frequentemente usa scripts fixos ou árvores de decisão simples que ignoram o contexto da batalha. O nosso objetivo hoje é resolver isso usando uma rede neural."*

---

## SLIDE 3: A Proposta - O Módulo de Sobrevivência (Tempo: ~2 min)

* **Título do Slide:** A Solução: Classificação Linear de Luta ou Fuga (Fight or Flight)
* **Tópicos no Slide:**
  - **Entrada 1 ($x_1$):** Vida do Inimigo (0% a 100%).
  - **Entrada 2 ($x_2$):** Distância até o Jogador (0 a 30 metros).
  - **Saída ($y$):** 
    - `0` = **FUGIR / RECUAR** (Buscar poção ou cobertura).
    - `1` = **ATACAR / LUTAR** (Seguir no combate).
* **Elementos Visuais:** Diagrama do neurônio recebendo Vida e Distância e acionando a ação.
* **O que você fala:**
  > *"Propomos um módulo inteligente de sobrevivência baseado em duas variáveis críticas que qualquer jogo monitora: a vida atual do NPC e a distância dele até o jogador. Se o NPC tiver pouca vida e o perigo estiver colado nele, o instinto básico deve ser recuar. Se estiver com vida alta ou a uma distância segura, ele pode lutar. O Perceptron aprende a fronteira exata que divide essas duas decisões."*

---

## SLIDE 4: O Modelo - O Perceptron de Rosenblatt (1958) (Tempo: ~2 min)

* **Título do Slide:** O Funcionamento do Perceptron Simples
* **Tópicos no Slide:**
  - Desenvolvido por Frank Rosenblatt em 1958.
  - Inspiração no neurônio biológico (dendritos, soma e axônio).
  - Multiplica entradas pelos pesos e adiciona o bias:
    $$\text{Soma} = (x_1 \cdot w_1) + (x_2 \cdot w_2) + b$$
  - Função Degrau (Heaviside):
    $$\text{Saída} = \begin{cases} 1, & \text{se Soma} \ge 0 \\ 0, & \text{se Soma} < 0 \end{cases}$$
* **Elementos Visuais:** Ilustração clássica do neurônio artificial.
* **O que você fala:**
  > *"O Perceptron é o bloco construtor de todas as redes neurais modernas. Ele funciona de forma direta: cada informação (vida e distância) é multiplicada por um peso que representa sua importância. Somamos tudo com um bias e passamos por uma função degrau. Se a soma for positiva, o neurônio dispara '1' (atacar). Se for negativa, dispara '0' (fugir). É como um interruptor que aprende a hora certa de ligar."*

---

## SLIDE 5: A Matemática Sem Complicação (Tempo: ~1.5 min)

* **Título do Slide:** Como o Perceptron Aprende? (Sem Derivadas!)
* **Tópicos no Slide:**
  - **Sem derivadas parciais e sem cálculo avançado**: Apenas soma e multiplicação.
  - O cálculo do erro é direto:
    $$\text{Erro} = y_{\text{esperado}} - y_{\text{previsto}} \quad (\text{resultado: } 0, +1 \text{ ou } -1)$$
  - Atualização dos pesos:
    $$w_i = w_i + (\eta \cdot \text{Erro} \cdot x_i)$$
    $$b = b + (\eta \cdot \text{Erro})$$
  - Se acertou ($\text{Erro} = 0$), os pesos permanecem idênticos.
* **O que você fala:**
  > *"O mais fascinante do Perceptron é a elegância e simplicidade do aprendizado. Ele não precisa de derivadas parciais, gradientes complexos ou regras da cadeia. Quando o NPC deveria fugir mas decide atacar, o erro é negativo e nós simplesmente subtraímos a entrada dos pesos. Se ele acerta, o erro é zero e o algoritmo não altera nada. É pura correção por tentativa e erro."*

---

## SLIDE 6: Demonstração Prática (Código ao Vivo) (Tempo: ~3 min)

* **Título do Slide:** Implementação: Do Zero vs Scikit-Learn
* **Tópicos no Slide:**
  - Código artesanal em Python puro (demonstração dos fundamentos).
  - Validação usando a biblioteca de mercado `sklearn.linear_model.Perceptron`.
  - **Alternância de Dados:**
    - Modo 1: Dados Fixos (14 inimigos) &rarr; Separação linear perfeita (100% acerto na época 5).
    - Modo 2: Dados Aleatórios (80 inimigos com ruído) &rarr; O Perceptron erra alguns pontos (~90% acerto), comprovando a teoria do professor!
  - **Modo Interativo:** Teste ao vivo sugerido pelo professor ou pela turma!
* **O que você faz:**
  > *(Você minimiza ou muda de janela para o terminal e roda: `python ia_skyrim_perceptron.py`)*
  >
  > *"Logo ao iniciar, o programa nos dá duas opções: rodar com dados fixos controlados ou com dados aleatórios com ruído.  
  > No Modo 1, com dados linearmente separáveis, o modelo zera todos os erros já na época 5 com 100% de acurácia!  
  > Mas se rodarmos o Modo 2 com 80 inimigos aleatórios, o modelo comete cerca de 7 a 9 erros inevitáveis (~90% de acurácia), exatamente como o professor explicou em aula: nenhuma reta consegue separar pontos com ruído comportamental!"*
  >
  > *(Em seguida, chame o professor para o teste interativo):*
  > *"Professor, me dê um valor de vida e distância para testarmos agora ao vivo!"*

---

## SLIDE 7: Análise Visual - A Fronteira de Decisão (Tempo: ~2 min)

* **Título do Slide:** Fronteira de Decisão: A Reta que Salva o NPC
* **Elementos Visuais:** Mostre a imagem gerada `grafico_skyrim.png` na tela cheia.
* **Tópicos no Slide:**
  - **Região Vermelha:** Zona de Recuo / Fuga.
  - **Região Verde:** Zona de Combate.
  - **Linha Azul Tracejada:** Fronteira calculada pelo nosso **Perceptron do Zero**.
  - **Linha Laranja Pontilhada:** Fronteira calculada pelo **Scikit-Learn** (mostrando convergência equivalente!).
  - **Estrela Amarela:** O bandido do Skyrim (10% HP, 2m) salvo pelo Perceptron!
  - **Triângulo Roxo:** O arqueiro (15% HP, 28m) que ataca por estar seguro pela distância.
* **O que você fala:**
  > *"Este gráfico resume visualmente todo o aprendizado. Cada ponto verde é combate seguro e cada ponto vermelho é recuo crítico. Nós plotamos duas retas: a **azul tracejada** (calculada pelo nosso modelo do zero) e a **laranja pontilhada** (calculada pelo Scikit-Learn). Ambas encontram hiperplanos válidos que separam perfeitamente os dados!  
  > Reparem na **estrela amarela** no canto inferior esquerdo: ela representa o bandido do Skyrim com 10% de vida e a 2 metros, caindo com folga na zona de fuga. Já no canto superior esquerdo, o **triângulo roxo** representa um arqueiro com 15% de vida, mas a 28 metros de distância: ele decide atacar porque a grande distância lhe dá segurança tática!"*

---

## SLIDE 8: Por que o Perceptron e não o MLP? (Tempo: ~1.5 min)

* **Título do Slide:** Discussão Teórica: Separação Linear vs MLP
* **Tópicos no Slide:**
  - **O Perceptron é perfeito aqui porque:** O problema é linearmente separável (uma reta divide o plano).
  - **Limitação histórica (Minsky & Papert, 1969):** O Perceptron falha no problema do XOR (não-linear).
  - **Quando precisaríamos do Perceptron Multicamadas (MLP)?**
    - Se houvesse tipos de terreno, poções no inventário ou zonas circulares de perigo.
    - O MLP resolveria com camadas ocultas (*hidden layers*) e *Backpropagation*.
* **O que você fala:**
  > *"Para fechar a parte teórica: por que não usamos um Perceptron Multicamadas (MLP)? Porque em engenharia de IA, a regra de ouro é: use a solução mais simples que resolve o problema com perfeição (Navalha de Occam). Como a relação entre vida e distância forma duas regiões contínuas separadas por uma reta, o Perceptron Simples atinge 100% de acurácia com custo computacional mínimo, ideal para rodar em tempo real em jogos com centenas de inimigos simultâneos."*

---

## SLIDE 9: Conclusão & Perguntas (Tempo: ~1.5 min)

* **Título do Slide:** Conclusão & Agradecimentos
* **Tópicos no Slide:**
  - O Perceptron Simples continua relevante 68 anos após sua criação.
  - Baixíssimo custo computacional, ideal para lógica de jogos.
  - Código implementado do zero e validado no Scikit-Learn.
  - Dúvidas ou perguntas?
* **O que você fala:**
  > *"Concluímos que um modelo clássico de 1958 ainda é extremamente prático e eficiente para resolver problemas reais de tomada de decisão. O código completo e a comparação com Scikit-Learn comprovam sua eficácia. Muito obrigado a todos pela atenção, e agora estou aberto às perguntas do professor e dos colegas!"*

---

## 🛡️ Dicas de Ouro para Perguntas do Professor (Colinha de Respostas)

* **Pergunta 1:** *"Por que você normalizou os dados dividindo por 100 e por 30?"*
  - **Sua Resposta:** *"Porque a vida varia de 0 a 100 e a distância de 0 a 30. Se não normalizarmos, a vida atualizaria os pesos 3 vezes mais rápido que a distância, desestabilizando o treino. Deixando ambas entre 0 e 1, o aprendizado converge suavemente em poucas épocas."*
* **Pergunta 2:** *"Qual a diferença entre o Perceptron e o Adaline?"*
  - **Sua Resposta:** *"O Perceptron calcula o erro depois da função degrau (saída discreta 0 ou 1). O Adaline calcula o erro antes da função degrau, usando a saída contínua e a descida do gradiente no Erro Quadrático Médio (MSE)."*
* **Pergunta 3:** *"E se a taxa de aprendizado for muito alta ou muito baixa?"*
  - **Sua Resposta:** *"Se for alta demais, os pesos podem oscilar em volta da reta sem convergir. Se for muito baixa, o treino demora muito mais épocas para atingir zero erros. O valor 0.1 se mostrou ideal para os nossos dados."*

