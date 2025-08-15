# Exercício 1 – Multiplicação de vários números
# Escreva uma função que receba quantos números o usuário quiser e retorne o dobro do produto deles usando multiplicar.
# Teste com: (2, 3, 4) → resultado esperado: 48

def multiplicador(*args):
    resultado = 1
    for numero in args:
       resultado = resultado * numero
    return resultado * 2

print(multiplicador(2, 3, 4))