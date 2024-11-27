
from datetime import datetime
import os
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


# CRIANDO A PARTE VISUAL PARA O STREAMLIT
st.title("Análise de Dados de Acidentes de Trânsito")
st.sidebar.header("Filtros")

# RELACIONANDO OS CSV
arquivos_csv = ["2021.csv", "2022.csv", "2023.csv", "2024.csv"]
dataframes = []

for caminho in arquivos_csv:
    if os.path.exists(caminho):
        df = pd.read_csv(caminho, sep=',', encoding='latin1', on_bad_lines='skip')
        dataframes.append(df)
    else:
        st.warning(f"Arquivo não encontrado: {caminho}")

# CONCATENANDO OS DATAFRAMES
df_completo = pd.concat(dataframes, ignore_index=True)
df_completo.columns = df_completo.columns.str.strip().str.lower()

# TRATANDO OS DADOS NAN
for col in df_completo.columns:
    if df_completo[col].dtype in ['int64', 'float64']:
        df_completo[col] = df_completo[col].fillna(df_completo[col].mean())
    elif df_completo[col].dtype == 'object':
        df_completo[col] = df_completo[col].fillna(df_completo[col].mode()[0])

# AJUSTANDO OS CAMPOS DATA
df_completo['datetime'] = pd.to_datetime(df_completo['data_inversa'] + ' ' + df_completo['horario'], errors='coerce')
df_completo = df_completo.dropna(subset=['datetime'])

# INICIANDO A PARTE VISUAL COM GRAFICOS

# Gráfico 1: Tipos de Acidente
st.subheader("Distribuição dos Tipos de Acidente")
tipo_acidente_contagem = df_completo['tipo_acidente'].value_counts()
st.bar_chart(tipo_acidente_contagem)

# Gráfico 2: Acidentes por Município
st.subheader("Acidentes por Município")
municipio_contagem = df_completo['municipio'].value_counts().head(10)  # Mostrando os 10 principais
st.bar_chart(municipio_contagem)

# Gráfico 3: Acidentes por Período do Dia
st.subheader("Acidentes por Período do Dia")
fase_dia_contagem = df_completo['fase_dia'].value_counts()
fig, ax = plt.subplots()
ax.pie(fase_dia_contagem, labels=fase_dia_contagem.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Gráfico 4: Mortos e Feridos
st.subheader("Total de Mortos e Feridos")
feridos_mortos = df_completo[['mortos', 'feridos_leves', 'feridos_graves']].sum()
st.bar_chart(feridos_mortos)

# Gráfico 5: Causa dos Acidentes
st.subheader("Causas dos Acidentes")
causa_acidente_contagem = df_completo['causa_acidente'].value_counts().head(10)
st.bar_chart(causa_acidente_contagem)

st.write("Dados completos visualizados acima refletem o cenário atual dos acidentes analisados.")
