"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def first_duplicate(lista_de_inteiros):
    numero_verificado = set()

    for numero in lista_de_inteiros:
        if numero in numero_verificado:
            return numero
        
        numero_verificado.add(numero)

    return -1

# for lista in lista_de_listas_de_inteiros:

#     print(
#         lista,
#         first_duplicate(lista)
#     )

# Exercícios Intermediários de set - 1. Remover duplicados mantendo a ordem

# Crie uma função que recebe uma lista de inteiros e retorna a lista sem duplicados na ordem em que aparecem.

# Dica: use um set para rastrear o que já viu, mas não para armazenar a lista final.

lista_de_listas_de_inteiros2 = [
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
]

def remove_duplicates(listas_de_inteiros):
    duplicados = set()
    lista_sem_duplicados = []
    numeros_removidos = []

    for lista in listas_de_inteiros:
        for numero in lista:
            
            if numero not in duplicados:
                lista_sem_duplicados.append(numero)

            else:
                numeros_removidos.append(numero)

            duplicados.add(numero)
    return lista_sem_duplicados, numeros_removidos


# resultado, removidos = remove_duplicates(lista_de_listas_de_inteiros2)
# print(resultado)
# print(f"{removidos} foram removidos")

# 2. Todos os duplicados

# Crie uma função que retorna uma lista com todos os elementos que aparecem mais de uma vez, sem repetir números na saída.

# Exemplo:

entrada = [1, 2, 2, 2, 3, 3, 1, 4]
# saida = [1, 2]

def allDuplicates(lista):
    checked_numbers = set()
    elementos_duplicados = []

    for number in lista:

        if number in checked_numbers:
            if number not in elementos_duplicados:
                elementos_duplicados.append(number)

        checked_numbers.add(number)

    return elementos_duplicados

# print(allDuplicates(entrada))

# 3. Interseção de múltiplas listas

# Crie uma função que recebe uma lista de listas de inteiros e retorna os elementos que aparecem em todas as sublistas.

# Exemplo:

#  entrada = [[1, 2, 3], [2, 3, 4], [0, 2, 3]]
# saida = [2, 3]

def intersectionList(listas_de_inteiros):
    
    lista_atual = set(listas_de_inteiros[0])

    for lista_entrada in listas_de_inteiros[1:]:
        lista_atual ^= set(lista_entrada)

    return lista_atual

     

# print(intersectionList([[1, 2, 3], [2, 3, 4]]))






