nome = input("Nome: ")
try:
    idade = int(input("idade: "))
    altura = float(input("Altura: "))

    print(f"Olá, seu nome é {nome}! Você tem {idade} anos e mede {altura:.2f}m de altura")
except ValueError:
    print("Você não digitou um valor válido")
    print("Certifique-se de digitar apenas números")
