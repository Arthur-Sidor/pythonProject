equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"s\" para continuar: ").upper()


for indice in range(0, len(equipamentos)):
    print("\nEquipamento..:", (indice + 1))
    print("Nome...........:", equipamentos[indice])
    print("Valor..........:", valores[indice])
    print("serial.........:", seriais[indice])
    print("departamento...:", departamentos[indice])