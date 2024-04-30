dias_votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

num_colaboradores = int(input("Quantos colaboradores irão participar da votação? "))


for _ in range(num_colaboradores):
    dia = input("Digite o dia da semana de sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira ou sexta-feira): ").lower()
    dias_votos[dia] += 1


dia_escolhido = max(dias_votos, key=dias_votos.get)


print(f"O dia escolhido pelos colaboradores para a realização das lives é: {dia_escolhido.capitalize()}, com {dias_votos[dia_escolhido]} voto(s).")
