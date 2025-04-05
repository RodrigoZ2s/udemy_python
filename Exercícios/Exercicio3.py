idade = input("Sua idade: ")

try:
    idade_int = int(idade)
    if idade_int < 18:
        print("Você é menor de idade")
    elif idade_int < 60:
        print("Você é um adulto")  
    else:
        print("Você é um idoso")
except ValueError:
    print("Você não digitou um número válido.")