import os, subprocess
# Mostrar o diretorio atual
print(f"Diretório Atual: ",os.getcwd())

# Mostra o processo atual
print(f"Processo Atual: ",os.getpid())

subprocess.run("notepad")

#Criar um arquivo
with open("Arquivo_aula.txt", "w") as arquivo:
    arquivo.write("Sistemas de Informação 4° Período, Sistemas Operacionais")