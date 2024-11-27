
#TRABALHO DE ANALISE COLABORATIVA
#HUB IA SENAI 
#ORIENTADOR: Leonardo Goshi Sanches 
#MENTORIA: Jucenir da Silva Serafim
#DISCENTES: Cléber Fernando Paixão  e  Eduardo Felipe Ardigo Braga


# TRABALHO DE ANALISE COLABORATIVA
# BANCO DE DADOS: POLICIA FEDERAL

#================================================================================================================================================================





from datetime import datetime
import pandas as pd
import os
import streamlit as st


# 1 PASSO - IDENTIFICAR O (1 LOTE) ARQUIVO CSV PARA ANALISE - MOTIVO: SEPARADORES IGUAIS
arquivos_csv = [
    r"/home/cleber-7-turma-hub-ia/Documentos/PRPF/Acidentes-de-Transito-no-BR/2022.csv",
    r"/home/cleber-7-turma-hub-ia/Documentos/PRPF/Acidentes-de-Transito-no-BR/2024.csv"
]

# 2 LISTANDO E ARMAZENANDO O DATAFRAME
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

# 3 IDENTIFICAR O (2 LOTE) ARQUIVO CSV PARA ANALISE - MOTIVO: SEPARADORES IGUAIS
arquivos_csv = [
    r"/home/cleber-7-turma-hub-ia/Documentos/PRPF/Acidentes-de-Transito-no-BR2021.csv",
    r"/home/cleber-7-turma-hub-ia/Documentos/PRPF/Acidentes-de-Transito-no-BR/2023.csv"
]

# 4 CONVERTENDO A COLUNA (ID) PARA TRAZER O TIPO INT32
df['id'] = df['id'].astype('int32')  

st.dataframe(df)

# 5 LISTANDO E ARMAZENANDO O OUTRO DATAFRAME
dataframes2 = []

# Sobre o carregamento csv
for caminho in arquivos_csv:
    if os.path.exists(caminho):
        print(f"Lendo o arquivo: {caminho}")
        df2 = pd.read_csv(caminho, encoding='latin1', sep=';', on_bad_lines='skip')
        dataframes2.append(df2)
    else:
        print(f"Arquivo não encontrado: {caminho}")

# 6 ABSORVENDO DOIS DATAFRAMES
lista_dataframes = dataframes + dataframes2

# 7 CONCATENANDO OS DATAFRAMES
df_completo = pd.concat(lista_dataframes, ignore_index=True)
df_completo.tail() #final do dataframe |  Head(cabeca)


# ATENÇÃO!!
# Para mostrar todas as colunas no dataframe
# usar o comando: df_completo.columns
# Sobre as primeiras linhas do DataFrame combinado
# pprecrint("\nDados combinados:")


# 8 COMBINANDO AS PRIMEIRAS COLUNAS DO DATAFRAME
arquivo_csv = 'dados_combinados.csv'
df_completo.to_csv(arquivo_csv, index=False)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df_completo.columns = df_completo.columns.str.strip()  # Aqui  é feito a remoção dos espaços
df_completo.columns = df_completo.columns.str.lower()  # Aqui é feito a conversão para minusculo 



# 9 TRATANDO OS VALORES "NAN"
for col in df_completo.columns:
    if df_completo[col].dtype in ['int64', 'float64']:
       df_completo[col] = df_completo[col].fillna(df_completo[col].mean())

    elif df_completo[col].dtype == 'object':
         df_completo[col] = df_completo[col].fillna(df_completo[col].mode()[0])

# 10 CRIAR E ATRIBUIR DATATIMEE
#  Aqui vamos criar a coluna datetime e atribuir o tipo 'datetime' com as informações contidas dentro dos parenteses e com o tipo escolhido
#    Filtrar linhas onde a concatenação falha

mask = ~(df_completo['data_inversa'].str.match(r'\d{4}-\d{2}-\d{2}') & df_completo['horario'].str.match(r'\d{2}:\d{2}:\d{2}'))
problematic_rows = df_completo[mask]
print(problematic_rows)

df_completo = df_completo[~mask]
df_completo['datetime'] = pd.to_datetime(df_completo['data_inversa'] + ' ' + df_completo['horario'], format='%Y-%m-%d %H:%M:%S') 
df_completo.head()

# ATENÇÃO!!
# Quando quiser ver uma coluna especifica dois tipos de visao
# Utlizar o comando:   df_completo['datetime']
# Utilizar o comando: df_completo.datetime
# Mostra a descrição mas nao o tipo das colunas numericas
# df_completo.describe()

df_completo.info()

# 11 MOSTRANDO O TIPO DF
df_completo.head()

