'''
Construa um algoritmo que determine (imprima) se um dado número N inteiro (recebido
através do teclado) é PAR ou ÍMPAR.

'''
# determinar as variaveis pelo usuario
num = int(input('Insira um número: '))
# determinar se é par ou impar
if num / 2:
    print(f'O {num} é par.')
else: 
    print(f'O {num} é impar.')

# PRONTO