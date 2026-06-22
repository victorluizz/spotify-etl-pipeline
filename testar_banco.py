import sqlite3
import pandas as pd

conexao = sqlite3.connect("data/spotify_data.db")

query = """
    SELECT artists, track_name, duration_min, popularity
    FROM musicas_tratadas
    ORDER BY popularity DESC
    LIMIT 5;
"""

df_resultado = pd.read_sql_query(query, conexao)
print("Top 5 músicas mais populares no dataset:")
print(df_resultado)

conexao.close()