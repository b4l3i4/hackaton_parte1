# Entrada do percurso, tipo de carro e preço do combustível
percurso = float(input("Digite o percurso da viagem (em km): "))
tipo_carro = input("Digite o tipo de carro (A, B ou C): ").upper()
preco_combustivel = float(input("Digite o preço do litro do combustível (em reais): "))

# Determinação do consumo por tipo de carro
if tipo_carro == 'A':
    consumo_por_km = 16
elif tipo_carro == 'B':
    consumo_por_km = 12
elif tipo_carro == 'C':
    consumo_por_km = 8
else:
    print("Tipo de carro inválido.")
    consumo_por_km = 0

# Cálculo do consumo total de combustível e valor da viagem
if consumo_por_km > 0:
    consumo_total = percurso / consumo_por_km
    valor_viagem = consumo_total * preco_combustivel

    # Saída do consumo e valor estimado
    print(f"O consumo estimado de combustível é: {consumo_total:.2f} litros")
    print(f"O valor estimado da viagem é: R$ {valor_viagem:.2f}")