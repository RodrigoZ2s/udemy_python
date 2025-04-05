"""
*args - convenção do python para receber múltiplos argumentos não nomeados em uma função
"""


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10))) # <- função de soma (sum)
