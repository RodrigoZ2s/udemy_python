"""
Interpolação básica de Strings
s - string
f - float
d e i - int
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Maconha"
preco = 1000.95897643
variavel = "%s, o preço é R$%.2f" %  (nome, preco)
print(variavel)