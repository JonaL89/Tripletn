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


import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title("Análisis de Datos de Vehículos en Venta")

# Crear gráfico de dispersión de odometer vs price
st.subheader("Gráfico de Dispersión: Kilometraje vs Precio")
fig = px.scatter(car_data, x="odometer", y="price",
                 title="Relación entre Kilometraje y Precio",
                 labels={"odometer": "Kilometraje", "price": "Precio"},
                 opacity=0.6)

st.plotly_chart(fig)

manufacturer_counts = car_data['manufacturer'].value_counts().reset_index()
manufacturer_counts.columns = ['manufacturer', 'count']  # Renombrar columnas correctamente

st.subheader("Cantidad de Vehículos por Fabricante")
fig_bar = px.bar(manufacturer_counts,
                 x='manufacturer', y='count',
                 labels={'manufacturer': 'Fabricante', 'count': 'Cantidad'},
                 title='Cantidad de Vehículos por Fabricante')
st.plotly_chart(fig_bar)


car_data['posting_date'] = pd.to_datetime(car_data['posting_date'])
car_data['year'] = car_data['posting_date'].dt.year
posts_per_year = car_data['year'].value_counts().sort_index()

posting_counts = car_data['posting_date'].value_counts().reset_index()
posting_counts.columns = ['posting_date', 'count']  # Renombrar columnas correctamente

st.subheader("Tendencia de Publicaciones por Año")
fig_line = px.line(posting_counts,
                   x='posting_date', y='count',
                   labels={'posting_date': 'Año de Publicación', 'count': 'Cantidad'},
                   title='Tendencia de Publicaciones por Año')
st.plotly_chart(fig_line)


price_condition = car_data.groupby('condition')['price'].mean().reset_index()
price_condition.columns = ['condition', 'price']  # Renombrar columnas correctamente

st.subheader("Distribución de Precios por Condición del Vehículo")
fig_box = px.box(price_condition,
                 x='condition', y='price',
                 labels={'condition': 'Condición del Vehículo', 'price': 'Precio Promedio'},
                 title='Distribución de Precios por Condición del Vehículo')
st.plotly_chart(fig_box)

