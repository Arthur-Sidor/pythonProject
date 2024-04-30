usuarios ={}
print(usuarios)

usuarios = dict(chaves=["Chaves do 8", "24/12/2017", "Recep_01"], kiko=["Kiko do 7", "20/12/2017", "Raiox_03"])
print (usuarios)

#inserimos a florinda no dicionario (usuarios)
usuarios ["Florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]
print(usuarios)

print ("###---###")
print(usuarios.get("kiko"))
print(usuarios.get("chaves"))