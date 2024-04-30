#IF (condição)

#Exemplo


nome = input("Digite o nome: ")

idade = int(input("Digite a idade: "))

# (SE) ***':' significa 'então'***
if idade >= 65:
    print("O paciente " + nome + " possui atendimento prioritário! ")
# (SE NÃO)
else:
    print("O paciente " + nome + " não possui atendimento prioritário! ")

