tabuada = int(input("Número que deseja ver a tabuada:  "))
fim_tabuada = int(input("Número que deseja parar: "))
contador = 1

while contador <= fim_tabuada:
    print(f"{tabuada} X {contador} = {tabuada * contador}")
    contador += 1

print("Fim da tabuada")


