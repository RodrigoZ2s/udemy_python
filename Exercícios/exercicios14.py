def calcular_media(*args):
    return (sum(args)) / len(args)

def verificar_aprovado(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

media_aluno = calcular_media(1, 5, 6)
print(f"A média do aluno é {media_aluno}")
print(verificar_aprovado(media_aluno))
