import streamlit as st
import pandas as pd
import plotly_express as px

#cargar los datos
df=pd.read_csv("/Users/franciscoisraelcanondoleon/Desktop/mi_proyecto/mi_6/vehicles_us.csv")

#creacion de boton histograma
st.header("Analisis de Datos")
boton_histograma=st.button("Crear Histograma")
if boton_histograma:
    st.write("Creacion de histograma de los datos de anuncio de ventas de coches") #mensaje
    #crear histograma
    fig=px.histogram(df, x="odometer")
    #mostrar grafico interactivo de Plotly
    st.plotly_chart(fig, use_container_width=True)

#creacion de boton dispersion
boton_dispersion= st.button("Crear Grafico de Dispersion")
if boton_dispersion:
    st.writre("Creacion de Grafico de Dispersion de los datos de anuncio de ventas de coches")
    #crear grafico
    fig=px.scatter(df, x="odometer")
    #mostrar el grafico interactivo
    st.plotly_chart(fig, use_container_width=True)