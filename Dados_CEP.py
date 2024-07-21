import pandas as pd
import requests
import time
import os

# Carregar o arquivo csv
df_path = r'C:\Users\Eric\Downloads\CEP.csv'
df = pd.read_csv(df_path, delimiter=';')

# Criar um dataframe vazio para armazenar os resultados
result_df = pd.DataFrame()

# Contador de consultas
counter = 0

# Caminho para o arquivo de resultados
result_file_path = r'C:\Users\Eric\Downloads\LOGRADOUROS_MG.csv'

# Função para verificar se o arquivo já existe
def file_exists(filepath):
    return os.path.isfile(filepath)

# Iterar sobre cada linha no dataframe
for index, row in df.iterrows():
    # Verificar se a coluna 'PROCESSADO' tem o valor 'concluido'
    if row['PROCESSADO'] == 'concluido':
        continue  # Pular para a próxima linha
    
    # Pegar o valor do CEP
    cep = int(row['CEP'])
       
    
    # Fazer a requisição para a API
    response = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    
    # Verificar se a requisição foi bem sucedida
    if response.status_code == 200:

        time.sleep(1)  # Pausar para evitar excesso de requisições

        # Converter a resposta JSON em um dataframe
        data = pd.json_normalize(response.json())
        
        print(f"Recebendo {data}")
        
        # Adicionar o dataframe de dados ao dataframe de resultados
        result_df = pd.concat([result_df, data], ignore_index=True)
        counter += 1
        
        # Marcar a linha como 'concluido'
        df.at[index, 'PROCESSADO'] = 'concluido'
        
        # Salvar o dataframe atualizado para evitar perda de progresso
        df.to_csv(df_path, sep=';', index=False)
        
        # Verificar se atingiu 100 consultas
        if counter == 100:
            # Salvar os resultados intermediários no arquivo csv
            result_df.to_csv(result_file_path, mode='a', sep=';', index=False, header=not file_exists(result_file_path))
            
            # Resetar o dataframe de resultados e o contador
            result_df = pd.DataFrame()
            counter = 0
    else:
        # Marcar a linha como 'falha' caso a requisição falhe
        df.at[index, 'PROCESSADO'] = 'falha'
        # Salvar o dataframe atualizado para evitar perda de progresso
        df.to_csv(df_path, sep=';', index=False)

# Salvar quaisquer resultados restantes
if not result_df.empty:
    result_df.to_csv(result_file_path, mode='a', sep=';', index=False, header=not file_exists(result_file_path))

print("Concluído!")
