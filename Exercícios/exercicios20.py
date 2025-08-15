# Exercício 5 – Produto condicionado
# Crie uma função que receba *args e um parâmetro multiplicar_pares=True/False.
# Se True → multiplica apenas os pares
# Se False → multiplica todos
# Teste com (1, 2, 3, 4) e os dois valores de multiplicar_pares.

def produtoCondicionado(*args, multiplicar_pares=True):
    total = 1
    for numero in args:
        if multiplicar_pares == True:
            if numero % 2 == 0:
                total *= numero
        else:
            total *= numero
    return total
    
print(produtoCondicionado(1, 2, 3, 4, multiplicar_pares=True))

                