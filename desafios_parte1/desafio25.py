'''
Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.

'''
# criar a lista com as vogais
vogal = ['a', 'e', 'i', 'o', 'u']
# o usuario escolhe uma letra
letra = input('insira uma letra: ')
# determinar se é vogal ou consoante
if letra in vogal:
    print(f'A {letra} é uma vogal.')
else:
    print(f'A {letra} é uma consoante.')

# PRONTO