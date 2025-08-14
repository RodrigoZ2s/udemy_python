def criar_calculadora(operacao):
    def calculo(x, y):
        if operacao == "subtrai":
            return x - y
        elif operacao == "divide":
            return x / y
        elif operacao == "multiplica":
            return x * y
        elif operacao == "soma":
            return x + y
    return calculo
subtrai = criar_calculadora("subtrai")
print(f"o resultado da subtração é {subtrai(5, 4)}")