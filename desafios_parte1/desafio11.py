#solicita dois valores
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

#define como numero
n1 = int(n1)
n2 = int(n2)

#elevando ambos os números
calculo1 = n1 ** n2
calculo2 = n2 ** n1

#imprime o resultado
print(f'|{n1} elevado a {n2} = {calculo1}|\n|{n2} elevado a {n1} = {calculo2}|')