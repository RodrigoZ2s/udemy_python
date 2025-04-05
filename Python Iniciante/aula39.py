nome = input("Digite seu nome: ")
contador = 0
nova_string = ""

while contador < len(nome):
    nova_string += "*" + nome[contador]
    contador += 1
print(f"Nova string: {nova_string}")
