"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

contador = 0

while contador <= 100:
    contador += 1
    if contador == 6:
        print("Não tem o 6")
        continue # Volta para o while

    if contador >= 10 and contador <= 27:
        print("Não tem o ", contador)
        continue # Volta para o while


    print(contador)
    if contador == 40:
        break
    
    
print("Acabou")