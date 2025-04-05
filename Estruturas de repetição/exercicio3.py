contador = int(input("Digite um número para contagem regressiva: "))
decrementação = int(input("Valor da decrementação: "))

while contador > 0:
    print(f"Contagem regressiva: {contador}")
    contador -= decrementação
print(f"Contagem regressiva: {contador}")
