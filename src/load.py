import pandas as pd
import sqlite3

def carregar_dados_sqlite(df: pd.DataFrame, caminho_banco: str, nome_tabela: str) -> None:
    """
    Recebe o DataFrame tratado e o salva em uma tabela dentro do banco SQLite.
    Caso a tabela já exista, ela será substituída.
    """
    print(f"💾 [CARGA] Iniciando o carregamento dos dados no banco: {caminho_banco}...")
    
    try:

        conexao = sqlite3.connect(caminho_banco)
        

        df.to_sql(name=nome_tabela, con=conexao, if_exists='replace', index=False)
        
        conexao.close()
        
        print(f"✅ [CARGA] Sucesso! {df.shape[0]} linhas inseridas na tabela '{nome_tabela}'.")
        
    except Exception as e:
        print(f"🚨 [CARGA] Erro ao carregar os dados no SQLite: {e}")
        raise e