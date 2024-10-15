'''
19. Construa um algoritmo que imprima qual o menor e qual o maior valor de três números
lidos através do teclado.

'''

# Entrada dos três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determina o menor e o maior número
menor = min(num1, num2, num3)
maior = max(num1, num2, num3)

# Saída
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")