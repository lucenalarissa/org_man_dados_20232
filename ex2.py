import pandas as pd

# Input do arquivo de texto
df = pd.read_csv('Bases/fulano.txt', header=None, names=['nome'], dtype=str)

# Adcionar constantes
df['mensagem'] = 'Hello World'
df['exclamacao'] = '!'
df['espaco'] = ' '

# Juntar campos
df['valuename'] = df['mensagem'] + df['espaco'] + df['nome'] + df['exclamacao']

# Salvar arquivo txt
df['valuename'].to_csv('output.txt', index=False, header=False)
