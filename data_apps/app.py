import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sqlalchemy import create_engine
import openai
from scipy.spatial.distance import cosine
import os
import seaborn as sns

# Conectar ao banco de dados PostgreSQL (Neon) usando SQLAlchemy
DB_URL = os.getenv("NEON_DB_URL")

# Criar a conexão usando SQLAlchemy
engine = create_engine(DB_URL)

# Carregar dados da tabela diretamente do PostgreSQL (Neon)
def load_data():
    query = "select * FROM public.electronics_reviews LIMIT 500"
    df = pd.read_sql(query, engine)
    return df

# Carregar dados
df = load_data()

# Página de introdução
st.title("Data App - Exploração de Dados Amazon Reviews")
st.write("Esse é o Data App para explorar as avaliações de produtos da Amazon.")

# Análise de Similaridade entre Produtos
st.header("1. Similaridade entre Produtos")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['reviewtext'])

similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

product_id = st.selectbox('Escolha o ID do Produto para encontrar similaridade', df['asin'].unique())

st.write(f"Produto Selecionado: {product_id}")
selected_product_idx = df[df['asin'] == product_id].index[0]

similar_products_idx = similarity_matrix[selected_product_idx].argsort()[-6:-1][::-1]
similar_products = df.iloc[similar_products_idx]

st.write(f"Produtos semelhantes ao produto com ID {product_id}:")
st.dataframe(similar_products[['asin', 'reviewtext']])

# Análise Exploratória de Dados (EDA) com GPT
st.header("2. Análise Exploratória de Dados (EDA) sem GPT limite de tokens excedido")

#os.environ['HTTP_PROXY'] = ''
#os.environ['HTTPS_PROXY'] = ''
#openai.proxy = None

# Substitua a chave pela sua chave real aqui
#openai.api_key = "OPENAI_API_KEY"

#def get_gpt_eda_analysis(text):
    # Prompt para enviar ao GPT
#    prompt = f"Realize uma análise exploratória dos dados e descreva as características principais do seguinte texto:\n\n{text}"
    
    # Usando o método correto para a versão 2.14.0 da OpenAI
#    response = openai.Completion.create(
 #       model="gpt-3.5-turbo",  # Ou use "gpt-4" se preferir
 #       prompt=prompt,          # Passando o prompt
 #       max_tokens=50          # Limitar a resposta a 150 tokens
 #   )
    
    # Retornando o texto da resposta
 #   return response.choices[0].text.strip()

# Exemplo de uso com um texto de exemplo do dataframe
#sample_text = df['reviewtext'].iloc[0]  # Pegando um texto da primeira linha
#eda_result = get_gpt_eda_analysis(sample_text)

df.dropna(subset=['reviewtext', 'overall'], inplace=True)

eda_summary = df.describe()

plt.figure(figsize=(10, 6))
sns.histplot(df['overall'], kde=True, bins=5, color='skyblue', edgecolor='black')
plt.title("Distribuição das Avaliações (Overall)")
plt.xlabel("Avaliação")
plt.ylabel("Número de Avaliações")
st.pyplot()

df['review_length'] = df['reviewtext'].apply(lambda x: len(x.split()))
plt.figure(figsize=(10, 6))
sns.histplot(df['review_length'], kde=True, color='green', bins=30)
plt.title("Distribuição do Comprimento das Avaliações")
plt.xlabel("Número de Palavras")
plt.ylabel("Número de Avaliações")
st.pyplot()

numeric_cols = df.select_dtypes(include=[np.number]).columns
plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matriz de Correlação")
st.pyplot()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['review_length'], y=df['overall'], color='purple')
plt.title("Relação entre o Comprimento das Avaliações e as Notas")
plt.xlabel("Número de Palavras na Avaliação")
plt.ylabel("Nota (Overall)")
st.pyplot()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='asin', order=df['asin'].value_counts().index[:10])
plt.title("Distribuição dos Produtos Mais Avaliados")
plt.xlabel("Produto (ID)")
plt.ylabel("Número de Avaliações")
plt.xticks(rotation=90)
st.pyplot()

# Exibindo a análise no Streamlit
#st.write("Análise Exploratória Gerada pelo GPT:")
#st.write(eda_result)

# Visualizações com Matplotlib
st.header("3. Visualizações")

# Exemplo de gráfico: Distribuição de Avaliações
st.subheader("Distribuição de Avaliações (Overall)")
fig, ax = plt.subplots()
ax.hist(df['overall'], bins=5, color='skyblue', edgecolor='black')
ax.set_xlabel('Avaliação')
ax.set_ylabel('Número de Avaliações')
st.pyplot(fig)

