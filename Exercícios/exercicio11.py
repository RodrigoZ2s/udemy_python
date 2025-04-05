texto = input("Digite um texto: ") # Solicita um texto
iterador = iter(texto) # Solicita o iterador

while True: # Enquanto a condição for verdadeira
    try:
        letra = next(iterador) # a letra vai receber o próximo iterador
        print(letra)
    except StopIteration:
        break