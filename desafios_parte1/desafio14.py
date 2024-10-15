'''
Escreva um algoritmo que leia a base e a altura de um retângulo e calcule a sua área, o
seu perímetro e a sua diagonal, sabendo que:

'''
# Entrada: base e altura do retângulo
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Cálculos
area = base * altura  # Área do retângulo
perimetro = 2 * (base + altura)  # Perímetro do retângulo
diagonal = (base * 2 + altura * 2) ** 0.5  # Diagonal do retângulo (teorema de Pitágoras)

# Exibição dos resultados
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
print(f"Diagonal: {diagonal:.2f}")