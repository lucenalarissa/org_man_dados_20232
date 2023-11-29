import pandas as pd

# Input tabela excel
df_capes = pd.read_excel('Bases/capes.xls')

# Input tabela csv
df_ies = pd.read_csv('Bases/ies.csv', delimiter=';', encoding='latin-1')

df_ies = df_ies.rename(columns={'idIES': 'id_instituicao'})

# Realizar a operação de Stream lookup
merged_df = pd.merge(df_capes, df_ies[['sigla_IES', 'id_instituicao']], how='left', left_on='ies', right_on='sigla_IES')

# Remover campos não desejados
result_df = merged_df.drop(['area', 'codigo_programa', 'ies', 'nome_programa', 'inicio_mestrado', 'inicio_doutorado', 'conceito_recomendado'], axis=1)

# Salvar arquivo txt
result_df.to_csv('resultado.txt', index=False)
