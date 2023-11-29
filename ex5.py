import pandas as pd
import os

# Listar todos os arquivos na pasta planilhas
files = [os.path.join('/Bases/', file) for file in os.listdir(planilhas_folder) if file.endswith('.xls')]

# Ler dados de todos os arquivos Excel
dfs = []
for file in files:
    df = pd.read_excel(file)
    dfs.append(df)

# Concatenar os DataFrames em um único DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# Salvar arquivo txt
merged_df.to_csv('resultado_planilhas.txt', index=False)
