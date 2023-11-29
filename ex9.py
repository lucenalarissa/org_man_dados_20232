import pandas as pd
from pathlib import Path
import os


# Leitura da base de pedidos 
pedidos_df = pd.read_excel("Bases/Pedidos.xls")

# Conversao utilizando formato de datetime
pedidos_df['data_hora_atualizacao'] = pd.to_datetime(pedidos_df['DataPedido'], format='%d/m/%Y')

print(pedidos_df.data_hora_atualizacao.values)

pedidos_df.to_csv("output_files/Pedidos.csv")