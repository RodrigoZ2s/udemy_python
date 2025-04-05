"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = iter("Luiz") # __inter__() # função que armazena os valores interáveis
# print(next(texto)) # chama o valor disponível dentro do "iter"

# for letra in texto    
texto = "Luiz" # iterável

# iterador = iter(texto) # iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)


