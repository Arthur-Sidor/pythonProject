# Pedir idade do aluno
idade = int(input("Por favor, informe a idade do aluno: "))
# Verificar se o aluno é maior de idade ou menor de idade

if idade <18:
    print("Aluno é menor de idade e tem", idade,"anos")
elif idade >65:
    print("Aluno é um dinossauro e tem", idade,"anos")
else:
    print("Aluno é maior de idade e tem", idade,"anos")
