
valor_carro = float(input("Digite o valor do carro: "))

preco_final_avista = valor_carro *0.8


parcelas = [6, 12, 18, 24, 30, 36 , 42, 48, 54, 60]

for num_parcelas in parcelas:

    if num_parcelas == 6:
        acrescimo_percentual = 0.03
    else:
        acrescimo_percentual =(num_parcelas / 6) * 0.03

    preco_final_parcelado = valor_carro * (1 + acrescimo_percentual)

    valor_parcela = preco_final_parcelado / num_parcelas

    print(f"Quantidade de Parcelas: {num_parcelas}")
    print(f"Preço Final: R${preco_final_parcelado:.2f}")
    print(f"Valor da Parcela: R${valor_parcela:.2f}")
    print()
