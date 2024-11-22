
from datetime import datetime
import pandas as pd
import os

# Lista dos arquivos CSV
arquivos_csv = [
    r"2022.csv",
    r"2024.csv"
]

# Lista para armazenar os DataFrame
dataframes = []

# Sobre o carregamento csv
for caminho in arquivos_csv:
    if os.path.exists(caminho):
        print(f"Lendo o arquivo: {caminho}")
        df = pd.read_csv(caminho, sep=',', on_bad_lines='skip')
        dataframes.append(df)
    else:
        print(f"Arquivo não encontrado: {caminho}")

from datetime import datetime
import pandas as pd
import os

# Lista dos arquivos CSV
arquivos_csv = [
    r"2021.csv",
    r"2023.csv"
]

# Lista para armazenar os DataFrames
dataframes2 = []

# Sobre o carregamento csv
for caminho in arquivos_csv:
    if os.path.exists(caminho):
        print(f"Lendo o arquivo: {caminho}")
        df2 = pd.read_csv(caminho, encoding='latin1', sep=';', on_bad_lines='skip')
        dataframes2.append(df2)
    else:
        print(f"Arquivo não encontrado: {caminho}")

# Sobre juntar os 2 dataframes por causa dos separadores
lista_dataframes = dataframes + dataframes2

# Sobre a concatenação
df_completo = pd.concat(lista_dataframes, ignore_index=True)
df_completo.tail() #final do dataframe |  Head(cabeca)


# mostrar todas as colunas no dataframe
#df_completo.columns

# Sobre as primeiras linhas do DataFrame combinado
#print("\nDados combinados:")


# Sobre as primeiras colunas do DataFrame combinado
arquivo_csv = 'dados_combinados.csv'
df_completo.to_csv(arquivo_csv, index=False)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df_completo.columns = df_completo.columns.str.strip()  # Remover espaços extras
df_completo.columns = df_completo.columns.str.lower()  # Converter para minúsculas, se necessário



# Sobre valores NaN
for col in df_completo.columns:
    if df_completo[col].dtype in ['int64', 'float64']:
       df_completo[col] = df_completo[col].fillna(df_completo[col].mean())

    elif df_completo[col].dtype == 'object':
         df_completo[col] = df_completo[col].fillna(df_completo[col].mode()[0])

# Aqui vamos criar a coluna datetime e atribuir o tipo 'datetime' com as informações contidas dentro dos parenteses e com o tipo escolhido
# Filtrar linhas onde a concatenação falha
mask = ~(df_completo['data_inversa'].str.match(r'\d{4}-\d{2}-\d{2}') & df_completo['horario'].str.match(r'\d{2}:\d{2}:\d{2}'))
problematic_rows = df_completo[mask]
print(problematic_rows)

df_completo = df_completo[~mask]
df_completo['datetime'] = pd.to_datetime(df_completo['data_inversa'] + ' ' + df_completo['horario'], format='%Y-%m-%d %H:%M:%S') 
df_completo.head()

#Quando quiser ver uma coluna especifica dois tipos de visao
#df_completo['datetime']
#df_completo.datetime
df_completo.info()

# Mostra o tipo
df_completo.head()

# Mostra a descrição mas nao o tipo das colunas numericas
#df_completo.describe()

data_atual = datetime.now()
dia_da_semana = data_atual.strftime("%A")
periodo = data_atual.strftime("%B")
ano = data_atual.year
print('DATA ATUAL:', data_atual)
print('DIA DA SEMANA: ',dia_da_semana)
print('MÊS:', periodo)
print('ANO:', ano)

# Sobre definir o periodo do dia

hora_atual = data_atual.hour
if 6 <= hora_atual < 12:
    periodo = 'Manhã'
elif 12 <= hora_atual < 18:
    periodo = 'Tarde'
else:
    periodo = 'Noite'

# Sobre criar uma variavel para receber os perídos do dia
periodo_dia = f'{dia_da_semana}, {ano}, {periodo}'
print('PERÍODO DO DIA:', periodo_dia)

