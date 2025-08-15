# Exercício 1 – Saudação personalizada

# Crie uma função criar_saudacao(saudacao) que retorna outra função que recebe um nome e retorna a saudação completa.

# Exemplo esperado:

# bom_dia = criar_saudacao("Bom dia")
# boa_tarde = criar_saudacao("Boa tarde")

# print(bom_dia("Alice"))   # Bom dia, Alice!
# print(boa_tarde("Bob"))   # Boa tarde, Bob!

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

bom_dia = criar_saudacao("Bom dia")
boa_tarde = criar_saudacao("Boa tarde")

print(bom_dia("Jorge"))
print(boa_tarde("Maria"))

# Exercício 2 – Potência personalizada

# Crie uma função criar_potencia(expoente) que retorna uma função que eleva qualquer número ao expoente definido.

# Exemplo esperado:

# quadrado = criar_potencia(2)
# cubo = criar_potencia(3)

# print(quadrado(5))  # 25
# print(cubo(2))      # 8

def criar_potencia(expoente):
    def elevar(numero):
        return numero ** expoente
    return elevar

quadrado = criar_potencia(2)
cubo = criar_potencia(3)

print(quadrado(5))
print(cubo(2))

# Exercício 3 – Filtro de números

# Crie uma função criar_filtro(multiplo_de) que retorna uma função que recebe uma lista de números e retorna apenas os múltiplos de multiplo_de.

# Exemplo esperado:

# filtro3 = criar_filtro(3)
# filtro5 = criar_filtro(5)

# print(filtro3([1,2,3,4,5,6,7,8,9]))  # [3, 6, 9]
# print(filtro5([10,12,15,20]))        # [10, 15, 20]

def criar_filtro(multiplo_de):
    def numberlist(lista):
        lista_numeros = []
        for numero in lista:
            if numero % multiplo_de == 0:
                    lista_numeros.append(numero)
        return lista_numeros
    return numberlist

filtro3 = criar_filtro(3)
filtro5 = criar_filtro(5)

print(filtro3([1,2,3,4,5,6,7,8,9]))

# Exercício 4 – Aplicar operação customizada

# Crie uma função criar_operacao(operacao) que recebe uma função operacao (por exemplo lambda x: x+2 ou lambda x: x*3) e retorna outra função que aplica essa operação a qualquer número que você passar.

# Exemplo esperado:

# adicionar2 = criar_operacao(lambda x: x+2)
# multiplicar3 = criar_operacao(lambda x: x*3)

# print(adicionar2(5))     # 7
# print(multiplicar3(4))   # 12

def criar_operacao(operacao):
     def aplicar(numero):
          return operacao(numero)
     return aplicar

adicionar2 = criar_operacao(lambda x: x+2)
multiplicar3 = criar_operacao(lambda x: x*3)

print(adicionar2(5))
print(multiplicar3(4))
            
                            

                


