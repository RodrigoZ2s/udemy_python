import re
import sys

# cpf_usuario = "064.511.077-94" \
#     .replace(".", "") \
#     .replace("-", "") \
#     .replace(" ", "") 

entrada = input("CPF: ")
cpf_usuario = re.sub(
    r"[^0-9]",
    "",
    entrada
)

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print("Você enviou dados sequenciais.")
    sys.exit()


nove_digitos = cpf_usuario[:9]
contador_1 = 10
digito_1 = 0

resultado_soma_1 = 0
for digito in nove_digitos:
    resultado_soma_1 += int(digito) * contador_1
    contador_1 -= 1

digito_1 = (resultado_soma_1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_2 = 11

resultado_soma_2 = 0
for digito in dez_digitos:
    resultado_soma_2 += int(digito) * contador_2
    contador_2 -= 1

digito_2 = (resultado_soma_2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f"{nove_digitos}{digito_1}{digito_2}"

if cpf_usuario == cpf_gerado:
    print(f"{cpf_usuario} é válido") 
else:
    print("CPF inválido")
