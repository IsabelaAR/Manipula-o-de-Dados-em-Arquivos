import os

# Removendo arquivo
arquivo_a_remover = "arquivo_a_remover.txt"
try:
    os.remove(arquivo_a_remover)
    print(f"O arquivo {arquivo_a_remover} foi removido com sucesso.")
except FileNotFoundError:
    print(f"O arquivo {arquivo_a_remover} não foi encontrado.")
except Exception as e:
        print(f"Ocorreu um erro ao remover o arquivo: {e}")

# Renomeando arquivo
nome_antigo = "arquivo_antigo.txt"
nome_novo = "arquivo_novo.txt"
try:
    os.rename(nome_antigo, nome_novo)
    print(f"O arquivo {nome_antigo} foi renomeando para {nome_novo}.")
except FileNotFoundError:
    print(f"O arquivo {nome_antigo} não foi encontrado.")
except Exception as e:
        print(f"Ocorreu um erro ao renomear o arquivo: {e}")