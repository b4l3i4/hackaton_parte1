'''
Solicite o nome e sobrenome de dois usuários e imprima o nome do primeiro com o
sobrenome do segundo e o nome do segundo com o sobrenome do primeiro.

'''
# Determinar as variáveis de acordo com o usuário
nome1 = input('Insira seu nome: ')
nome2 = input('Insira seu nome: ')
sobre1 = input(f'Insira seu sobrenome {nome1}: ')
sobre2 = input(f'Insira seu sobrenome {nome2}: ')
# inverter as variáveis
nometrocado1 = nome1 + sobre2
nometrocado2 = nome2 + sobre1

print(f'Os nomes trocados são: {nometrocado1} e {nometrocado2}')

# PRONTO