'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
• o novo peso, caso a pessoa engorde 15% sobre o seu peso original;

• o novo peso, caso a pessoa emagreça 20% sobre o seu peso original.

'''
# Entrada: Recebe o peso da pessoa
peso = float(input("Digite o seu peso em kg: "))

# Cálculos
novo_peso_engordar = peso + (peso * 0.15)
novo_peso_emagrecer = peso - (peso * 0.20)

# Saída: Mostra os resultados
print(f"Se você engordar 15%, seu novo peso será: {novo_peso_engordar:.2f} kg")
print(f"Se você emagrecer 20%, seu novo peso será: {novo_peso_emagrecer:.2f} kg")