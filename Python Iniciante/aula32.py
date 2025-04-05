"""
try:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar")
except ValueError:
    print("Você não digitou um número inteiro.")
"""

"""
try:
    hora = float(input("Informe seu horário atual: "))
    if hora >= 0 and hora <= 11:
        print("Bom dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite")
except ValueError:
    print("Você não digitou um horário válido.")
"""

"""
nome = input("Digite seu nome: ")
letras = len(nome)

if letras <= 4:
    print("Seu nome é curto")
elif letras <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
"""
