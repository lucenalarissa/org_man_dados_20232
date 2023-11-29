import csv

input_path = 'Bases/movies.txt'
output_path = 'output_files/filmes.csv'

# Vamos armazenar todos os cabeçalhos possíveis que encontrarmos enquanto processamos o arquivo
headers = set()

filmes = []
filme_atual = {}

with open(input_path, 'r', encoding='latin-1', errors='replace') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if line:
        if ':' in line:
            key, value = line.split(':', 1)
            # Removendo espaços e traduzindo os termos
            key = key.strip().replace('Year', 'Ano').replace('Genre', 'Gênero')\
                .replace('Directed by', 'Direção').replace('Script', 'Roteiro')\
                .replace('Music', 'Música').replace('Cast', 'Elenco')\
                .replace('Produced by', 'Produzido por')
            value = value.strip()

            # Adicionando a chave traduzida ao conjunto de cabeçalhos, se ainda não estiver lá
            headers.add(key)
            
            filme_atual[key] = value
        else:
            if filme_atual:
                filmes.append(filme_atual)
            filme_atual = {'Título': line}
    else:
        # Linha vazia – fim do bloco de informações do filme atual
        if filme_atual:
            filmes.append(filme_atual)
            filme_atual = {}

# Adiciona o último filme se o arquivo não terminar com uma linha em branco
if filme_atual:
    filmes.append(filme_atual)

# Convertendo o set de cabeçalhos em uma lista ordenada
headers = ['Título'] + sorted(list(headers - {'Título'}))

# Gravação no arquivo CSV
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
    csv_writer.writeheader()
    for filme in filmes:
        # Preenche os valores faltantes com 'n/a'
        row = {header:(filme.get(header) or 'n/a') for header in headers}
        csv_writer.writerow(row)

print(f'Arquivo CSV "{output_path}" criado com sucesso!')