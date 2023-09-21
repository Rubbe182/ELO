import streamlit as st
import pandas as pd


# Crea tu DataFrame
tu_dataframe = pd.read_csv('Classification.csv')

# Título de la aplicación
st.title('Filtrar DataFrame por Liga')

# Sidebar para la selección múltiple
ligas_seleccionadas = st.sidebar.multiselect('Selecciona Ligas', tu_dataframe['League'].unique())

# Filtra el DataFrame basado en las ligas seleccionadas
df_filtrado = tu_dataframe[tu_dataframe['League'].isin(ligas_seleccionadas)]

# Muestra el DataFrame filtrado
st.write('DataFrame Filtrado:', df_filtrado)
