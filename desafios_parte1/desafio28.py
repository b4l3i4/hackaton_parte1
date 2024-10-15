#recebe a placa do veículo
placa = (input('Informe a os ultimos quatro números da sua placa:  '))
ut = int(placa[-1])

#define a data de vencimento do ipva
if ut == 0:
    print('Sua placa vencerá em janeiro')
elif ut == 1:
    print('Sua placa vencerá em fevereiro')
elif ut == 2:
    print('Sua placa vencerá em março')
elif ut ==3:
    print('Sua placa vencerá em abril')
elif ut == 4:
    print('Sua placa vencerá em maio')
elif plac == 5:
    print('Sua placa vencerá em junho')
elif ut == 6:
    print('Sua placa vencerá em julho')
elif ut == 7:
    print('Sua placa vencerá em agosto')
elif ut == 8:
    print('Sua placa vencerá em setembro')
else:
    print('Sua placa vencerá em outubro')
