#reecebe a palavra
p = input('Digite uma palavra: ')

#define a quantidade de letras
letras = len(p)

#faz a comparaçao para os devidos resultados
if letras % 2 == 0:
    print(f'A palavra "{p}" tem {letras} letras, que é um número par.')
else:
    print(f'A palavra "{p}" tem {letras} letras, que é um número impar.')