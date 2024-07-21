import pandas as pd

# Ler os arquivos CSV
arquivo1 = pd.read_csv(r'C:\Users\Eric\Downloads\CEP2.csv', delimiter=";")
arquivo2 = pd.read_csv(r'C:\Users\Eric\Downloads\LOGRADOUROS_MG2.csv', delimiter=";")

# Converter as colunas "cep" para string para garantir a consistência
arquivo1['CEP'] = arquivo1['CEP'].astype(str)
arquivo2['cep'] = arquivo2['cep'].astype(str)

# Criar uma coluna 'PROCESSADO' e inicializar com valores vazios
#arquivo1['PROCESSADO'] = ''

# Verificar se os CEPs de arquivo1 estão em arquivo2
for index, row in arquivo1.iterrows():
    if row['CEP'] not in arquivo2['cep'].values:
        arquivo1.at[index, 'PROCESSADO'] = 'falhou'
        print(f"{row['CEP']} falhou.")

# Salvar o resultado em um novo arquivo CSV
arquivo1.to_csv(r'C:\Users\Eric\Downloads\CEP_falha.csv', sep=';',index=False)
print("Concluido")
