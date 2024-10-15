'''
Faça um programa que receba o número de horas trabalhadas e o valor do salário-
mínimo, calcule e mostre o salário a receber, seguindo estas regras:

• a hora trabalhada vale a metade do salário-mínimo.
• o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor
da hora trabalhada.
• o imposto equivale a 3% do salário bruto.
• o salário a receber equivale ao salário bruto menos o imposto.

'''
# Entrada: número de horas trabalhadas e valor do salário mínimo

horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))

# Cálculos
valor_hora_trabalhada = salario_minimo / 2  # A hora trabalhada vale a metade do salário mínimo
salario_bruto = horas_trabalhadas * valor_hora_trabalhada  # Salário bruto
imposto = salario_bruto * 0.03  # Imposto de 3%
salario_receber = salario_bruto - imposto  # Salário a receber

# Exibição dos resultados
print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"Imposto: R${imposto:.2f}")
print(f"Salário a receber: R${salario_receber:.2f}")