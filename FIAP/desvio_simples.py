#Pedir que o usuário digite o nome de quem ta devendo
nome= input("Informe o nome: ")

#Pedir que o usuário digite a dívida

valor = float(input("Digite o valor da divida: "))

if valor <500:
    print("Ta deveno!!", valor)
elif valor >1000:
    print("Vai pagar com a vida!", valor)
else: print("Ta suave! ", valor)