print("---CALCULADORA---")
print("tipo de cálculo: ")
calculo = input("[1] Multiplicação \n[2] Divisão \n[3] Subtração \n:")

if calculo not in ("1", "2", "3"):
    print("Você não escolheu uma opção válida")
else: 
    if calculo == '1':
        print("Número:", end="")
        num = float(input(" "))
        print(f"{num} X ", end="")
        num2 = float(input(""))
        print(f"{num} X {num2} = {num * num2:.2f}")
    if calculo == '2':
        print("Número:", end="")
        num = float(input(" "))
        print(f"{num} ÷ ", end="")
        num2 = float(input(""))
        print(f"{num} ÷ {num2} = {num / num2:.2f}")
    if calculo == '3':
        print("Número:", end="")
        num = float(input(" "))
        print(f"{num} - ", end="")
        num2 = float(input(""))
        print(f"{num} - {num2} = {num - num2:.2f}")