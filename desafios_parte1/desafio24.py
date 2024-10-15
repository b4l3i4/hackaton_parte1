'''
24. Faça um algoritmo que simule uma calculadora simples. O usuário deve escolher uma
operação básica: adição, subtração, multiplicação, divisão e potenciação. Feito isso, o
usuário deve entrar com dois números quaisquer e o programa deve realizar a operação
mostrando o resultado correto.

'''
# determinar os números pelo usuário
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))
# calculos simples.
adicao = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2

print(f'A soma dos números é: {adicao}, a subtração é: {sub}, a multiplicação é: {multi}, a divisão é: {div}')

# PRONTO