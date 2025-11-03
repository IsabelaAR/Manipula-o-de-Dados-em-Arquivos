import os

# Criando um diretório
try: 
    os.mkdir("meu_diretorio")
    print("Diretório criado!")
except PermissionError as erro:
    print("Sem permissão para criar diretório")
    print("Descrição:", erro)
except FileExistsError as erro:
    print("Diretório já existe")
    print("Descrição:", erro)

try: 
    os.rmdir("meu_diretorio")
    print("Diretório removido!")
except PermissionError as erro:
    print("Sem permissão para remover diretório")
    print("Descrição:", erro)
except FileNotFoundError as erro:
    print("Diretório inexistente")
    print("Descrição:", erro)
except OSError as erro:
    print("Outro erro.")
    print("O diretório está vazio?")
    print("Descrição:", erro)