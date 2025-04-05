nome = input("Qual seu nome?")
idade = input("Qual sua idade?")
print(f"Seu nome é {nome} e você tem {idade} anos.")

# Metodo que pode gerar problemas futuros
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
print(n1 + n2)
# Método mais prudente
n1 = (input("Digite um número:"))
n2 = (input("Digite outro número:"))

check1 = int(n1)
check2 = int(n2)
print(check1 + check2)