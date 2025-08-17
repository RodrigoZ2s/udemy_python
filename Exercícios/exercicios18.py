# Exercício 3 – Multiplicar apenas números pares
# Modifique a função multiplicar para multiplicar apenas os números pares recebidos via *args.
# Teste com: (1, 2, 3, 4) → resultado esperado: 8 (2 * 4)

def multiplicarPares(*args):
    total = 1
    for numero in args:
        if numero % 2 == 0:
            total *= numero
    if total == 1:
        return 0
    return total

print(multiplicarPares(1, 2, 3, 4))
            
