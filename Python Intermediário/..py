import os

lista_de_gatos = [
    {"nome": "Mimikyu", "peso": "" },
    {"nome": "fumaça", "peso": "" },
    {"nome": "Macumba", "peso": "",},
    {"nome": "puera", "peso": "",},
]

def registrar_gatos(): # Em desenvolvimento
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

        if nome_verificado == False: # Verifica se o nome existe
            print("Nome não encontrado!")

        registrar_outro = input("Gato registrado com sucesso! deseja continuar? digite [S]im ou [N]ao]")
        if registrar_outro.lower() in ["sim", "s"]:
            continue
        break


def monitor_peso(): # Em manutenção
    
    gato = input("Nome do gato: ")

    if gato[peso_atual] == 0:
        return "Por favor, registre o peso do seu gato"
    
    peso_atual = input("Peso atual: ")
    lista_de_gatos.append(gato[peso_atual])

    if peso_atual < peso_atual + 10:
        return "❌ Ruim!: Ganho de peso abaixo de 10g."
    elif peso_atual >= (peso_atual + 10) and peso_atual <= (peso_atual + 15):
        return "✅ Bom!: Ganho de peso entre 10g e 15g."
    elif peso_atual >= (peso_atual + 16) and peso_atual <= (peso_atual + 20):
        return "✅ Muito bom!: Ganho de peso entre 19g e 21g."
    elif peso_atual >= (peso_atual + 22) and peso_atual <= (peso_atual + 25):
        return "✅ Excelente!: Ganho de peso de 22g ou mais."
    else:
        return f"Atenção!: Ganho de peso excessivo! procure um veterinário se notar mudanças no comportamento de {gato}"
def info_gatos(): # Em desenvolvimento
    pass
   

def menu_gatos(): # Finalizado
    while True:
        print("========================")
        print("   Pesagem dos gatos    ")
        print("========================")
        print("Escolha as opções abaixo")
        print("1 - Registrar peso atual")
        print("2 - Monitor de Peso")
        print("3 - Informações mais recentes")
        print("0 - Sair")
        escolha_usuario = input("R: ")

        if escolha_usuario == "1":
            os.system("cls")
            registrar_gatos()
        elif escolha_usuario == "2":
            os.system("cls")
            monitor_peso()
        elif escolha_usuario == "3":
            os.system("cls")
            info_gatos()
        elif escolha_usuario == "0":
            continue
        else:
            os.system("cls")
            print("Você não escolheu uma opção válida!")
            continue



