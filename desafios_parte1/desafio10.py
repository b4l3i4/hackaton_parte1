
n = float(input('Digite um número positivo maior que 0: '))

if n > 0:
    quadrado = n ** 2
    cubo = n ** 3
    raiz1 = n ** 0.5
    raiz2= n ** (1/3)

    print(f'A) {quadrado}')
    print(f'B) {cubo}')
    print(f'C) {raiz1}')
    print(f'D) {raiz2}')
else:
    print(f'|{29*'='}|\n|O número deve ser maior que 0|\n|{29*'='}|')








