# Conversão de tipos, coerção

print(int("1"), type (int("1"))) # str > int
print(int("1") + 1) # str > int
print(type(int("1") + 1)) # str > int
print(bool("")) # str > boolean
print(str(1) + "b") # int > str