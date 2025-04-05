"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
    escolha = input("Deseja continuar? [S] [N]: ")
    if escolha == "S":
        nome = input("Digite seu nome: ")
        print(f"Seu nome é {nome}")
    else:
        break

print("Acabou")