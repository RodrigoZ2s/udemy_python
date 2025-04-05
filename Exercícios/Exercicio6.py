print("--- CALCULADORA DE IMC ---")

try:
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    imc = peso / (altura ** 2)

    print("--------------------------")
    print(f"Seu IMC: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso ideal.")
    elif imc <= 24.9:
        print("Peso ideal")
    elif 24.9 < imc <= 29.9:
        print("Acima do peso ideal")
    elif imc > 29.9:
        print("Muito acima do peso ideal")
except ValueError:
    print("Você não digitou um número válido. Tente novamente.")


