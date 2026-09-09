from sqlalchemy import Column, Integer, String, Float, Datetime
from datetime import datetime 
from app.database import Base

class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    monto = Column(Float, nullable=False)
    tipo = Column(String(10), nullable=False)
    fecha = Column(Datetime, default=datetime.utcnow, index=True)
    categoria = Column(String(100), nullable=False)
    descripcion = Column(String(255) , nullable=True)



    
