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
            


            
        
            

            
            


quest(perguntas)