# Obter_dados_CEP_MG
 obtenção de dados de endereço, latitude e longitude

# README.md

# CEP Data Processing

Este repositório contém um script em Python para processar dados de CEPs a partir de um arquivo CSV, fazendo consultas a uma API de CEPs e salvando os resultados em outro arquivo CSV.

## Descrição

O script carrega um arquivo CSV contendo CEPs, verifica se cada CEP já foi processado, faz uma requisição a uma API de CEPs para obter informações detalhadas e salva esses dados em um arquivo de saída. O processo é repetido até que todos os CEPs no arquivo original sejam processados.

## Pré-requisitos

- Python 3.x
- Bibliotecas: `pandas`, `requests`

Você pode instalar as bibliotecas necessárias com o comando:

```bash
pip install pandas requests
```

## Configuração

1. Altere os caminhos dos arquivos no script para corresponder aos seus diretórios locais:
   ```python
   df_path = r'C:\Users\Eric\Downloads\CEP.csv'
   result_file_path = r'C:\Users\Eric\Downloads\LOGRADOUROS_MG.csv'
   ```

2. Certifique-se de que o arquivo `CEP.csv` esteja no formato esperado, com uma coluna chamada `CEP` e uma coluna chamada `PROCESSADO`.

## Execução

Execute o script com o comando:

```bash
python script.py
```

O script irá:
1. Carregar o arquivo CSV contendo os CEPs.
2. Iterar sobre cada linha do CSV.
3. Verificar se o CEP já foi processado.
4. Fazer uma requisição à API para obter informações detalhadas do CEP.
5. Salvar os resultados em um arquivo CSV de saída.
6. Marcar o CEP como processado no arquivo original.
7. Repetir o processo até que todos os CEPs sejam processados.

## Detalhes do Script

- O script utiliza a biblioteca `pandas` para manipulação dos dados em CSV.
- Utiliza a biblioteca `requests` para fazer requisições HTTP à API de CEP.
- Inclui uma pausa de 1 segundo entre as requisições para evitar excesso de requisições.
- Salva progressivamente os resultados para evitar perda de dados em caso de interrupções.
- Marca CEPs processados como `concluido` ou `falha` no arquivo original.

## Considerações Finais

- Certifique-se de que o arquivo CSV original esteja no formato correto.
- Ajuste o caminho dos arquivos conforme necessário.
- Monitore o número de requisições para evitar ser bloqueado pela API.