import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de coches usados 🚗')

# Botón para histograma
if st.button('Mostrar histograma de kilómetros'):
    st.write('Histograma de kilómetros recorridos:')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig)

# Botón para gráfico de dispersión
if st.button('Mostrar dispersión (km vs precio)'):
    st.write('Gráfico de dispersión:')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig)