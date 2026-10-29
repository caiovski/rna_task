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

## SLIDE 8: A Limitação da Reta e a Necessidade do MLP (Tempo: ~2 min)

* **Título do Slide:** Discussão Teórica: A Limitação da Reta e a Solução com MLP
* **Tópicos no Slide:**
  - **O Perceptron Simples resolveu o meme:** Perto e com pouca vida, o NPC foge com sucesso.
  - **A Descoberta da Limitação (O Efeito 'Vai e Volta'):**
    - A reta de decisão é infinita e inclinada.
    - Se o NPC fugir para longe (> 20m), a reta volta a dar sinal positivo para "Atacar".
    - Inimigos corpo a corpo andariam para frente até se aproximar, assustar e fugir de novo, gerando um loop de oscilação!
  - **Por que o Perceptron Simples não resolve isso sozinho?** Porque ele está preso à separação linear (uma única linha reta).
  - **Como o Perceptron Multicamadas (MLP) resolve?**
    - O MLP possui camadas ocultas e funções não-lineares, permitindo criar **fronteiras em curva ou em 'L'**.
    - Podemos definir uma regra fechada: *"Com menos de 20% de vida, FOGE SEMPRE, não importa a distância!"*, eliminando o loop.
* **O que você fala:**
  > *"Professor e turma, chegamos ao ponto alto da nossa análise crítica:*  
  > *O Perceptron Simples resolveu com perfeição o problema do meme de Skyrim: com 10% de vida colado no jogador, o inimigo recua.*  
  > 
  > *Porém, descobrimos uma limitação lógica muito interessante: como a reta do Perceptron é infinita e inclinada, se o bandido fugir e ficar muito longe (mais de 20 metros), a reta volta a dar sinal para 'Atacar'. Se for um inimigo de espada, ele correria em direção ao jogador de novo, até se aproximar, cruzar a linha e fugir outra vez, gerando um **loop de oscilação ('vai e volta')**!*  
  > 
  > *E é exatamente essa limitação da reta que justifica a criação do **Perceptron Multicamadas (MLP)**! Com o MLP e suas camadas ocultas, a fronteira de decisão não precisa ser uma reta: ela pode ser uma **curva ou um formato em 'L'**, definindo que com vida crítica o NPC foge para sempre, independentemente da distância!"*

---

## SLIDE 9: Conclusão & Perguntas (Tempo: ~1.5 min)

* **Título do Slide:** Conclusão & Considerações Finais
* **Tópicos no Slide:**
  - O Perceptron Simples continua sendo a base fundamental e mais rápida para IA em tempo real.
  - Resolve com precisão o problema da autopreservação básica em jogos.
  - Implementação validada tanto do zero quanto no Scikit-Learn.
  - Compreensão clara de suas fronteiras e de quando migrar para o MLP.
* **O que você fala:**
  > *"Para concluir: vimos que o Perceptron Simples de 1958 é uma ferramenta incrível, rápida e eficiente para tomada de decisão em tempo real. Conseguimos resolver o meme do Skyrim com custo computacional mínimo e, ao mesmo tempo, entendemos na prática por que a ciência precisou evoluir para o Perceptron Multicamadas quando os problemas exigem fronteiras não-lineares.  
  > Muito obrigado pela atenção de todos, e agora estou aberto para as dúvidas do professor!"*

---

## 🛡️ Dicas de Ouro para Perguntas do Professor (Colinha de Respostas)

* **Pergunta Crucial:** *"Se o Perceptron Multicamadas (MLP) resolve esse problema do loop 100%, por que você escolheu implementar o Perceptron Simples?"*
  - **Sua Resposta de Ouro:**
    > *"Professor, essa foi uma escolha deliberada de **engenharia de software e performance de jogos**:*  
    > 1. ***Custo Computacional a 60 FPS (Navalha de Occam):** Em um jogo de RPG de mundo aberto como Skyrim, não temos apenas 1 NPC; temos centenas de inimigos rodando simultaneamente com física, animações e renderização. O Perceptron Simples tem complexidade $O(1)$ — são apenas 2 multiplicações e 1 soma! O MLP exigiria calcular matrizes e funções sigmoides/ReLU para múltiplos neurônios ocultos, sendo um 'canhão para matar uma mosca' em uma decisão binária básica.*  
    > 2. ***Explicabilidade e Calibração (Caixa Branca vs Caixa Preta):** O Perceptron Simples é transparente. Qualquer game designer consegue ajustar os pesos e entender exatamente onde a reta está cortando no mapa. O MLP é uma caixa preta muito mais difícil de calibrar e depurar se o NPC tiver um comportamento estranho.*  
    > 3. ***Metodologia de Engenharia:** Em IA, a boa prática é sempre começar pelo modelo base mais simples e leve (baseline). Ao implementar o Perceptron Simples, resolvemos o meme do bandido suicida e identificamos com precisão o limite da separabilidade linear, o que nos dá a base teórica perfeita para justificar o MLP apenas quando for estritamente necessário!"*

* **Pergunta 2:** *"Por que você normalizou os dados dividindo por 100 e por 30?"*
  - **Sua Resposta:** *"Porque a vida varia de 0 a 100 e a distância de 0 a 30. Se não normalizarmos, a vida atualizaria os pesos 3 vezes mais rápido que a distância, desestabilizando o treino. Deixando ambas entre 0 e 1, o aprendizado converge suavemente em poucas épocas."*

* **Pergunta 3:** *"Qual a diferença entre o Perceptron e o Adaline?"*
  - **Sua Resposta:** *"O Perceptron calcula o erro depois da função degrau (saída discreta 0 ou 1). O Adaline calcula o erro antes da função degrau, usando a saída contínua e a descida do gradiente no Erro Quadrático Médio (MSE). Ambos continuam restritos a uma reta linear."*

* **Pergunta 4:** *"E os dados aleatórios que comentei na aula?"*
  - **Sua Resposta:** *"Incluímos no código o **Modo 2**: ao gerar 80 inimigos aleatórios com ruído de personalidade (covardia e fúria), a acurácia cai para cerca de 91% e o Perceptron comete 7 erros inevitáveis, comprovando na prática o Teorema da Convergência do Perceptron — nenhuma reta perfeita consegue separar dados com sobreposição!"*

