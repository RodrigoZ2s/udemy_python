try:
    numero = int(input("Digite um número: "))
    print("Número válido.")
except ValueError:
    print("Valor inválido, tente digitar apenas números.")
