# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def quest(dicionario):
    acertos = 0
    erros = 0
    for questoes in dicionario:
        print(questoes["Pergunta"])


        for i, opcoes in enumerate(questoes["Opções"]):
            print(f"{i}) {opcoes}")
        resposta = int(input("R:"))
        if resposta == questoes["Opções"].index(questoes["Resposta"]):
            print("Acertou! 😁")
            acertos += 1
        else: 
            print("Errou! 🙄")
            erros += 1

    print(f"Você conseguiu um total de {acertos} acertos e {erros} erros! 😀")
            
# quest(perguntas)

# Exercício – Quiz de verdadeiro ou falso

# Monte um sistema parecido, mas em vez de múltipla escolha, cada pergunta deve ter apenas “V” ou “F” como resposta.

# Use o mesmo esquema de contar acertos e erros.

# No final, mostre o placar.

# Exemplo da estrutura de perguntas:

perguntas2 = [
    {"Pergunta": "O Sol é uma estrela?", "Resposta": "V"},
    {"Pergunta": "Python foi criado em 2020?", "Resposta": "F"},
    {"Pergunta": "A água ferve a 100°C?", "Resposta": "V"},
]

def TrueOrFalse(dicionario):
    acertos = 0
    for pergunta in dicionario:
        print("------------------------------------")
        print(f"Pergunta: {pergunta["Pergunta"]}")
        print("------------------------------------")
        escolha = input("[V]erdadeiro ou [F]also? \nResposta:").lower()

        if escolha not in "vf":
            print("\n>> Resposta inválida!\n")
        
        if escolha == pergunta["Resposta"].lower():
            print(">> Você acertou!")
            acertos += 1
        else:
            print(">> Errou!")

    print(f"Você acertou um total de {acertos} de {len(dicionario)}")

# TrueOrFalse(perguntas2)

# Exercício – Quiz com dicas

# Faça um quiz de múltipla escolha, mas cada pergunta terá também uma “dica” armazenada no dicionário.

# O usuário pode digitar dica antes de responder.

# Se usar a dica, perde meio ponto na nota final.

# Exemplo de dicionário:

perguntas3 = [
    {
        "Pergunta": "Qual é a capital da França?",
        "Opções": ["Londres", "Paris", "Roma", "Madrid"],
        "Resposta": "Paris",
        "Dica": "É conhecida como a cidade da luz."
    },
    {
        "Pergunta": "Quem desenvolveu a Teoria da Relatividade?",
        "Opções": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Nikola Tesla"],
        "Resposta": "Albert Einstein",
        "Dica": "Seu sobrenome virou sinônimo de 'gênio'."
    },
    {
        "Pergunta": "Qual planeta é conhecido como o 'Planeta Vermelho'?",
        "Opções": ["Marte", "Vênus", "Júpiter", "Saturno"],
        "Resposta": "Marte",
        "Dica": "É o quarto planeta a partir do Sol."
    },
]

def average_quest(dicionario):

    print("----------------------")
    print("Questionário com dicas")
    print("----------------------")
    acertou = False
    acertos = 0
    while acertou == False and tentativas > 0:
        acertou = False
        tentativas = 2
        for perguntas in dicionario:
            print(f"Pergunta: {perguntas['Pergunta']}")
            opcoes = perguntas["Opções"]
            for i, opcao in enumerate(opcoes):
                  print(f"{i}) {opcao}")

            escolha = int(input("Escolha uma opção: "))

            if opcoes[escolha] == perguntas["Resposta"]:
                acertos += 1
                print("\n>> Acertou!\n" )
                acertou =- True
                continue
            elif opcoes[escolha] != perguntas["Resposta"]:
                    tentativas -= 1
                    print(f"\n>> Errou! tente novamente...\n | tentivas restantes: {tentativas}\n ")

                    if tentativas > 0:
                        erro_usuario = input("> Pressione [ENTER] continuar ou [1] para pedir uma dica\n").lower()
                    elif tentativas == 0:
                        print("Tentativas esgotadas, você falhou no questionário, tente novamente")
                        input("[Enter]")
                        break
                    elif erro_usuario == "":
                        continue
                    elif erro_usuario == "1":
                        print(f">> Dica: {perguntas["Dica"]}")
                        input("Pressione qualquer tecla para continuar\n")
                        

        print(f"Você acertou")
average_quest(perguntas3)