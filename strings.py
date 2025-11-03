arquivo = open('dados.txt', 'r', encoding='utf-8')

# Lendo o arquivo com função read()
"""
conteudo = arquivo.read()
print("Tipo de conteúdo: ", type(conteudo))

print('Conteúdo retornado pelo read:')
print(repr(conteudo))

# Lendo o arquivo com a função readline()
conteudo = arquivo.readline()
print("Tipo de conteúdo: ", type(conteudo))

print('Conteúdo retornado pelo readline:')
print(repr(conteudo))

prox_conteudo = arquivo.readline()
print('Conteúdo retornado pelo próximo readline:')
print(repr(prox_conteudo))"""

# Lendo o arquivo com função readlines()
conteudo = arquivo.readlines()
print("Tipo de conteúdo: ", type(conteudo))

print('Conteúdo retornado pelo readlines:')
print(repr(conteudo))


# Contando as linhas do arquivo
with open ('dados.txt', encoding='utf-8') as arquivo:
    contador = 0
    print('Representação do arquivo')
    for linha in arquivo: # Conta todas as linhas do arquivo
        print(repr(linha))
        if linha:
            contador += 1
    print("Total de linhas =", contador) 


# Contando as linhas do arquivo após o uso do strip
with open ('dados.txt', encoding='utf-8') as arquivo:
    contador = 0
    print('Representação do arquivo após strip')
    for linha in arquivo: 
        linha_limpa = linha.strip() # Limpa as linhas vazias
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
    print("Total de linhas =", contador) 

# Contador de palavras iguais do arquivo

with open('dados.txt', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    contador = texto.count("Olá")
    print("Total de Olás =", contador)

arquivo.close()
