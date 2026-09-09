from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings


#Creamos el motor de conexion apuntando a NEON 
engine = create_engine(settings.DATABASE_URL)

#Creador de sesiones individuales para cada peticion HTTP
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Clase base de la que heredan nuestras tablas 
Base = declarative_base()

#Inyeccion de dependencias para abrir y cerrar la conexion de forma limpia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()