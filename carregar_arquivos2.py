
#TRABALHO DE ANALISE COLABORATIVA
#HUB IA SENAI 
#ORIENTADOR: Leonardo Goshi Sanches 
#MENTORIA: Jucenir da Silva Serafim
#DISCENTES: Cléber Fernando Paixão  e  Eduardo Felipe Ardigo Braga


# TRABALHO DE ANALISE COLABORATIVA
# BANCO DE DADOS: POLICIA FEDERAL

#================================================================================================================================================================

from datetime import datetime
import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Função para carregar arquivos CSV
def carregar_csv(arquivos_csv, sep, encoding=None):
    dataframes = []
    for caminho in arquivos_csv:
        if os.path.exists(caminho):
            print(f"Lendo o arquivo: {caminho}")
            df = pd.read_csv(caminho, sep=sep, encoding=encoding, on_bad_lines='skip')
            dataframes.append(df)
        else:
            print(f"Arquivo não encontrado: {caminho}")
    return dataframes

# Função para tratar valores nulos
def tratar_valores_nulos(df):
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].mean())
        elif df[col].dtype == 'object':
            df[col] = df[col].fillna(df[col].mode()[0])
    return df

# Função para criar coluna de data e hora
def criar_coluna_datetime(df):
    mask = ~(df['data_inversa'].str.match(r'\d{4}-\d{2}-\d{2}') & df['horario'].str.match(r'\d{2}:\d{2}:\d{2}'))
    problematic_rows = df[mask]
    print(problematic_rows)
    df = df[~mask]
    df['datetime'] = pd.to_datetime(df['data_inversa'] + ' ' + df['horario'], format='%Y-%m-%d %H:%M:%S')
    return df

# Carregar arquivos CSV com diferentes separadores
arquivo_csv_1 = [r"2021.csv"]
arquivo_csv_2 = [r"2022.csv"]
arquivo_csv_3 = [r"2023.csv"]
arquivo_csv_4 = [r"2024.csv"]

# Carregar DataFrames
dataframe_1 = carregar_csv(arquivo_csv_1, sep=';', encoding='latin1')
dataframe_2 = carregar_csv(arquivo_csv_2, sep=',')
dataframe_3 = carregar_csv(arquivo_csv_3, sep=';', encoding='latin1')
dataframe_4 = carregar_csv(arquivo_csv_4, sep=',')

# Concatenar DataFrames
lista_dataframes = dataframe_1 + dataframe_2 + dataframe_3 + dataframe_4
df_completo = pd.concat(lista_dataframes, ignore_index=True)
df_completo.to_csv("dados_combinados.csv", index=False)

# Limpeza de dados
df_completo.columns = df_completo.columns.str.strip()  # Remover espaços extras
df_completo.columns = df_completo.columns.str.lower()  # Converter para minúsculas

# Tratar valores nulos
df_completo = tratar_valores_nulos(df_completo)

# Criar coluna datetime
df_completo = criar_coluna_datetime(df_completo)

# Exibir informações do DataFrame
df_completo.info()
print(df_completo.head())

# Obter data atual
data_atual = datetime.now()
dia_da_semana = data_atual.strftime("%A")
periodo = data_atual.strftime("%B")
ano = data_atual.year
hora_atual = data_atual.hour

# Definir período do dia
if 6 <= hora_atual < 12:
    periodo_dia = 'Manhã'
elif 12 <= hora_atual < 18:
    periodo_dia = 'Tarde'
else:
    periodo_dia = 'Noite'

# Exibir informações sobre o período do dia
periodo_dia_str = f'{dia_da_semana}, {ano}, {periodo}'
print('PERÍODO DO DIA:', periodo_dia_str)

# Resumo estatístico das colunas numéricas
print("\nResumo estatístico:")
print(df_completo.describe())

# Análise de atributos
df_classificacao_causa = df_completo[['classificacao_acidente', 'causa_acidente']]
df_tipo_municipio = df_completo[['tipo_acidente', 'municipio']]
df_fase_horario = df_completo[['fase_dia', 'horario']]
df_feridos = df_completo[['mortos', 'feridos_leves', 'feridos_graves', 'ilesos', 'ignorados', 'feridos']]
df_condicao_metereologica = df_completo[['condicao_metereologica']]
df_localizacao = df_completo[['latitude', 'longitude']]
df_data = df_completo[['data_inversa', 'datetime']]

# Contagem de categorias
contagem_classificacao_causa = df_classificacao_causa.groupby(['classificacao_acidente', 'causa_acidente']).size().reset_index(name='contagem')
contagem_tipo_municipio = df_tipo_municipio.groupby(['tipo_acidente', 'municipio']).size().reset_index(name='contagem')
contagem_fase_horario = df_fase_horario.groupby(['fase_dia', 'horario']).size().reset_index(name='contagem')

# Exibir as primeiras linhas das contagens
print(contagem_classificacao_causa.head())
print(contagem_tipo_municipio.head())
print(contagem_fase_horario.head())

# Visualizar a tabela completa
print(contagem_classificacao_causa)
print(contagem_tipo_municipio)
print(contagem_fase_horario)

# Análises de dados para visualização com Streamlit
df_selecionado = df_completo[['classificacao_acidente', 'causa_acidente', 'tipo_acidente', 'municipio', 'horario', 'fase_dia']]

contagem_classificacao_causa = df_selecionado.groupby(['classificacao_acidente', 'causa_acidente']).size().reset_index(name='contagem')
contagem_tipo_municipio = df_selecionado.groupby(['tipo_acidente', 'municipio']).size().reset_index(name='contagem')
contagem_fase_horario = df_selecionado.groupby(['fase_dia', 'horario']).size().reset_index(name='contagem')

# Streamlit interface
st.title("Análise de Acidentes")

st.subheader("Classificação e Causa do Acidente")
st.dataframe(contagem_classificacao_causa)

st.subheader("Tipo de Acidente e Município")
st.dataframe(contagem_tipo_municipio)

st.subheader("Fase do Dia e Horário")
st.dataframe(contagem_fase_horario)

# Preenchendo valores nulos para exibição no gráfico
df_selecionado.loc[:, 'causa_acidente'] = df_selecionado['causa_acidente'].fillna(df_selecionado['causa_acidente'].mode()[0])
df_selecionado.loc[:, 'tipo_acidente'] = df_selecionado['tipo_acidente'].fillna(df_selecionado['tipo_acidente'].mode()[0])
df_selecionado.loc[:, 'municipio'] = df_selecionado['municipio'].fillna(df_selecionado['municipio'].mode()[0])
df_selecionado.loc[:, 'horario'] = df_selecionado['horario'].fillna(df_selecionado['horario'].mode()[0])
df_selecionado.loc[:, 'fase_dia'] = df_selecionado['fase_dia'].fillna(df_selecionado['fase_dia'].mode()[0])

# Gráfico de barras interativo
fig = px.bar(contagem_classificacao_causa, x='classificacao_acidente', y='contagem', color='causa_acidente', title="Classificação e Causa do Acidente")
st.plotly_chart(fig)

# Filtro interativo para colunas
selected_columns = st.multiselect("Escolha as colunas para análise", df_completo.columns.tolist(), default=['classificacao_acidente', 'causa_acidente', 'tipo_acidente'])
df_selecionado = df_completo[selected_columns]
print(df_selecionado)

# Filtro interativo para o município
municipio_filtro = st.selectbox('Selecione o Município', df_completo['municipio'].unique())
df_filtrado = df_completo[df_completo['municipio'] == municipio_filtro]

# Análises com o DataFrame filtrado
st.write(df_filtrado)
