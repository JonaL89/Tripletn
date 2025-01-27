import streamlit as st
import pandas as pd
import plotly.express as px

# Lee los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Título de la app
st.title('Dashboard de Análisis de Vehículos')

# Crea un histograma
st.header('Histograma de Odometer')
fig = px.histogram(car_data, x="odometer")
st.plotly_chart(fig)
