numero = 0

while True:
    numero = int(input("Digite um número positivo: "))
    if numero >= 0:
        print(numero)
    else:
        print("Fim da execução!")
        break
