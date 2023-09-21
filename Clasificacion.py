import streamlit as st
import pandas as pd


# Crea tu DataFrame
tu_dataframe = pd.read_csv('Classification.csv')

# Título de la aplicación
st.title('Clasificacion Ligas Europa')

ligas_seleccionadas = st.multiselect('Selecciona Ligas', tu_dataframe['League'].unique())

# Filtra el DataFrame basado en las ligas seleccionadas
df_filtrado = tu_dataframe[tu_dataframe['League'].isin(ligas_seleccionadas)]
df_filtrado=df_filtrado[['Rk', 'Squad', 'MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts', 'Pts/MP',
       'xG', 'xGA', 'xGD', 'xGD/90', 'Last 5', 'Attendance', 'Top Team Scorer',
       'Goalkeeper']]


# Muestra el DataFrame filtrado
st.write(df_filtrado.head(20))
