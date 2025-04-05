entrada = input("[E]trar [S]air: ")
senha_digitada = input("Senha: ")
senha_permitida = "123456"
print(entrada)
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Você entrou no sistema")
else:
    print("Você saiu do sistema")