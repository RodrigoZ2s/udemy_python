"""
Closure e funções que retornam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

falar_bom_dia = criar_saudacao("Olá")
print(falar_bom_dia("Maconheiro"))

for nome in ["Maconha", "Dry", "Ice", "Cuzinho"]:
    print(falar_bom_dia(nome))
