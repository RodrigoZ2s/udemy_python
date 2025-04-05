"""
 Flag (Bandeira) -> Marcar um local
 None -> Não valor
 is e is not -> é ou não é (Tipo, valor, indentidade)
 id -> identidade
"""

# v1 = "a"
# v2 = "b"

# print(id(v1))
# print(id(v2))

condicao = False
passou_no_if = None # <- Variável sem valor atribuido

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça algo")

print(passou_no_if, passou_no_if is None) # <- Fala que a variável ainda é None
print(passou_no_if, passou_no_if is not None) # <- Fala que a variável não é None
