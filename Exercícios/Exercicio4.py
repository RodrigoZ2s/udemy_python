print("Digite 3 notas \n")

try:
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
    n3 = float(input("n3: "))

    media = (n1 + n2 + n3) / 3

    print(f"Média: {media:.2f}")
    if media < 5:
        print("Reprovado")
    elif media < 7:
        print("Recuperação")
    else:
        print("Aprovado")
except ValueError:
    print("Você não digitou um número válido.")