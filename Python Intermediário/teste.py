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
    
    gato = input("Nome do gato: ")
    for gatos in lista_de_gatos:
        if gato != gatos["nome"]:
            return "Gato não encontrado"
    
    peso_atual = input("Peso atual: ")
    for nomes in lista_de_gatos:
        if nomes == gato:
            nomes["peso"] = peso_atual
            return nomes["peso"]

monitor_peso()