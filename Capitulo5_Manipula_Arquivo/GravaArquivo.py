#with open("teste.txt", "r") as arquivo:    ##"r" leitura     "w" escrita
  #  conteudo = arquivo.read()

#Dentro do with, não estamos mais utilizando o método read() e, sim, o método write(),
# que nos permite passar o conteúdo que queremos para dentro do arquivo.

#with open("teste.txt", "w") as arquivo:
 #   arquivo.write("Nunca foi tão fácil criar um arquivo.")


with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")