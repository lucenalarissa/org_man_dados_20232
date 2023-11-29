import os
import re

# Lista todos os arquivos na pasta "bases"
files_list = os.listdir("Bases/")

# Expressão regular para verificar arquivos que terminam com '.xls'
xls_regex = re.compile(r'.*\.xls$')

# Filtra a lista usando a expressão regular
xls_files = [file for file in files_list if xls_regex.match(file)]

# Exibe os arquivos .xls
print(xls_files)

# Salvando a lista de arquivos .xls em um arquivo
with open('output_files/xls_files_list.txt', 'w') as f:
    for xls_file in xls_files:
        f.write(f"{xls_file}\n")