import streamlit as st
import pandas as pd


# Crea tu DataFrame
tu_dataframe = pd.read_csv('Classification.csv')
tu_dataframe =tu_dataframe.drop('Unnamed:0')

# Título de la aplicación
st.title('Clasificacion Ligas Europa')

ligas_seleccionadas = st.multiselect('Selecciona Ligas', tu_dataframe['League'].unique())

# Filtra el DataFrame basado en las ligas seleccionadas
df_filtrado = tu_dataframe[tu_dataframe['League'].isin(ligas_seleccionadas)]


# Muestra el DataFrame filtrado
st.write('DataFrame Filtrado:', df_filtrado)
