# len() te diz quantos elementos tem dentro de algo



nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if nome and idade:

    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")

    if " " in nome:
        print(f"Seu nome contém espaços")
    else:
        print(f"Seu não contém espaços")
    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
else:
    print("Você não digitou nada em um dos campos")