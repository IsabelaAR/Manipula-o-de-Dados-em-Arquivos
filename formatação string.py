# Método format()
nome = "Maria"
idade = 30
mensagem = "Olá, {}. Você tem {} anos.".format(nome, idade)
print(mensagem) 

# Método F-string
nome = "Carlos"
idade = 28
mensagem = f"Olá, {nome}. Você tem {idade} anos."
print(mensagem)

# Precisão numérica usando format()
valor = 3.14159
print("Pi com 2 casas decimais: {:.2f}".format(valor))

# Precisão numérica usando F-string
valor = 3.14159
print(f"Pi com 2 casas decimais: {valor:.2f}")

# Formatação de datas usando format()
from datetime import datetime
hoje = datetime.now()
data_formatada = hoje.strftime("Data: %d/%m/%Y")
print(data_formatada)

# Formatação de datas usando F-string
hoje = datetime.now()
data_formatada = f"Data:{hoje: %d/%m/%Y}"
print(data_formatada)
