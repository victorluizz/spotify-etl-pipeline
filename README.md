---

```markdown
# 🧬 Spotify Data DNA - Pipeline ETL

Este projeto implementa um pipeline de Engenharia de Dados completo (ETL - Extract, Transform, Load) utilizando Python, Pandas e SQLite para analisar e tratar dados de mais de 114.000 faixas musicais do Spotify. 

O objetivo principal é extrair os dados brutos, realizar uma Análise Exploratória de Dados (EDA) para mapear o comportamento estatístico das músicas, aplicar regras de negócio para limpeza de anomalias/outliers e persistir os dados purificados em um banco de dados relacional local para consultas analíticas.

## 🏗️ Arquitetura do Projeto

O projeto foi estruturado de forma modular seguindo as boas práticas de desenvolvimento de software:

```text
spotify-etl-pipeline/
├── data/                  # Armazenamento local de dados (ignorado no Git)
│   ├── raw/               # Dataset bruto (dataset.csv)
│   └── spotify_data.db    # Banco de dados SQLite gerado pelo pipeline
├── notebook/
│   └── exploratoria.ipynb # Laboratório de Análise Exploratória (EDA)
├── src/                   # Código-fonte modular do pipeline
│   ├── __init__.py
│   ├── extract.py         # Módulo de Extração de dados
│   ├── transform.py       # Módulo de Transformação e Limpeza (Peneira Lógica)
│   └── load.py            # Módulo de Carga no banco de dados relacional
├── .gitignore             # Filtro de arquivos para o repositório
├── main.py                # Maestro que orquestra a execução do pipeline
└── README.md              # Documentação do projeto

```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem principal:** Python 3.11+
* **Manipulação de Dados:** Pandas
* **Visualização de Dados & Estatística:** Matplotlib, Seaborn
* **Banco de Dados:** SQLite3
* **Ambiente de Desenvolvimento:** VS Code (Jupyter Extension)

---

## 🔬 Insights da Análise Exploratória (EDA)

Durante a fase de experimentação no Jupyter Notebook, foram identificados comportamentos cruciais no dataset que guiaram as regras de engenharia no pipeline:

1. **Distorção por Outliers de Duração:** O catálogo comercial do Spotify é dominado por faixas de **3 a 4.5 minutos**. No entanto, o dataset bruto continha registros com duração zerada (bugs de extração) e arquivos de até **87 minutos** (provavelmente podcasts ou compilações), o que distorcia a média aritmética do tempo.
2. **O Mar de Músicas Esquecidas:** Cerca de 25% do dataset possui popularidade inferior a 17 (escala 0-100), revelando um volume massivo de faixas sem audiência ativa.
3. **Paradoxo da Popularidade:** A análise de correlação linear (Pearson) provou que características sonoras como **Energia ($0.001$)** e **Valência ($-0.041$)** não possuem relação direta com o sucesso de uma música. O sucesso no Spotify é um fenômeno complexo ditado por fatores externos (marketing, comunidade, tendências sociais e algoritmos de recomendação).

---

## ⚙️ Regras de Transformação Aplicadas

Com base nos insights, o módulo `src/transform.py` aplica uma **peneira lógica vetorizada** no Pandas que executa:

* **Remoção de Duplicatas:** Eliminação de linhas repetidas usando o identificador único da música (`track_id`).
* **Tratamento de Nulos:** Descarte de registros com valores ausentes em colunas críticas textuais como `track_name` e `artists`.
* **Engenharia de Atributos:** Criação da coluna de tempo legível em minutos (`duration_min`).
* **Filtro Estatístico de Tempo:** Remoção de faixas com menos de 30 segundos e acima de 15 minutos, expurgando ruídos e garantindo um catálogo estritamente musical (reduzindo o dataset de 114.000 para **89.587 linhas puras**).
```
