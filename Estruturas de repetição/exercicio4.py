contador = 0
multiplos = int(input("Deseja pular multiplos de: "))


while contador < 20:
    contador += 1

    if contador % multiplos == 0:
        continue
    else:
        print(f"Contagem: {contador}")

