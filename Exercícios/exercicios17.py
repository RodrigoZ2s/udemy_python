# Exercício 2 – Par ou ímpar estendido
# Crie uma função que receba uma lista de números e retorne uma lista de mensagens dizendo se cada número é par ou ímpar, usando parImpar.

# Exemplo: [1, 2, 3] → ['1 é ímpar!', '2 é par!', '3 é ímpar!']

def parImpar(lista):
    resultado = []
    for numero in lista:
        if numero % 2 == 0:
            resultado.append(f"{numero} é par")
        else:
            resultado.append(f"{numero} é ímpar")
    return resultado

print(parImpar([1, 2, 3]))
            