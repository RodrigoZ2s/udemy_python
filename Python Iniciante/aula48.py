"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# string = "ABCDE"
# # print(bool([])) # false
# # print(lista, type(lista))

# #         0     1       2       3    4
# lista = [123, True, "Maconha", 1.2, []]
# lista[-3] = "Makonha"
# del lista[2]
# print(lista)
# print(lista[2], type(lista[2]))

# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(50) # Adiciona algo a lista
# lista.pop() # Remove o último item da lista
# lista.append(60)
# ultimo_valor = lista.pop(3)
# lista.clear() # Limpa a lista
# lista.insert(0, 5) # Adiciona um item no índice escolhido (índice, item)
# print(lista, "Removido:", ultimo_valor)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_d)




