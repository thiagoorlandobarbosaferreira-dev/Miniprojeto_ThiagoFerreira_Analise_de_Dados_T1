import csv
import pandas as pd
from datetime import datetime

# ==============================================================================
# SPRINT 1: IMPORTAÇÃO DOS DADOS
# ==============================================================================
arquivo_csv = "Varejo.csv"
dados_limpos = []

print("--- Iniciando o processamento dos dados via csv.DictReader ---")

# ==============================================================================
# SPRINT 2 & 3: TRATAMENTO, LIMPEZA DE NULOS E DATAS
# ==============================================================================
try:
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        leitor = csv.DictReader(file)
        
        for linha in leitor:
            # Lógica para preencher categorias vazias
            if not linha.get('CATEGORIA') or linha['CATEGORIA'].strip() == "":
                linha['CATEGORIA'] = "Sem Categoria"
                
            # Tratamento de nulos para número de filhos
            if not linha.get('NUMERO_FILHOS') or linha['NUMERO_FILHOS'].strip() == "":
                linha['NUMERO_FILHOS'] = "0"
                
            # Conversão de string de data utilizando o módulo datetime
            try:
                data_str = linha['DATA'].strip()
                linha['DATA_DATETIME'] = datetime.strptime(data_str, '%Y-%m-%d') 
            except (ValueError, KeyError):
                linha['DATA_DATETIME'] = None
                
            dados_limpos.append(linha)
except FileNotFoundError:
    print(f"Aviso: O arquivo '{arquivo_csv}' precisa estar na mesma pasta para execução local.")

# Convertendo para DataFrame Pandas para as Sprints 4 e 5
if dados_limpos:
    df = pd.DataFrame(dados_limpos)
    df['NUMERO_FILHOS'] = pd.to_numeric(df['NUMERO_FILHOS'], errors='coerce').fillna(0).astype(int)
    df = df.drop_duplicates()
else:
    # DataFrame fictício estruturado caso o arquivo não seja carregado no ambiente de nuvem
    df = pd.DataFrame({'NUMERO_FILHOS': [0, 1, 2, 1, 3, 0, 2], 'CATEGORIA': ['Eletro', 'Moda', 'Eletro', 'Alimentos', 'Moda', 'Alimentos', 'Eletro']})

# ==============================================================================
# SPRINT 4: ESTATÍSTICA DESCRITIVA
# ==============================================================================
print("\n--- ESTATÍSTICA DESCRITIVA: NÚMERO DE FILHOS DOS CLIENTES ---")
filhos = df['NUMERO_FILHOS']
estatisticas = {
    "Média": filhos.mean(),
    "Mediana": filhos.median(),
    "Desvio Padrão": filhos.std(),
    "Moda": filhos.mode().iloc[0] if not filhos.mode().empty else "N/A",
    "Máximo": filhos.max(),
    "Mínimo": filhos.min(),
    "Contagem": filhos.count(),
    "Q1 (25%)": filhos.quantile(0.25),
    "Q2 (50%)": filhos.quantile(0.50),
    "Q3 (75%)": filhos.quantile(0.75)
}
for k, v in statistics.items():
    print(f"{k}: {v}")

# ==============================================================================
# SPRINT 5: PADRÕES DE AGRUPAMENTO
# ==============================================================================
print("\n--- AGRUPAMENTO 1: Total de Compras por Categoria ---")
print(df.groupby('CATEGORIA').size().reset_index(name='Total_Compras'))

print("\n--- AGRUPAMENTO 2: Compras por Perfil de Filhos ---")
print(df.groupby('NUMERO_FILHOS').size().reset_index(name='Total_Transacoes'))

