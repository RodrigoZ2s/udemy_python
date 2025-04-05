""" Calculadora com While """
while True:
    n1 = input("Digite o primeiro número: ")
    n2 = input("Digite o segundo número: ")
    operador = input("Escolha um operador lógico: (+-/*): ")


    numeros_validos = None # Flag
    float_n1 = 0
    float_n2 = 0

    try:
        float_n1 = float(n1)
        float_n2 = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador inválido")
        continue
    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
    
    if operador == "+":
        print(f"Resultado: {float_n1 + float_n2}")
    elif operador == "-":
        print(f"Resultado: {float_n1 - float_n2}")
    elif operador == "/":
        print(f"Resultado: {float_n1 / float_n2}")
    else:
        print(f"Resultado: {float_n1 * float_n2}")
    
    sair = input("Deseja sair? [s]im: ").lower().startswith('s')
    if sair is True:
        break


    