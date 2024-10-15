'''
12. Sabe-se que:
1 pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1,760 jarda
• Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre
os resultados.
a) polegadas
b) jardas
c) milhas

'''
# Entrada: medida em pés
pes = float(input("Digite a medida em pés: "))

# Conversões
polegadas = pes * 12  # 1 pé = 12 polegadas
jardas = pes / 3      # 1 jarda = 3 pés
milhas = jardas / 1760  # 1 milha = 1760 jardas

# Exibição dos resultados
print(f"Polegadas: {polegadas}")
print(f"Jardas: {jardas}")
print(f"Milhas: {milhas}")