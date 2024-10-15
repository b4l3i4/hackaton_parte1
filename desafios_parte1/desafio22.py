#recebe o numero do usuario
d = input('Digite um número de 1 a 7: ')
dia = int(d)


#define a data conforme o dia que foi pedido
if dia == 1:
    print('1 corresponde ao dia de domingo!')
elif dia == 2:
    print('2 corresponde ao dia de segunda!')
elif dia == 3:
    print('3 corresponde ao dia de terça!')
elif dia == 4:
    print('4 corresponde ao dia de quarta!')
elif dia == 5:
    print('5 corresponde ao dia de quinta!')
elif dia == 6:
    print('6 corresponde ao dia de sexta!')
elif dia == 7:
    print('7 corresponde ao dia de sábado!')
else:
    print('Data inválida!')
    