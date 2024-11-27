# **Análise de Dados de Acidentes**

## **Descrição do Projeto**
Este projeto realiza uma análise exploratória de dados de acidentes de trânsito, utilizando dados fornecidos pela Polícia Federal. Ele permite a visualização de estatísticas, gráficos interativos e mapas de acidentes, facilitando a identificação de padrões e insights relevantes.

---

## **Autores**
- **Orientador:** Leonardo Goshi Sanches  
- **Mentoria:** Jucenir da Silva Serafim  
- **Discentes:**  
  - Cléber Fernando Paixão  
  - Eduardo Felipe Ardigo Braga  

---

## **Objetivo**
Este projeto foi desenvolvido como parte de um trabalho colaborativo no curso do Hub IA SENAI. O principal objetivo é consolidar o aprendizado em análise de dados utilizando Python e bibliotecas como Pandas, Plotly, Seaborn e Streamlit, além de gerar insights para auxiliar a análise de acidentes.

---

## **Principais Funcionalidades**
1. **Carregamento de Dados**: 
   - Leitura de arquivos CSV com diferentes configurações de separadores e codificações.  
2. **Tratamento de Dados**:  
   - Limpeza de valores nulos.  
   - Padronização de colunas.  
   - Criação de uma coluna de data e hora para análises temporais.  
3. **Análises Estatísticas e Visuais**:  
   - Resumo estatístico das colunas numéricas.  
   - Gráficos interativos utilizando Plotly e Streamlit.  
4. **Interface Interativa**:  
   - Exibição de tabelas dinâmicas e gráficos para facilitar a análise.  
   - Filtros para selecionar colunas ou municípios específicos.  
   - Mapas interativos para visualização geográfica.  
5. **Métricas de Impacto**: 
   - Exibição de métricas como número total de mortes e acidentes sem feridos.  

---

## **Requisitos**
Para executar este projeto, é necessário instalar as dependências listadas no arquivo `requirements.txt`.  

### **Dependências**
- `matplotlib`  
- `numpy`  
- `pandas`  
- `plotly`  
- `seaborn`  
- `streamlit`  

---

## **Instalação**
1. Clone este repositório:
   ```bash
   git clone https://github.com/Teopx/Acidentes-de-Transito-no-BR.git
   cd Acidentes-de-Transito-no-BR
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Certifique-se de que os arquivos CSV (`2021.csv`, `2022.csv`, `2023.csv` e `2024.csv`) estão no mesmo diretório que o script principal.

---

## **Como Usar**
1. Execute o script Streamlit:
   ```bash
   streamlit run analise_dados_acidentes.py
2. Acesse a interface interativa no navegador, que estará disponível no endereço:
   http://localhost:8501
3. Explore as funcionalidades:
   - Visualize tabelas dinâmicas e gráficos interativos.
   - Filtre os dados por colunas ou municípios.
   - Analise a distribuição geográfica e as classificações dos acidentes.

---

## **Arquitetura do Código**
- Funções Principais:
   - carregar_csv: Carrega arquivos CSV e trata inconsistências.
   - tratar_valores_nulos: Substitui valores nulos por médias ou modas.
   - criar_coluna_datetime: Combina colunas de data e hora em um único formato padrão.
- Pipeline de Análise:
   - Carregamento e concatenação de dados.
   - Limpeza e tratamento de valores.
   - Análises estatísticas e geração de gráficos.

---

## **Exemplos de Uso**
- Gráficos de Barras: Comparação de classificações e causas de acidentes.
- Mapas Interativos: Visualização de acidentes com base em latitude e longitude.
- Gráficos de Pizza: Proporção de diferentes classificações de acidentes.
