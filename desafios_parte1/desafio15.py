'''
Escreva um algoritmo que efetue o cálculo de uma prestação em atraso, sendo dados o
valor inicial da prestação, a taxa de juros e o tempo de atraso em dias. Utilize a fórmula
abaixo:

prestação = valor + [ valor * (taxa / 100) * tempo]

'''
# determinar as variaveis pelo usuario
taxa = float(input('Insira a taxa de juros: '))
tempo = float(input('Insira o tempo em dias: '))
valor = float(input('Insira o valor: '))
# calculo pela formula
prestacao = valor + (valor * (taxa / 100) * tempo)

print(prestacao)

# PRONTO