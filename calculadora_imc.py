# ==========================================
# Projeto: Calculadora de IMC
# Autor: Isabella
# Descrição: Programa em Python para calcular o Índice de Massa Corporal (IMC)
# ==========================================

print("=== CALCULADORA DE IMC ===")

# Entrada de dados do utilizador
peso = float(input("Digite o seu peso em kg (ex: 65.5): "))
altura = float(input("Digite a sua altura em metros (ex: 1.65): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibição do resultado arredondado para 2 casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")