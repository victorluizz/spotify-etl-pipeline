from src.extract import carregar_dados_brutos
from src.transform import transformar_dados_spotify
from src.load import carregar_dados_sqlite

def executar_pipeline():

    print(" --- INICIANDO PIPELINE SPOTIFY DATA DNA --- \n")

    # Caminhos dos arquivos
    CAMINHO_DADO_BRUTO = "data/raw/dataset.csv"
    CAMINHO_BANCO_DADOS = "data/spotify_data.db" 
    TABELA_FINAL = "musicas_tratadas"

    #1. Etapa de extração
    df_spotify_bruto = carregar_dados_brutos(CAMINHO_DADO_BRUTO)

    print("\n Primeiras 5 linhas extraídas:")
    print(df_spotify_bruto.head(5))

    #2. Etapa de transformação
    df_spotify_limpo = transformar_dados_spotify(df_spotify_bruto)

    # 3. ETAPA DE CARGA
    carregar_dados_sqlite(df_spotify_limpo, CAMINHO_BANCO_DADOS, TABELA_FINAL)

    print("\n --- ✅ PIPELINE EXECUTADO COM SUCESSO ---")

if __name__ == "__main__":
    executar_pipeline()