# 12 DEFINIÇÃO DOS FORMATOS DIA-MES-ANO
data_atual = datetime.now()
dia_da_semana = data_atual.strftime("%A")
periodo = data_atual.strftime("%B")
ano = data_atual.year
print('DATA ATUAL:', data_atual)
print('DIA DA SEMANA: ',dia_da_semana)
print('MÊS:', periodo)
print('ANO:', ano)

# 13 DEFININDO OS PERÍODOS DO DIA

hora_atual = data_atual.hour
if 6 <= hora_atual < 12:
    periodo = 'Manhã'
elif 12 <= hora_atual < 18:
    periodo = 'Tarde'
else:
    periodo = 'Noite'

# 14 CRIANDO UMA VARIAVEL PARA RECEBER O PERIODO DO DIA
periodo_dia = f'{dia_da_semana}, {ano}, {periodo}'
print('PERÍODO DO DIA:', periodo_dia)

# 15 ANALISANDO A DF 
df_completo.describe()

# 16 RESUMO DAS COLUNAS NUMERICAS
print("\nResumo estatístico:")
print(df_completo.describe())

# 17 ANALISANDO AS COLUNAS DA DF 
df_classificacao_causa = df_completo[['classificacao_acidente', 'causa_acidente']]
df_tipo_municipio = df_completo[['tipo_acidente', 'municipio']]
df_fase_horario = df_completo[['fase_dia', 'horario']]
df_feridos = df_completo[['mortos', 'feridos_leves', 'feridos_graves', 'ilesos', 'ignorados', 'feridos']]
df_condicao_metereologica = df_completo[['condicao_metereologica']]
df_localizacao = df_completo[['latitude', 'longitude']]
df_data = df_completo[['data_inversa', 'datetime']]

# 18 CONVERTENDO AS COLUNAS  'object' PARA 'str'
df_completo = df_completo.applymap(lambda x: str(x) if isinstance(x, str) else x)

# 19 CONVERTENDO AS COLUNAS PARA  string OU category
df['classificacao_acidente'] = df['classificacao_acidente'].astype('category')

# ou
df['classificacao_acidente'] = df['classificacao_acidente'].astype('str')

st.dataframe(df)

# 20 SUBSTITUINDO VALORES nulos OU pSUBSTITUINDO POR VALOR ESPECIFICO
df['classificacao_acidente'] = df['classificacao_acidente'].fillna('Desconhecido')

# Ou removendo as linhas com valores nulos na coluna
df = df.dropna(subset=['classificacao_acidente'])

st.dataframe(df)

# 21 CONVERTENDO O DATAFRAME PARA TIPO ARROWW
import pyarrow as pa

table = pa.Table.from_pandas(df)
st.write(table)


# 22 FAZENDO A CORRELAÇÃO DOS DADOS
contagem_classificacao_causa = df_classificacao_causa.groupby(['classificacao_acidente', 'causa_acidente']).size().reset_index(name='contagem')


# 23 CCONTAGEM DOS TIPOS "tipos acidente, municipios + fase do dia + horário"
contagem_tipo_municipio = df_tipo_municipio.groupby(['tipo_acidente', 'municipio']).size().reset_index(name='contagem')
contagem_fase_horario = df_fase_horario.groupby(['fase_dia', 'horario']).size().reset_index(name='contagem')

# 24 EXIBINDO AS PRIMEIRAS LINHAS DO DATAFRAME PARA CHECAGEM DO TRATAMENTO DE DADOS
print(contagem_classificacao_causa.head())
print(contagem_tipo_municipio.head())
print(contagem_fase_horario.head())

# 25 VISUALIZANDO A TABELA COMPLETA
print(contagem_classificacao_causa)
print(contagem_tipo_municipio)
print(contagem_fase_horario)

# 26 FASE: PREPARANDO A PARTE VISUAL NO STREAMLIT
import streamlit as st
import pandas as pd

# Reanalise dos dados
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

# 27 CRIANDO UM GRAFICO DE BARRAS PARA 'classificacao_acidente'
fig = px.bar(contagem_classificacao_causa, x='classificacao_acidente', y='contagem', color='causa_acidente', title="Classificação e Causa do Acidente")
st.plotly_chart(fig)
selected_columns = st.multiselect("Escolha as colunas para análise", df_completo.columns.tolist(), default=['classificacao_acidente', 'causa_acidente', 'tipo_acidente'])
df_selecionado = df_completo[selected_columns]
print(df_selecionado,'esse é o df')

# 28 DEFININDO UM FILTRO PARA O municipio
municipio_filtro = st.selectbox('Selecione o Município', df_completo['municipio'].unique())
df_filtrado = df_completo[df_completo['municipio'] == municipio_filtro]

# 29 ANALISE COM O DATAFRAME FILTRADO
st.write(df_filtrado)

# 3O CRIANDO O ARQUIVO "graficos.py" PARA DEMONSTRAR A SEGREGAÇÃO DOS DADOS POR MEIO DESSA CLASSE

# Fim.