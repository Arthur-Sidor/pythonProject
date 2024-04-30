inventario = {}
opcao = 0

while opcao != 4:
    opcao = int(input("Digite:\n<1> para registrar ativo\n<2> para persistir em arquivo\n<3> para exibir ativos armazenados\n<4> para sair\n"))

    if opcao == 1:
        resp = "S"
        while resp.upper() == "S":
            inventario[input("Digite o número patrimonial: ")] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")
            ]
            resp = input("Digite <S> para continuar ou qualquer outra tecla para voltar ao menu principal: ").upper()
    elif opcao == 2:
        with open("inventario.csv", "a+") as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
            print("Persistido com sucesso!")
    elif opcao == 3:
        try:
            with open("inventario.csv", "r") as inv:
                print(inv.read())
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except:
            print("Ocorreu um erro ao tentar ler o arquivo.")
    elif opcao == 4:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
