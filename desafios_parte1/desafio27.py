'''
27. A biblioteca Branca Adjuto Botelho do IFTM -- Campus Paracatu deseja criar um
programa que leia o nome do livro que será emprestado, o tipo de usuário (professor ou
aluno) e a data de empréstimo do livro. O programa deve imprimir um recibo conforme
mostrado abaixo:

➢ Nome do livro: XXXXX
➢ Tipo de usuário: XXXXX
➢ Data do empréstimo: XXXXX
➢ Data da devolução: XXXXX

* O programa deve considerar que o professor tem vinte dias para devolver o livro e
o aluno somente quinze dias. Escreva esse algoritmo.

'''

# fiz um menu "interativo"

print(20*'*', 'Biblioteca', 20*'*')
livro = input('➢ Nome do livro: ')
usuario = input('➢ Tipo de usuário: ')
emprestimo = input('➢ Data do empréstimo: ')

# deterninar a data de entrega de acordo com o usuário

if usuario == 'professor':
    print('➢ Data da devolução: Você têm até 20 dias para a devolução.')
    print(52*'*')
    d = 20
    devolucao = d
elif usuario == 'aluno':
    print('➢ Data da devolução: Você têm até 15 dias para evolução.')
    print(52*'*')
    d = 15
    devolucao = d

# PRONTO