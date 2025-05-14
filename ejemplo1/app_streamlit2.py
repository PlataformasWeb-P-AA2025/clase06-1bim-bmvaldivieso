import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar saludos
saludos = session.query(Saludo).order_by(Saludo.id).all()

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

lista = [{"ID": s.id, "Mensaje": s.mensaje, "Tipo": s.tipo, "Origen": s.origen} for s in saludos]

st.dataframe(lista)
