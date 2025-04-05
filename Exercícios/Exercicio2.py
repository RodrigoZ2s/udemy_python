num1 = input("Primeiro número: ")
num2 = input("Segundo número: ")

try:
    num1_int = float(num1)
    num2_int = float(num2)
    print(f"Soma: {num1_int + num2_int}")
    print(f"Subtração: {num1_int - num2_int}")
    print(f"Multiplicação: {num1_int * num2_int}")
    print(f"Divisão: {num1_int // num2_int}")
    print(f"Ponteciação: {num1_int ** num2_int}")
    print(f"Resto da divisão: {num1_int % num2_int}")
except:
    print("[Erro] Você não digitou um número válido")