import streamlit as st
import pandas as pd
import plotly_express as px

#cargar los datos
df=pd.read_csv("vehicles_us.csv")

#creacion de boton histograma
st.header("Analisis de Datos de Vehículos Usados en EE.UU.")
boton_histograma=st.button("Crear Histograma")
if boton_histograma:
    st.write("Distribución del Kilometraje de Vehículos en Anuncios") #mensaje
    #crear histograma
    fig=px.histogram(df, x="odometer")
    #mostrar grafico interactivo de Plotly
    st.plotly_chart(fig, use_container_width=True)

#creacion de boton dispersion
boton_dispersion= st.button("Crear Grafico de Dispersion")
if boton_dispersion:
    st.write("Gráfico de Dispersión del Kilometraje de Vehículos")
    #crear grafico
    fig=px.scatter(df, x="odometer", y="price")
    #mostrar el grafico interactivo
    st.plotly_chart(fig, use_container_width=True)