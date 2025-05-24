import sys

# Generator expression, Iterables e Iterators em Python
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iter(iterable) # tem __iter__ e __next__

lista = [n for n in range(10000)] # Guarda tudo na memória
generator = (n for n in range(10000)) # Entrega apenas valores pedidos

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)