import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la app
st.title('Análisis de Datos de Vehículos')

# Gráfico de dispersión
st.subheader('Relación entre Precio y Año de Fabricación')

fig = px.scatter(
    car_data, 
    x='year', 
    y='price', 
    title='Gráfico de Dispersión: Precio vs Año de Fabricación',
    labels={'year': 'Año', 'price': 'Precio'}
)


st.plotly_chart(fig)

