"""
=============================================================================
PROJETO: IA de Sobrevivência para NPCs em RPG (Skyrim)
MODELO:  Perceptron Simples (Rosenblatt, 1958) + Comparação Scikit-Learn
DISCIPLINA: Inteligência Artificial I
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron as SklearnPerceptron

# =====================================================================
# 1. SELEÇÃO DO CONJUNTO DE DADOS (Fixos vs Aleatórios)
# =====================================================================
print("=" * 65)
print("     IA DE SOBREVIVENCIA PARA NPCS (PERCEPTRON SIMPLES)         ")
print("=" * 65)
print("Escolha o conjunto de dados para o treinamento:")
print("  [1] Dados Fixos (14 inimigos controlados -> Separacao 100% perfeita)")
print("  [2] Dados Aleatorios com Ruido (80 inimigos -> O Perceptron erra mais!)")
escolha = input("Opcao [Pressione ENTER para 1]: ").strip()

MAX_VIDA = 100.0
MAX_DIST = 30.0

if escolha == "2":
    # MODO 2: 80 inimigos aleatórios com ruído de personalidade (covardia/fúria)
    np.random.seed(42) # Semente fixa para reprodutibilidade garantida
    n = 80
    vidas = np.random.uniform(5, 95, n)
    distancias = np.random.uniform(1, 29, n)
    dados_brutos = np.column_stack((vidas, distancias))
    
    # Regra base + ruído estocástico (pontos misturados)
    pontos = (vidas / MAX_VIDA) * 0.12 + (distancias / MAX_DIST) * 0.12 - 0.10
    ruido = np.random.normal(0, 0.025, n)
    y = np.where((pontos + ruido) >= 0, 1, 0)
    nome_modo = "ALEATORIOS COM RUIDO (80 Inimigos)"
else:
    # MODO 1: 14 inimigos clássicos pré-estabelecidos
    dados_brutos = np.array([
        # [Vida, Distância] -> Decisão
        [10,  2],   # 0: Quase sem vida e colado -> Fugir!
        [15,  5],   # 0: Pouca vida e perto -> Fugir!
        [20,  4],   # 0: Pouca vida e perto -> Fugir!
        [25, 10],   # 0: Pouca vida -> Fugir!
        [30,  3],   # 0: Vida baixa e colado -> Fugir!
        [35,  8],   # 0: Vida baixa -> Fugir!
        
        [45, 20],   # 1: Meia vida mas com folga de distância -> Atacar!
        [60, 10],   # 1: Boa vida -> Atacar!
        [70,  5],   # 1: Muita vida, pode ir pro mano a mano -> Atacar!
        [80, 18],   # 1: Vida alta -> Atacar!
        [90,  3],   # 1: Vida cheia, vai pra cima -> Atacar!
        [95, 25],   # 1: Tanque de guerra -> Atacar!
        [85, 12],   # 1: Muito saudável -> Atacar!
        [55, 15]    # 1: Equilibrado -> Atacar!
    ])
    y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
    nome_modo = "FIXOS PRE-ESTABELECIDOS (14 Inimigos)"

print(f"\n-> Modo Selecionado: {nome_modo}\n")

# Normalização simples (0 a 1):
X = np.zeros_like(dados_brutos, dtype=float)
X[:, 0] = dados_brutos[:, 0] / MAX_VIDA
X[:, 1] = dados_brutos[:, 1] / MAX_DIST


# =====================================================================
# 2. IMPLEMENTAÇÃO DO ZERO: PERCEPTRON DE ROSENBLATT
# =====================================================================
class PerceptronDoZero:
    def __init__(self, taxa_aprendizado=0.1, epocas=50):
        self.taxa = taxa_aprendizado
        self.epocas = epocas
        self.pesos = np.zeros(2) # [w_vida, w_distancia]
        self.bias = 0.0          # limiar inicial
        
    def somatorio(self, x):
        # Combinação linear: (x1 * w1) + (x2 * w2) + bias
        return np.dot(x, self.pesos) + self.bias
        
    def ativacao(self, soma):
        # Função degrau de Heaviside: se soma >= 0 -> 1, senao -> 0
        return 1 if soma >= 0 else 0
        
    def prever(self, x):
        return self.ativacao(self.somatorio(x))
        
    def treinar(self, X, y):
        print("=== INICIANDO TREINAMENTO: PERCEPTRON DO ZERO ===")
        for epoca in range(self.epocas):
            erros = 0
            for i in range(len(X)):
                previsao = self.prever(X[i])
                erro = y[i] - previsao # 0 se acertou, 1 ou -1 se errou
                
                # Regra de atualização do Perceptron (sem derivadas complexas!)
                if erro != 0:
                    self.pesos += self.taxa * erro * X[i]
                    self.bias += self.taxa * erro
                    erros += 1
                    
            print(f"Epoca {epoca+1:02d} -> Erros de decisao cometidos: {erros}")
            
            # Se não cometeu erros na rodada inteira, convergiu!
            if erros == 0:
                print(f"[SUCESSO] Perceptron convergiu perfeitamente na epoca {epoca+1}!\n")
                break


# =====================================================================
# 3. TREINANDO O MODELO DO ZERO E O MODELO DO SCIKIT-LEARN
# =====================================================================
# A) Nosso modelo artesanal
modelo_zero = PerceptronDoZero(taxa_aprendizado=0.1, epocas=50)
modelo_zero.treinar(X, y)

# B) Modelo equivalente usando Scikit-Learn
modelo_sklearn = SklearnPerceptron(max_iter=50, eta0=0.1, random_state=42)
modelo_sklearn.fit(X, y)
print("=== TREINAMENTO SCIKIT-LEARN CONCLUÍDO COM SUCESSO! ===")

# Desempenho geral
acertos_zero = np.sum(np.array([modelo_zero.prever(x) for x in X]) == y)
acuracia_zero = (acertos_zero / len(y)) * 100

acertos_sk = np.sum(modelo_sklearn.predict(X) == y)
acuracia_sk = (acertos_sk / len(y)) * 100

print(f"\n[DESEMPENHO NO TREINO - {nome_modo}]")
print(f"  -> Acuracia Perceptron do Zero: {acuracia_zero:.1f}% ({acertos_zero}/{len(y)} acertos | {len(y)-acertos_zero} erros)")
print(f"  -> Acuracia Scikit-Learn:       {acuracia_sk:.1f}% ({acertos_sk}/{len(y)} acertos | {len(y)-acertos_sk} erros)")


# =====================================================================
# 4. TESTE COMPARATIVO: O CASO DO BANDIDO DO SKYRIM
# =====================================================================
cenarios_teste = [
    ("Bandido do Skyrim (Meme)", 10, 2),  # 10% vida, colado a 2m do Dragonborn
    ("Bandido Arqueiro",         15, 28), # 15% vida, mas a 28m de distância (seguro!)
    ("Guerreiro Forte",          85, 3),  # 85% vida, colado no jogador
    ("Guerreiro Cauteloso",      40, 10), # 40% vida, 10 metros
]

print("\n================== RESULTADOS DOS TESTES ==================")
for nome, vida, dist in cenarios_teste:
    x_teste = np.array([vida / MAX_VIDA, dist / MAX_DIST])
    
    decisao_zero = modelo_zero.prever(x_teste)
    decisao_sklearn = modelo_sklearn.predict([x_teste])[0]
    
    acao_zero = "ATACAR!" if decisao_zero == 1 else "FUGIR / RECUAR!"
    acao_sk = "ATACAR!" if decisao_sklearn == 1 else "FUGIR / RECUAR!"
    
    print(f"* {nome:25} | Vida: {vida:2}% | Dist: {dist:2}m")
    print(f"    -> Modelo do Zero:    {acao_zero}")
    print(f"    -> Scikit-Learn:      {acao_sk}")
print("===========================================================\n")


# =====================================================================
# 5. MODO INTERATIVO: TESTE AO VIVO COM A TURMA / PROFESSOR
# =====================================================================
ponto_interativo = None

print("=" * 60)
print("     [MODO INTERATIVO - TESTE AO VIVO COM A BANCA]          ")
print("=" * 60)
print("Quer testar um cenario sugerido pelo professor/colegas agora?")
resp = input("Pressione [ENTER] para testar ou digite 'n' para pular: ").strip().lower()

if resp != 'n':
    try:
        entrada_vida = input("-> Digite a Vida do Inimigo (0 a 100%): ").strip()
        entrada_dist = input("-> Digite a Distancia ate o Jogador (metros): ").strip()
        
        if entrada_vida and entrada_dist:
            v_val = float(entrada_vida)
            d_val = float(entrada_dist)
            
            x_custom = np.array([v_val / MAX_VIDA, d_val / MAX_DIST])
            dec_zero = modelo_zero.prever(x_custom)
            dec_sk = modelo_sklearn.predict([x_custom])[0]
            
            res_zero = "ATACAR!" if dec_zero == 1 else "FUGIR / RECUAR!"
            res_sk = "ATACAR!" if dec_sk == 1 else "FUGIR / RECUAR!"
            
            print("\n---------------- RESULTADO DO TESTE AO VIVO ----------------")
            print(f"Inimigo com Vida: {v_val}% e Distancia: {d_val}m")
            print(f">>> Decisao (Perceptron do Zero): {res_zero}")
            print(f">>> Decisao (Scikit-Learn):       {res_sk}")
            print("------------------------------------------------------------\n")
            
            ponto_interativo = (v_val, d_val, res_zero)
    except ValueError:
        print("[Aviso] Valor numerico invalido digitado. Seguindo para o grafico...")


# =====================================================================
# 6. GERANDO O GRÁFICO VISUAL DA FRONTEIRA DE DECISÃO
# =====================================================================
plt.figure(figsize=(10, 6.5))

# Plotando os dados de treinamento
plt.scatter(dados_brutos[y == 0][:, 0], dados_brutos[y == 0][:, 1], 
            color='#e74c3c', s=110, label='Treino: Fugir / Recuar (0)', edgecolors='black', alpha=0.9)
plt.scatter(dados_brutos[y == 1][:, 0], dados_brutos[y == 1][:, 1], 
            color='#2ecc71', s=110, label='Treino: Atacar / Lutar (1)', edgecolors='black', alpha=0.9)

# 1) Calculando a reta de separação linear do MODELO DO ZERO (w1*x1 + w2*x2 + b = 0):
w1 = modelo_zero.pesos[0] / MAX_VIDA
w2 = modelo_zero.pesos[1] / MAX_DIST
b = modelo_zero.bias

vidas_linha = np.linspace(0, 100, 100)
dist_linha = -(w1 * vidas_linha + b) / w2
plt.plot(vidas_linha, dist_linha, color='#2980b9', linestyle='--', linewidth=2.5, 
         label='Fronteira: Modelo do Zero')

# 2) Calculando a reta de separação linear do SCIKIT-LEARN:
w1_sk = modelo_sklearn.coef_[0][0] / MAX_VIDA
w2_sk = modelo_sklearn.coef_[0][1] / MAX_DIST
b_sk = modelo_sklearn.intercept_[0]
dist_linha_sk = -(w1_sk * vidas_linha + b_sk) / w2_sk
plt.plot(vidas_linha, dist_linha_sk, color='#e67e22', linestyle=':', linewidth=2.5, 
         label='Fronteira: Scikit-Learn')

# Destaque para o Bandido do Skyrim (Estrela Amarela)
plt.scatter(10, 2, color='#f1c40f', s=280, marker='*', edgecolors='black', 
            label='Bandido do Skyrim (10% HP, 2m) -> FOGE!', zorder=6)

# Destaque para o Arqueiro com pouca vida mas longe (Triângulo Roxo)
plt.scatter(15, 28, color='#9b59b6', s=200, marker='^', edgecolors='black', 
            label='Bandido Arqueiro (15% HP, 28m) -> ATACA!', zorder=6)

# Se o professor ou a turma realizou um teste interativo, destaca no gráfico!
if ponto_interativo is not None:
    cor_teste = '#2ecc71' if 'ATACAR' in ponto_interativo[2] else '#e74c3c'
    plt.scatter(ponto_interativo[0], ponto_interativo[1], 
                color=cor_teste, s=320, marker='X', edgecolors='white', linewidths=2.5,
                label=f'Teste da Turma ({ponto_interativo[0]:.0f}% HP, {ponto_interativo[1]:.0f}m) -> {ponto_interativo[2]}', zorder=7)

plt.title('IA de Sobrevivencia para NPCs em RPG (Perceptron Simples)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Vida do Inimigo (%)', fontsize=12, fontweight='bold')
plt.ylabel('Distancia ate o Jogador (metros)', fontsize=12, fontweight='bold')
plt.xlim(0, 105)
plt.ylim(0, 36)
plt.grid(True, linestyle=':', alpha=0.6)
# Legenda posicionada no canto superior direito para NÃO cobrir o triângulo do arqueiro!
plt.legend(loc='upper right', fontsize=9.5, framealpha=0.95)
plt.tight_layout()

# Salva arquivo e abre janela interativa
plt.savefig('grafico_skyrim.png', dpi=150)
print("[OK] Grafico gerado com sucesso! Abrindo janela visual...")
plt.show()

