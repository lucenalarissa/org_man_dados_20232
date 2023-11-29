import pandas as pd

# Passo 1: Ler o arquivo capes.xls
caminho_do_arquivo = 'Bases/capes.xls'

# Tente abrir o arquivo Excel e carregar o conteúdo no DataFrame
df = pd.read_excel(caminho_do_arquivo)

# Passo 2: Validar os campos do dataset
# Nome do campo que usaremos para validação
campo_para_validar = 'Escore_3'

# Verificar se o campo 'Escore_3' possui algum valor nulo
if campo_para_validar not in df.columns:
    print(f"O campo '{campo_para_validar}' não foi encontrado no dataset.")
else:
    # Contar a quantidade de valores nulos na coluna
    qtde_nulos = df[campo_para_validar].isnull().sum()

    # Se a coluna possui valores nulos, interrompa a execução
    if qtde_nulos > 0:
        print(f"O campo '{campo_para_validar}' contém {qtde_nulos} valores nulos."
        "\nPortanto, nao passou na validação.")
    else:
        print(f"O campo '{campo_para_validar}' passou na validação. Não contém valores nulos.")
