import pandas as pd
import os

def carregar_dados_brutos(caminho_arquivo: str) -> pd.DataFrame:

    if not os.path.exists(caminho_arquivo):

        raise FileNotFoundError(f"❌ Erro de extração: O arquivo no caminho {caminho_arquivo} não foi encontrado!")
    
    print(f"🔁 [EXTRAÇÃO] Arquivo localizado! Lendo dados brutos de: {caminho_arquivo}")

    df_bruto = pd.read_csv(caminho_arquivo)

    print(f"✅ [EXTRAÇÃO] Sucesso! Carregadas {df_bruto.shape[0]} linhas e {df_bruto.shape[1]} colunas.")

    return df_bruto