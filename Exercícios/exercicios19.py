# Exercício 4 – Contagem de pares e ímpares
# Escreva uma função que receba qualquer quantidade de números e retorne quantos são pares e quantos são ímpares.
# Teste com: (1, 2, 3, 4, 5) → saída: "Pares: 2, Ímpares: 3"

def parImparCount(*args):
    contagem_par = 0
    contagem_impar = 0
    for numero in args:
        if numero % 2 == 0:
            contagem_par += 1
        else:
            contagem_impar += 1
    return f"Pares: {contagem_par}, Ímpares: {contagem_impar}"

print(parImparCount(1, 2, 3, 4, 5))
