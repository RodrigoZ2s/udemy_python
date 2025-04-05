# Operadores in e not in
# Strings são iteráveis

#  0 1 2 3 4 5
#  o t a v i o
# -6-5-4-3-2-1

# nome = "Otávio"
# print(nome[2])
# print("á" in nome)
# print("á" not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite a letra que deseja encontrar: ")

if encontrar in nome:
    print(f"A letra {encontrar} foi encontrada no seu nome.")
else:
    print(f"A letra {encontrar} não foi encontrada.")
