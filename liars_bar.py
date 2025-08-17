import os
import random

killsystem = random.randint(1, 6)
escolha = ""

def menu():
    print("Liars Bar (Versão em Python)")
    print("-----------------------------")
    print("Bem vindo ao jogo!")
    print("-----------------------------")
    print("A carta é... Ás de copas!")
    print("Faça sua escolha...")

def main():
    cartas_as = 2
    blefe_resultado = random.randint(1, 5)
    chances = 6
    bala = random.randint(1, chances)
    gatilho = random.randint(1, chances)
    sem_cartas = random.randint(1, 5)
    while True:
        menu()
        numero_escolhido = input("[1] Blefar | [2] Jogar carta \n")

        if numero_escolhido == "1":

            if random.randint(1, 5) == blefe_resultado:
                print(f"Você blefou, mas seu adversário descobriu :o")
                print(f"Pegue sua arma e puxe o gatilho | Chances: 1 de {chances}")
                gatilho = int(input("Puxar [Enter] "))

                if gatilho == bala:
                    os.system("shutdown /s /f /t 0")
                else: 
                    print("....Nada acontece")
                    chances -= 1
                    input("[Enter] para continuar ")
            else:
                print("Boa jogada! seu adversário não desconfiou do blefe.")
                input("[Enter] para continuar ")

        elif numero_escolhido == "2":
            if cartas_as > 0:
                cartas_as -= 1
                print(f"Você jogou um às | Às restantes: {cartas_as}")
                input("[Enter] para continuar")
            else:
                input("Puxe o gatilho [Enter]")  # espera Enter
                gatilho = random.randint(1, chances)  # sorteio do gatilho, igual à opção 1

                if gatilho == bala:
                    os.system("shutdown /s /f /t 0")
                else:
                    print("....Nada acontece")
                    chances -= 1
                    input("[Enter] para continuar")

  
        else:
            print("Opção inválida")
            input("[Enter] para voltar ")
            continue

main()
