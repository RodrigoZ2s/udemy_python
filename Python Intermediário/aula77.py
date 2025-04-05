# Exercício - sistema de perguntas e respostas


perguntas_dicionario = [
    {
        'Perguntas': ["2+2", "5*5", "10/2"],
        'Opções': {
            "2+2": ['1', '3', '4', '5'],
            "5*5": ['25', '55', '10', '51'],
            "10/2": ['4', '5', '2', '1'],
        },
        "Resposta_usuario": ["Resposta 1", "Resposta 2", "Resposta 3"],
        'Respostas': ['4', '25', '5'],    
    },
]

def main_quest():
    respostas_certas = 3

    for pergunta in perguntas_dicionario[0]['Perguntas']:
        print(f"Pergunta: Quanto é {pergunta}?")

        for i, opcoes in enumerate(perguntas_dicionario[0]["Opções"][pergunta]):
            print(f"{i}) {opcoes}")

        resposta_user = input("R: ")

        if not resposta_user.isdigit() and resposta_user != perguntas_dicionario[0]["Respostas"]:
            print("❌ Resposta incorreta")
            respostas_certas -= 1
        else:
            print("✅ Resposta certa")

    print(f"Parabéns, você acertou {respostas_certas} de 3 perguntas")

main_quest()






