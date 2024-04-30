tabela_juros_parcelas = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

valor_divida = float(input("Digite o valor da dívida: "))

for parcelas, juros in tabela_juros_parcelas.items():
    total = valor_divida * (1 + juros / 100)
    valor_parcela = total / parcelas
    print(f"Total: R${total:.2f} Juros: R${total - valor_divida:.2f} Número de parcelas: {parcelas} Valor da Parcela: R${valor_parcela:.2f}")
