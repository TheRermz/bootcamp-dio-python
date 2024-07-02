# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:


# TODO: Crie um loop para solicita os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":

itens = []
def adiciona_item():
    qtd_itens = 0
    while qtd_itens < 3:
        adiciona_item = input()
        itens.append(adiciona_item)
        qtd_itens +=1
    return itens


def main():
    # Exibe a lista de itens
    itens = adiciona_item()
    print("Lista de Equipamentos:")
    for item in itens:
        # Loop que percorre cada item na lista "itens"
        print(f"- {item}")

main()
