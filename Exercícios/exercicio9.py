letras = input("Digite uma frase: ")
i = 0
letra_mais_vezes = ""
quantidade_mais_vezes = 0

while i < len(letras):
    letra_atual = letras[i]
    quantidade_atual = letras.count(letra_atual)
    
    if quantidade_atual > quantidade_mais_vezes:
        quantidade_mais_vezes = quantidade_atual
        letra_mais_vezes = letra_atual

    i += 1
    
print(quantidade_mais_vezes, letra_mais_vezes)
    