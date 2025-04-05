import os

lista = []

while True:
    print("Selecione uma opção: ")
    escolha = input("[i]nserir [a]pagar [l]istar: ").lower()
    
    escolhas_permitidas = "ial"

    if escolha not in escolhas_permitidas:
        print("Escolha uma opção válida.")
        continue

    if len(escolha) > 1:
        print("Escolha apenas uma opção.")
        continue

    if escolha == "i":
        os.system("cls")
        item = input("Digite o item que deseja inserir: ")
        lista.append(item)

    elif escolha == "a":
        os.system("cls")
        try:
            if not lista:
                print("A lista está vazia.")
            else:
                apagar = int(input("Item que deseja apagar: "))
                os.system("cls")
                item_deletado = lista[apagar]
                del lista[apagar]
                print(f"[{item_deletado}] foi removido da sua lista.")
        except:
            print("Item não encontrado ou inexistente.")
    else:
        if not lista:
            print("A lista está vazia.")
        else:
            os.system("cls")
            for indice, item in enumerate(lista):
                print(f"{indice} {item}")
