import pandas as pd

# Input do arquivo de texto
df = pd.read_csv('ex2/fulano.txt', header=None, names=['nome'], dtype=str)

# Adcionar constantes
df['mensagem'] = 'Hello World'
df['exclamacao'] = '!'
df['espaco'] = ' '

# Juntar campos
df['valuename'] = df['mensagem'] + df['espaco'] + df['nome'] + df['exclamacao']

# Salvar arquivo txt
df['valuename'].to_csv('ex2/output.txt', index=False, header=False)
