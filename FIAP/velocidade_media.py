#pedir a distancia da viagem

distancia = float(input("Digite a distancia percorrida: "))

#pedir o tempo da viagem

tempo = float(input("Digite o tempo da viagem: "))


#dividir a distância pelo tempo

velocidade_media = distancia / tempo

#Exibir resultado
print ("A velocidade média foi de {:.2f} km/h" .format(velocidade_media))

#ou

print (f"A velocidade média foi de {velocidade_media} km/h")