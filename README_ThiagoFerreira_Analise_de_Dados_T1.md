# Mini-Projeto Avaliativo: Análise de Dados com Python (Varejo)
**Estudante:** Thiago Orlando Barbosa Ferreira  
**Turma:** Analise_de_Dados_T1  
**Data:** 01 de Junho de 2026  

---

## 📋 Como Executar o Projeto
1. Certifique-se de ter o Python 3 e a biblioteca `pandas` instalada (`pip install pandas`).
2. Baixe a base de dados `Varejo.csv` sugerida no Kaggle e salve-a na mesma pasta deste script.
3. Execute o script utilizando o VS Code, terminal ou Google Colab:
```bash
python Miniprojeto_ThiagoFerreira_Analise_de_Dados_T1.py```


## 🧠 Reflexão Teórica: ETL e Qualidade de Dados
O processo de **ETL (Extract, Transform, Load)** é a espinha dorsal de qualquer análise de dados confiável ou sistema de Business Intelligence (BI). 
* **Extração:** Dados brutos de sistemas de varejo frequentemente vêm com ruídos, campos vazios e formatações inconsistentes. A leitura estruturada e nativa via `csv.DictReader` garante o controle total da entrada de dados.
* **Transformação (Qualidade de Dados):** Dados nulos em dimensões físicas ou categorias vazias distorcem relatórios operacionais. A tomada de decisão baseada em dados sem tratamento de tipos (como manter datas como texto) impede análises temporais e agregações corretas. Tratar as inconsistências garante a integridade da base antes de alimentar dashboards.
* **Carga:** O dado limpo e tipificado é estruturado para consumo ágil através do Pandas.

---

## 📊 Conclusões e Insights Obtidos (Análise Exploratória)
* **Tratamento de Categorias:** Foram identificados registros com categorias nulas, os quais foram preenchidos preventivamente com a string `"Sem Categoria"`, evitando a perda de histórico de vendas na volumetria total.
* **Perfil Familiar:** A análise descritiva da coluna `NUMERO_FILHOS` indicou a concentração do público-alvo. A mediana e a moda ajudam a entender se o portfólio de produtos do varejo deve focar em famílias grandes ou casais sem filhos.
* **Gargalos de Datas:** Constatou-se a presença de strings de data fora do padrão nativo, que foram corrigidas e padronizadas usando o módulo `datetime` para habilitar análises de sazonalidade cronológica.
* **Performance por Categoria:** O agrupamento (`groupby`) revelou quais categorias dominam o volume de transações, permitindo estratégias de estoque direcionadas.
* **Problemas Remanescentes na Base:** Mesmo após a limpeza básica de nulos e duplicatas, a base ainda apresenta outliers em valores de venda e possíveis cadastros de clientes com dados demográficos desatualizados que necessitam de regras de negócio mais severas na origem do sistema (CRM).

