"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
outra_variavel = f"{string[:3]}ABC{string[4:]}" # A posição do ":" indica pra qual lado vai continuar exibindo
print(string)
print(outra_variavel)
print(string.zfill(10)) # Executa uma ação
#print(string.capitalize()) # Executa uma ação
