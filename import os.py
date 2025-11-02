import os

arquivo1 = open("dados1.txt", 'w', encoding='utf-8') #"enconding" e pra n bugar as palavras acentos
print(os.path.abspath(arquivo1.name))

print("Nome do arquivo:", arquivo1.name)
print("Modo de abertura:",arquivo1.mode)
print("Arquivo está fechado?", arquivo1.closed)

arquivo1.write("Olá, mundo!!!")

arquivo1.close()

print("Arquivo está fechado agora? ", arquivo1.closed)

relpath = os.path.relpath('dados1.txt')
abspath = os.path.abspath('dados1.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)