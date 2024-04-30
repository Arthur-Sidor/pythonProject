tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número", tabuada)
for valor in range(1, 11):
    resultado = tabuada * valor
    print(str(tabuada) + " x " + str(valor) + " = " + str(resultado))
