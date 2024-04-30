nome=input("Digite o nome: ")
idade=int (input("Digite a idade: "))
doença_infectocontagiosa= input ("Suspeita de doença infectocontagiosa? ") .upper()
if idade >=65 :
    print("O paciente " + nome + " possui atendimento prioritário. ")
elif doença_infectocontagiosa=="SIM" :
    print("O paciente " + nome + " deve ser direcionado para a sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum.")

