with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()

print("Tipo de dado da variável conteudo:", type(conteudo))
print("\nConteúdo do arquivo:\n", conteudo)
