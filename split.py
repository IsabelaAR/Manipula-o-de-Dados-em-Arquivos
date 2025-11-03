# Quebrando strings usando a função split
frase1 = "Eu amo comer amoras no café da manhã"
lista_termos1 = frase1.split()
print(lista_termos1)

frase2 = "Amora abacaxi    abacate         banana"
lista_termos2 = frase2.split()
print(lista_termos2)

frase3 = "Carro,moto,avião"
lista_termos3 = frase3.split(',')
print(lista_termos3)

# Contagem de uma palavra na string usando o método count diretamente
print("Contagem direta:", frase1.count('amo'))

# Contagem de uma palavra na string usando o método split
contador = 0
lista_termos1 = frase1.split()
for termo in lista_termos1:
    if termo == 'amo':
        contador += 1
print("Contagem correta:", contador)