import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar saludos
saludos = session.query(Saludo2).order_by(Saludo2.id).all()

# Mostrar con Streamlit
st.title("Listado de Saludos")

for saludo in saludos:
    st.subheader(f"Saludo ID: {saludo.id}")
    st.write(f"**Mensaje:** {saludo.mensaje}")
    st.write(f"**Tipo:** {saludo.tipo}")
    st.write(f"**Origen:** {saludo.origen}")
    st.markdown("---")

# Presentación en tabla
st.title("Tabla de Saludos")

lista = []

for s in saludos:
    diccionario = {"ID": s.id, "Mensaje": s.mensaje, "Tipo": s.tipo, "Origen": s.origen}
    lista.append(diccionario)

st.dataframe(lista)
