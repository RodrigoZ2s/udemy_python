"""
Introdução ao try/except
try -> tentar executar um código
except -> ocorreu um erro ao tentar executar
try -> não deixa o código quebrar se der erro
"""
numero_str = input(
    "Vou dobrar o número que vc digitar: "
)
try:
    numero_float = float(numero_str)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
except:
    print("Você não digitou apenas números.")


# if numero_str.isdigit(): # Função que recebe apenas números
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
# else:
#     print("Você não digitou apenas números.")

