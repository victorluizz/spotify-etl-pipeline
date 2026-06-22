import pandas as pd

def transformar_dados_spotify(df: pd.DataFrame) -> pd.DataFrame:

    """
    Recebe um DF bruto e aplica as seguintes transformações encontradas na EDA
    1. Remover duplicadas pelo ID da música
    2. Remover valores nulos.
    2. Filtrar outliers de duração
    4. Criar a coluna oficial de duração em minutos
    """

    print("⚙️ [TRANSFORMAÇÃO] Iniciando o tratamento dos dados")
    
    df_limpo = df.copy()

    #1. Removendo faixas duplicadas

    tamanho_antes = df_limpo.shape[0]
    df_limpo = df_limpo.drop_duplicates(subset=['track_id'])
    tamanho_depois = df_limpo.shape[0]
    print(f"Foram removidas {tamanho_antes - tamanho_depois} linhas duplicadas")

    #2. Removendo valores nulos

    df_limpo = df_limpo.dropna(subset=['track_name', 'artists', 'album_name'])
    print("Valores nulos removidos!")

    #3. Convertendo o tempo em minutos
    df_limpo['duration_min'] = df_limpo['duration_ms'] / 60000
    df_limpo['duration_min'] = df_limpo['duration_min'].round(2)
    print("Conversão da duração de faixa de ms para minutos realizada!")

    #4. Removendo outliers de duração
    tamanho_antes_filtro = df_limpo.shape[0]

    filtro_tempo = (df_limpo['duration_min'] >= 0.5) & (df_limpo['duration_min'] <= 15.0)
    df_limpo = df_limpo[filtro_tempo]

    tamanho_depois_filtro = df_limpo.shape[0]
    print(f"Filtro de duração: {tamanho_antes_filtro} - {tamanho_depois} linhas removidas do catálogo.")

    print(f"✅ [TRANSFORMAÇÃO] Concluída com sucesso! Volume final: {df_limpo.shape[0]} linhas.")


    return df_limpo



if __name__ == "__main__":
    print("Iniciando teste isolado na etapa de tratamento")

    from extract import carregar_dados_brutos
    
    CAMINHO_TESTE = "data/raw/dataset.csv"
    
    try:
        df_bruto = carregar_dados_brutos(CAMINHO_TESTE)
        df_tratado = transformar_dados_spotify(df_bruto)
        
        print("\n👀 Amostra do dado transformado:")
        print(df_tratado[['track_name', 'artists', 'duration_min']].head(3))
        print("\n🎉 O teste local do transform funcionou perfeitamente!")
    except Exception as e:
        print(f"🚨 O teste local falhou! Motivo: {e}")


