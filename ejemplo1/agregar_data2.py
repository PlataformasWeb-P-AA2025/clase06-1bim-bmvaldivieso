from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

