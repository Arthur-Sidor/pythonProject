import math
num_transacao = int(input("Informe quantas transações você realizou ao longo do dia: "))
total_gasto = 0

for i in range(num_transacao):
    valor_transacoes = float(input(f"Informe o valor da transação {i+1}: "))
    total_gasto += valor_transacoes

print(f'O total gasto foi de {total_gasto}')
