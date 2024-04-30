num_alimentos = int(input("Informe a quantidade de alimentos consumidos: "))

total_calorias = 0

for i in range(num_alimentos):
    calorias_alimento = float(input(f"Informe o número de calorias do alimento {i+1}: "))
    total_calorias += calorias_alimento

print(f'Total de calorias consumidas hoje: {total_calorias}')