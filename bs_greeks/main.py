import calculabs
from geraResultado import criaRelatorio

ativo = input("Informe o ativo: ")

# Selecionando o tipo da opção entre Call e Put
tipo = input("Tipo de opção (Call: 'c' e Put: 'p'): ")
tipo = tipo.lower()
while tipo != 'c' and tipo != 'p':
    print("\nOpção inválida. Digite 'c' para Call e 'p' para Put.\n")
    tipo = input("Tipo de opção: ")

# Criando seleção da taxa de juros
'''
Por default a taxa de juros será 13.75%, predominante atualmente.
Caso o uruário queira inserir outra taxa, pode fazê-lo, digitando 'N'
e inserindo manualmente.
'''
sn = input("A taxa de Juros atual é 13.75%? (Sim: 'S' e Não: 'N')")
if sn.lower() == 's':
    r = 0.1375
elif sn.lower() == 'n':
    r = float(input('Taxa de Juros: '))
else:
    print("Valor inválido. Digite 'S' para Sim e 'N' para Não")

# Incluindo demais parâmetros
S = float(input('Preço Atual: '))
X = float(input('Preço de Exercício: '))
sigma =  float(input('Volatilidade Implícita: '))
T = int(input('Tempo Restante para o Exercício: '))
T = T/252

# Realizando os cálulos
preco = calculabs.bs(r, S, X, T, sigma, tipo="c")
delta = calculabs.delta(r, S, X, T, sigma, tipo="c")
gama = calculabs.gama(r, S, X, T, sigma, tipo='c')
vega = calculabs.vega(r, S, X, T, sigma, tipo='c')
theta = calculabs.theta(r, S, X, T, sigma, tipo='c')
rho = calculabs.rho(r, S, X, T, sigma, tipo='c')
moneyness, vi, ve = calculabs.moneyness(S, X, preco, tipo)

criaRelatorio(ativo, X, S, preco, delta, gama, theta, vega, rho, moneyness, vi, ve, tipo)