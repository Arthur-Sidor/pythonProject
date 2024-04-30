investimento = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI, 3 para LCA): "))
if investimento not in [1, 2, 3]:
    print("Tipo de investimento inválido.")
else:
    valor_resgate = float(input("Digite o valor a ser resgatado: "))
    dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

    if investimento == 1:  # CDB
        if dias <= 180:
            aliquota_ir = 22.5
        elif 181 <= dias <= 360:
            aliquota_ir = 20
        elif 361 <= dias <= 720:
            aliquota_ir = 17.5
        else:
            aliquota_ir = 15
    else:
        aliquota_ir = 0  # Isento de IR para LCI e LCA

    ir = (valor_resgate * aliquota_ir) / 100
    print(f"O imposto de renda a ser pago é de R$ {ir:.2f}")