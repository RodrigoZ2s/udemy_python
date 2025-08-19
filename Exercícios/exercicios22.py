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
import os

def quiz_withTips(dicionario):
    acertos = 0

    for perguntas in dicionario:
        tentativas = 2
        acertou = False

        print(f"\nPergunta: {perguntas['Pergunta']}")   
        while tentativas > 0 and acertou == False:

            for indice, opcao in enumerate(perguntas["Opções"]):
                print(f"{indice}) {opcao}")

            escolha_inicial = input("Escolha uma opção: ")

            if escolha_inicial.isdigit() == False: # Verifica se é um número
                os.system("cls")
                print("Você não digitou um número válido!\n")
                continue

            escolha_indice = int(escolha_inicial)

            if perguntas["Opções"][escolha_indice] == perguntas["Resposta"]:
                acertos += 1
                print("\nVocê acertou!")
                acertou = True
                break

            tentativas -= 1   
            if tentativas == 0:
                print("\n>> Acabou suas tentativas! Você errou a questão")
                break

            else:
                os.system("cls")
                escolha_errada = input("Você errou! Pressione [1] para uma dica ou [Enter] para tentar novamente.\nEscolha: ")
                print(f"restam {tentativas} tentativas")

                if escolha_errada == "1":
                    input(f"\n>> {perguntas['Dica']} [Enter para continuar]")
                    continue
                else: 
                    continue
    print(f"Você conseguiu um total de {acertos} de {len(dicionario)} acertos!")

quiz_withTips(perguntas3)
    