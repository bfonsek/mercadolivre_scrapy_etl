import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data/quotes.db')

df = pd.read_sql_query('SELECT * FROM mercadolibre_itens', conn)

conn.close()

# Titulo do dash
st.title('Pesquisa de Mercado - Tenis Mercado Livre')

# Subtitulo
st.subheader('Principais KPIs do Sistema')
col1, col2, col3 = st.columns(3)

# KPI 1 - Numero total de itens
total_itens = df.shape[0]
col1.metric(label='Numero Total de Itens', value=total_itens)

# KPI 2 - Numero de marcas unicas
unique_brands = df['brand'].nunique()
col2.metric(label='Numero de Marcas Unicas', value=unique_brands)

# KPI 3 - Preco Medio Novo (em reais)
average_new_price = df['new_price_product'].mean()
col3.metric(label='Preço Médio Novo (R$)', value=f"{average_new_price:.2f}")

# Marcas mais encontradas
st.subheader('Marcas mais encontradas')
col1, col2 = st.columns([4,2])
top_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

# Preco Medio por Marca
st.subheader('Preço Médio por Marca')
col1, col2 = st.columns([4,2])
average_price_by_brand = df.groupby('brand')['new_price_product'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Review por marca
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4,2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)
