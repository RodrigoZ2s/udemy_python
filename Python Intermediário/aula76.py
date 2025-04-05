pessoa = {
    "nome": "Maconha",
    "sobrenome": "Da silva",
    "idade": 18,
    "altura": 1.8,
    "endereços": [
        {"rua": "Rua dos baguio", "numero": 1},
        {"rua": "Rua dos cuzudo", "numero": 2},
    ]
}   
# pessoa = dict(nome="Maconha", sobrenome="Da Silva")
# print(pessoa["nome"])

for chave in pessoa:
    print(chave, pessoa[chave])

pessoa = {}
chave = "sobrenome"

pessoa[chave] = "cuzin"
pessoa["nome"] = "Maconheiro"

del pessoa["sobrenome"]
print(pessoa["nome"])
print(pessoa)

if pessoa.get("sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["sobrenome"])


print(len(pessoa)) # Número de chaves
print(list(pessoa.keys())) # Chaves
print(list(pessoa.values())) # Valores
print(list(pessoa.items())) # Chaves e valores

pessoa.setdefault("idade", None) # Define um valor padrão na chave

d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1 , 2]
}
d2 = d1.copy() # Função para copiar um dicionário

d2["c1"] = 1000
d2["l1"][1] = 999999

print(d1)
print(d2)
