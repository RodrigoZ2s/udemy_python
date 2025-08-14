lista_de_gatos = [
    {"nome": "Mimikyu", "peso": "" },
    {"nome": "fumaça", "peso": "" },
    {"nome": "Macumba", "peso": "",},
    {"nome": "puera", "peso": "",},
]

def registrar_gatos(): # Finalizado
    while True:
        nome_digitado = input("Digite o nome do gato: ")
        nome_verificado = False

        for nome in lista_de_gatos:
            if nome_digitado.lower() == nome["nome"].lower():
                nome_verificado = True
                peso_atual = input("Digite o peso atual do gato (Em gramas): ")
                if peso_atual.isdigit() == False:
                    print("Número inválido")
                else:
                    nome["peso"] = peso_atual
                    print("Gato registrado com sucesso!")
                    print(nome["peso"])
        if nome_verificado == False: # Verifica se o nome existe
            print("Nome não encontrado!")

        registrar_outro = input("deseja continuar? digite [S]im ou [N]ao]")
        if registrar_outro.lower() in ["sim", "s"]:
            continue
        break

def monitor_peso(): # Em manutenção

    excelente = 30
    muito_bom = 20
    bom = 15
    baixo = 10
    
    gato_digitado = input("Nome do gato: ")
    for gatos in lista_de_gatos:
        if gato_digitado in gatos["nome"]:
            peso_atual = input("Peso atual do gato: ")

            if peso_atual.isdigit() == False:
                return "Você não digitou um número válido"  
            ganho = int(peso_atual) - gatos["peso"]

            if ganho < bom:
                return "❌ Ruim!: Ganho de peso igual ou abaixo de 14g."
            elif ganho >= 15 and ganho < muito_bom:
                return "✅ Bom!: Ganho de peso entre 15g e 19g."
            elif ganho >= muito_bom and ganho < excelente:
                return "✅ Muito bom!: Ganho de peso entre 20g e 29g."
            elif ganho >= excelente:
                return (
                f"✅ Excelente!: Ganho de peso de 30g ou mais. \n" 
                f"Atenção!: Ganho de peso excessivo! procure um veterinário se notar mudanças no comportamento de {gato_digitado}"
            )

    return "Gato não encontrado"

        


            

monitor_peso()