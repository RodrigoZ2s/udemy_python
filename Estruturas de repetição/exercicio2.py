positivo = 0
respostas = []

while positivo <= 0:
    positivo = int(input("Digite um número positivo: "))
    respostas.append(positivo)

    if positivo > 0:
        print("Você digitou um número positivo")  
        break
    else:
        print(f"{positivo} não é um valor positivo...")

print(f"Valores digitados: {respostas}")

