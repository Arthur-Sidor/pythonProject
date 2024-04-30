#Uma loja concede descontos para compras pagas com cartão de crédito e com valor superior a R$100

valor_compra = float(input("Por favor, informe o total da compra: "))
forma_pagamento= int(input("ESCOLHA UMA FORMA DE PAGAMENTO\n1 - CARTÃO DE CRÉDITO \n2 - DINHEIRO\n3 - BOQUECARD\n4 - XERECARD\nInforme a forma adotada: "))
if valor_compra > 100 and forma_pagamento == 1:    #and- ambas verdadeiras     or- basta uma ser verdadeira
    valor_compra = valor_compra * 0.9
    print("O cliente tem direito a desconto!")
##  valor_compra * 0.9  significa 90% do valor informado
print(f"O valor da compra é de {valor_compra}")