nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

try:
    idade_int = int(idade)
    print(f" seu nome: {nome}\n sua idade: {idade}")
    print(f"O dobro da sua idade é: {idade_int * 2} ")
except:
    print("Você não digitou um número válido.")
