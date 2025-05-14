from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

import csv

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

# Leer el archivo CSV y agregar datos
with open('data/saludos_mundo.csv', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv, delimiter='|')
    for fila in lector:
        saludo = Saludo2(mensaje=fila['saludo'], tipo=fila['tipo'], origen=fila['origen'])
        session.add(saludo)

session.commit()