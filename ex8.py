import pandas as pd
from datetime import datetime

# Caminho do seu arquivo Excel existente.
input_file_path = 'Bases/capes.xls'
# Caminho para o novo arquivo Excel com a data/hora incluída.
output_file_path = 'output_files/capes.csv'

# Carregando o arquivo Excel em um DataFrame do pandas.
df = pd.read_excel(input_file_path)

# Adicionando uma coluna com a data e hora atual.
df['DataHoraRegistro'] = datetime.now()

# Gravando o DataFrame alterado de volta em um novo arquivo Excel.
df.to_csv(output_file_path, index=False)