import pandas as pd

# Gerar 10 mensagens
messages = ['Hello World!' for _ in range(10)]

# Criar um DataFrame do Pandas
df = pd.DataFrame({'mensagem': messages})

# Salvar arquivo csv
df.to_csv('ex1/output.csv', index=False)
