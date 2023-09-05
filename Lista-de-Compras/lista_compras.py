lista_compras = []


def inserir_item(item):
    lista_compras.append(item)
    print(f"\tItem adicionado: {item}")


def apagar_item(item):
    lista_compras.pop(item)
    print(f"\tO item {item} foi apagado da lista!")


def listar_itens():
    if lista_compras == []:
        print("\tA lista está vazia!")
    for indice, item in enumerate(lista_compras):
        print(indice, item.upper())


while True:
    opcao = input("""\tSelecione uma opção:
    [i]nserir [a]pagar [l]istar\n\t\t""").lower()
    if opcao not in ['i', 'a', 'l']:
        print("\tOpção inválida")
        continue

    if opcao == 'i':
        while True:
            item = input("\tDigite o item a ser adicionado: ")
            if item.isalpha() or ' ' in item:
                inserir_item(item)
                break
            else:
                print("\tDigite apenas letras.")
            continue
    elif opcao == 'a':
        try:
            item = int(input("Digite o índice do item a ser apagado: "))
            apagar_item(item)
        except ValueError:
            print("\tDigite apenas números")
            continue
        except IndexError:
            print("\tÍndice inexistente")
            continue
    elif opcao == 'l':
        listar_itens()
