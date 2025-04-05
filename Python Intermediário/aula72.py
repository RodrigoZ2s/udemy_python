def multiplo(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
    
total_multiplicado = multiplo(1, 2, 3, 4)
print(total_multiplicado)


def par_ou_impar():
        numero_input = int(input("Digite um número: "))
        resposta = numero_input % 2 == 0
        if resposta:
            return f"{numero_input} é par"         
        return f"{numero_input} é ímpar"
            

print(par_ou_impar())



