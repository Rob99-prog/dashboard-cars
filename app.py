import streamlit as st
import pandas as pd
import plotly.express as px

# Línea de debug para confirmar que app.py se ejecuta
st.write("🚀 app.py está arrancando…")

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Título y encabezado
st.title("Dashboard de Anuncios de Coches")
st.header("Explora tu dataset de vehículos")

# Botón para histograma
if st.button("Mostrar histograma de kilometraje"):
    st.write("Histograma de la columna 'odometer'")
    fig1 = px.histogram(
        df,
        x='odometer',
        nbins=30,
        title='Distribución de kilometraje'
    )
    st.plotly_chart(fig1, use_container_width=True)

# Botón para scatter plot
if st.button("Mostrar scatter precio vs. año"):
    st.write("Scatter plot de 'model_year' vs. 'price'")
    fig2 = px.scatter(
        df,
        x='model_year',
        y='price',
        trendline='ols',
        title='Precio vs. Año'
    )
    st.plotly_chart(fig2, use_container_width=True)
