import os

lista_compras = []


def inserir_item(item):
    lista_compras.append(item)
    os.system('clear')
    print(f"\tItem adicionado: {item}")


def listar_itens():
    if lista_compras == []:
        print("\tA lista está vazia!")
    print("---------LISTA ATUAL---------")
    for indice, item in enumerate(lista_compras):
        print(f"\t{indice}: {item.upper()}")


def apagar_item(item):
    lista_compras.pop(item)
    print(f"\tO item {item} foi apagado da lista!")


while True:
    opcao = input("""\tSelecione uma opção:
    [i]nserir [a]pagar [l]istar\n\t\t""").lower()
    if opcao not in ['i', 'a', 'l']:
        print("\tOpção inválida")
        continue

    if opcao == 'i':
        os.system('clear')
        while True:
            item = input("\tDigite o item a ser adicionado: ")
            if item.isalpha() or ' ' in item:
                inserir_item(item)
                break
            else:
                print("\tDigite apenas letras.")
            continue
    elif opcao == 'a':
        if lista_compras == []:
            print("\tA lista está vazia!")
        else:
            print("---------LISTA ATUAL---------\n")
            for indice, item in enumerate(lista_compras):
                print(f"\t{indice}: {item.upper()}")
            try:
                item = int(input("Digite o índice do item a ser apagado: "))
                apagar_item(item)
                print("---------LISTA ATUAL---------\n")
                for indice, item in enumerate(lista_compras):
                    print(f"\t{indice}: {item.upper()}")
            except ValueError:
                print("\tDigite apenas números")
                continue
            except IndexError:
                print("\tÍndice inexistente")
                continue
    elif opcao == 'l':
        os.system('clear')
        listar_itens()
