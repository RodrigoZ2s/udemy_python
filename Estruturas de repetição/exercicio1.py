num_secreto = 3
resposta = 0
tentativas = 3

while tentativas > 0:
    resposta = int(input(f"Acerte o número secreto, você tem apenas {tentativas} tentativas. \n 1:"))

    if resposta != num_secreto:
        print("Você errou! tente novamente")
        tentativas -= 1
    else:
        print(f"Você acertou o número na {4 - tentativas} tentativa, parabéns!")
        break
if tentativas == 0:
    print("Suas tentativas acabaram, tente novamente mais tarde ;(")



