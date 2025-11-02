import os

arquivo1 = open("dados1.txt", 'w', encoding='utf-8') #"enconding" e pra n bugar as palavras acentos
print(os.path.abspath(arquivo1.name))

arquivo1.write("Olá, mundo!!!")

print(os.path.relpath(arquivo1.name))
print(arquivo1)

arquivo1.close()