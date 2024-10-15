'''
23. Escreva um programa que determine o grau de obesidade de uma pessoa, sendo
fornecido o peso e a altura da pessoa. O grau de obesidade é determinado pelo índice da
massa corpórea (IMC = Peso / Altura2) através da tabela abaixo:

'''
# determinar as variáveis pelo usuário
altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))
# calculo do IMC
IMC = peso / (altura ** 2)

print('Sua massa corpórea é: ', IMC)

# PRONTO