# Sobre analisar os atributos
df_completo.describe()

# Resumo estatístico das colunas numericas
print("\nResumo estatístico:")
print(df_completo.describe())

# Análise das colunas
df_classificacao_causa = df_completo[['classificacao_acidente', 'causa_acidente']]
df_tipo_municipio = df_completo[['tipo_acidente', 'municipio']]
df_fase_horario = df_completo[['fase_dia', 'horario']]
df_feridos = df_completo[['mortos', 'feridos_leves', 'feridos_graves', 'ilesos', 'ignorados', 'feridos']]
df_condicao_metereologica = df_completo[['condicao_metereologica']]
df_localizacao = df_completo[['latitude', 'longitude']]
df_data = df_completo[['data_inversa', 'datetime']]

# Correlação entre elas
contagem_classificacao_causa = df_classificacao_causa.groupby(['classificacao_acidente', 'causa_acidente']).size().reset_index(name='contagem')


# Contando os tipos de acidente, municipios + fase do dia + horário 
contagem_tipo_municipio = df_tipo_municipio.groupby(['tipo_acidente', 'municipio']).size().reset_index(name='contagem')
contagem_fase_horario = df_fase_horario.groupby(['fase_dia', 'horario']).size().reset_index(name='contagem')

# Exibição das primeiras linhas
print(contagem_classificacao_causa.head())

print(contagem_tipo_municipio.head())

print(contagem_fase_horario.head())

# Exibição das tabelas completas
print(contagem_classificacao_causa)
print(contagem_tipo_municipio)
print(contagem_fase_horario)

# Fase do Streamlit - processando os dados da parte visual
import streamlit as st
import pandas as pd

# Continuar com as análises...
df_selecionado = df_completo[['classificacao_acidente', 'causa_acidente', 'tipo_acidente', 'municipio', 'horario', 'fase_dia']]


contagem_classificacao_causa = df_selecionado.groupby(['classificacao_acidente', 'causa_acidente']).size().reset_index(name='contagem')
contagem_tipo_municipio = df_selecionado.groupby(['tipo_acidente', 'municipio']).size().reset_index(name='contagem')
contagem_fase_horario = df_selecionado.groupby(['fase_dia', 'horario']).size().reset_index(name='contagem')

st.title("Análise de Acidentes")

st.subheader("Classificação e Causa do Acidente")
st.dataframe(contagem_classificacao_causa)

st.subheader("Tipo de Acidente e Município")
st.dataframe(contagem_tipo_municipio)

st.subheader("Fase do Dia e Horário")
st.dataframe(contagem_fase_horario)

df_selecionado['causa_acidente'].fillna(df_selecionado['causa_acidente'].mode()[0])
df_selecionado['tipo_acidente'].fillna(df_selecionado['tipo_acidente'].mode()[0])
df_selecionado['municipio'].fillna(df_selecionado['municipio'].mode()[0])
df_selecionado['horario'].fillna(df_selecionado['horario'].mode()[0])
df_selecionado['fase_dia'].fillna(df_selecionado['fase_dia'].mode()[0])

import plotly.express as px

# Aqui vamos criar um gráfico de barras interativo para a 'classificacao_acidente'
fig = px.bar(contagem_classificacao_causa, x='classificacao_acidente', y='contagem', color='causa_acidente', title="Classificação e Causa do Acidente")
st.plotly_chart(fig)

# O usuário poderá escolher as colunas para análise
selected_columns = st.multiselect("Escolha as colunas para análise", df_completo.columns.tolist(), default=['classificacao_acidente', 'causa_acidente', 'tipo_acidente'])

# Filtrar o DataFrame com as colunas selecionadas
df_selecionado = df_completo[selected_columns]
print(df_selecionado,'esse é o df')
# Filtro interativo para o município
municipio_filtro = st.selectbox('Selecione o Município', df_completo['municipio'].unique())
df_filtrado = df_completo[df_completo['municipio'] == municipio_filtro]

# Análises com o DataFrame filtrado
st.write(df_filtrado)