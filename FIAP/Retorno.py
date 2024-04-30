def somar(valor1, valor2):
    soma = valor1 + valor2
    ## print (soma)
    return soma

primeiro_valor = float(input("Informe o primeiro valor: "))
segundo_valor = float(input("Informe o segundo valor: "))
soma = somar(primeiro_valor, segundo_valor)
media = soma/2
print (media)