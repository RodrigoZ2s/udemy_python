"""
split e join com list e str
split - divide uma string
join - une uma string
rstrip - corta o espaço da direita
lstrip - corta o espaço da esquerda
"""

frase = "Olha só que, coisa interessante"

lista_cruas = frase.split(',')
lista_frases = []

# lista_frases = frase.split(',') # Separa a partir do caractere 

for i, frase in enumerate(lista_cruas):
    lista_frases.append(lista_cruas[i].strip()) # Corta o espaço sobrando

frases_unidas = ', '.join(lista_frases) # Une uma string separada
print(frases_unidas)
