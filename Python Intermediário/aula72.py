def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero 
    return total

print(multiplicar(1, 2, 3))

def parImpar(numero):
    if numero % 2 == 0:
        return f"{numero} é par!"
    return f"{numero} é impár!"

print(parImpar(3))