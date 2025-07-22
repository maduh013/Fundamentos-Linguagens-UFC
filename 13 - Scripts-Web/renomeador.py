Exemplo de Script: Renomear arquivos em uma pasta (Python)

import os

pasta = "./arquivos"

# Cria a pasta de teste se não existir
if not os.path.exists(pasta):
    os.makedirs(pasta)
    with open(os.path.join(pasta, "exemplo1.txt"), "w") as f:
        f.write("Teste 1")
    with open(os.path.join(pasta, "exemplo2.txt"), "w") as f:
        f.write("Teste 2")

# Renomeia os arquivos
for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith(".txt"):
        novo_nome = f"arquivo_{nome_arquivo}"
        os.rename(
            os.path.join(pasta, nome_arquivo),
            os.path.join(pasta, novo_nome)
        )

print("Arquivos renomeados com sucesso.")
