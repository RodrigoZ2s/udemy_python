def contar_vogais(palavra):
    resultado = 0
    for letra in palavra.lower():
        if letra in "aeiou":
            resultado += 1
    return resultado

print(contar_vogais("programacao"))