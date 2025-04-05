"""
Introdução ao desempacotamento
"""

nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
print(nome1)

nome1, *resto = ["Maria", "Helena", "Luiz"] # Armazena valores restantes
print(nome1, resto)

nome1, *_ = ["Maria", "Helena", "Luiz"] # Formato convencional de armazenar valores restantes
print(nome1)
