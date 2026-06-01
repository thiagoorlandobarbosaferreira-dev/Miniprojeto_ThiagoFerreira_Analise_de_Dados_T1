import csv
import pandas as pd
from datetime import datetime

# ==========================================================
# SPRINT 1 - IMPORTAÇÃO DOS DADOS
# ==========================================================

arquivo_csv = "Varejo.csv"
dados_limpos = []

print("=== INICIANDO PROCESSAMENTO DOS DADOS ===")

try:
    with open(arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            # ==================================================
            # SPRINT 2 E 3 - LIMPEZA DOS DADOS
            # ==================================================

            # Categoria vazia
            if "CATEGORIA" in linha:
                if linha["CATEGORIA"] is None or linha["CATEGORIA"].strip() == "":
                    linha["CATEGORIA"] = "Sem Categoria"

            # Número de filhos vazio
            if "NUMERO_FILHOS" in linha:
                if linha["NUMERO_FILHOS"] is None or linha["NUMERO_FILHOS"].strip() == "":
                    linha["NUMERO_FILHOS"] = "0"

            # Conversão de data
            if "DADOS" in linha:
                try:
                    linha["DATA_DATA_HORA"] = datetime.strptime(
                        linha["DADOS"],
                        "%Y-%m-%d"
                    )
                except:
                    linha["DATA_DATA_HORA"] = None

            dados_limpos.append(linha)

except FileNotFoundError:
    print("Arquivo Varejo.csv não encontrado.")
    exit()

# ==========================================================
# CONVERSÃO PARA DATAFRAME
# ==========================================================

df = pd.DataFrame(dados_limpos)

# ==========================================================
# INFORMAÇÕES DA BASE
# ==========================================================

print("\n=== INFORMAÇÕES DA BASE ===")

print("Quantidade de registros:", df.shape[0])
print("Quantidade de colunas:", df.shape[1])

print("\nColunas:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)

# ==========================================================
# NULOS
# ==========================================================

print("\n=== VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())

# ==========================================================
# DUPLICATAS
# ==========================================================

print("\n=== DUPLICATAS ===")
print(df.duplicated().sum())

# ==========================================================
# AJUSTE DE TIPOS
# ==========================================================

if "NUMERO_FILHOS" in df.columns:
    df["NUMERO_FILHOS"] = pd.to_numeric(
        df["NUMERO_FILHOS"],
        errors="coerce"
    ).fillna(0)

if "DATA_DATA_HORA" in df.columns:
    df["DATA_DATA_HORA"] = pd.to_datetime(
        df["DATA_DATA_HORA"],
        errors="coerce"
    )

# ==========================================================
# REMOÇÃO DE DUPLICATAS
# ==========================================================

df = df.drop_duplicates()

# ==========================================================
# SPRINT 4 - ESTATÍSTICA DESCRITIVA
# ==========================================================

if "NUMERO_FILHOS" in df.columns:

    filhos = df["NUMERO_FILHOS"]

    print("\n=== ESTATÍSTICA DESCRITIVA ===")

    print("Média:", filhos.mean())
    print("Mediana:", filhos.median())

    if not filhos.mode().empty:
        print("Moda:", filhos.mode()[0])

    print("Desvio Padrão:", filhos.std())
    print("Máximo:", filhos.max())
    print("Mínimo:", filhos.min())
    print("Contagem:", filhos.count())

    print("\nQuartis:")
    print(filhos.describe())

# ==========================================================
# SPRINT 5 - AGRUPAMENTOS
# ==========================================================

print("\n=== AGRUPAMENTO 1 ===")

if "CATEGORIA" in df.columns:
    agrupamento_categoria = (
        df.groupby("CATEGORIA")
        .size()
        .reset_index(name="TOTAL_COMPRAS")
    )

    print(agrupamento_categoria)

print("\n=== AGRUPAMENTO 2 ===")

if "NUMERO_FILHOS" in df.columns:
    agrupamento_filhos = (
        df.groupby("NUMERO_FILHOS")
        .size()
        .reset_index(name="TOTAL_TRANSACOES")
    )

    print(agrupamento_filhos)

# ==========================================================
# EXPORTAÇÃO
# ==========================================================

df.to_csv(
    "df_limpo.csv",
    index=False,
    encoding="utf-8"
)

print("\nArquivo df_limpo.csv gerado com sucesso!")

# ==========================================================
# CONCLUSÕES
# ==========================================================

print("\n=== INSIGHTS DA ANÁLISE ===")

print("1. Foram identificados e tratados valores nulos.")
print("2. Categorias vazias foram preenchidas com 'Sem Categoria'.")
print("3. Registros duplicados foram removidos.")
print("4. Foi realizada conversão e validação de datas.")
print("5. Foram geradas estatísticas da coluna NUMERO_FILHOS.")
print("6. Foram analisados padrões através de agrupamentos.")

