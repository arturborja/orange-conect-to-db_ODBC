import pyodbc
import pandas as pd
from Orange.data.pandas_compat import table_from_frame

# Credenciais do banco de dados
dsn = "nomeddriver dsn ODBC"
username = "username"
password = "senha"

# Nome da tabela a ser consultada (modifique esta variável conforme necessário)
selected_table = "nomedatabela"  # Altere para a tabela desejada

try:
    print("Iniciando conexão ODBC...")
    # Conectar ao banco de dados MySQL via ODBC
    connection = pyodbc.connect(
        f"DSN={dsn};UID={username};PWD={password}"
    )
    print("Conexão estabelecida!")

    # Listar todas as tabelas do banco de dados
    cursor = connection.cursor()
    cursor.tables()
    tables = [row.table_name for row in cursor.fetchall() if row.table_type == 'TABLE']
    print("Tabelas disponíveis:", tables)

    if selected_table in tables:
        # Consultar dados da tabela selecionada
        query = f"SELECT * FROM {selected_table}"
        df = pd.read_sql_query(query, con=connection)

        # Converter o DataFrame para uma Tabela do Orange
        out_data = table_from_frame(df)
        print(f"Dados da tabela '{selected_table}' carregados com sucesso!")
        print(df.head(5))
    else:
        print(f"Tabela '{selected_table}' não encontrada no banco de dados.")

except Exception as e:
    print(f"Erro: {e}")


