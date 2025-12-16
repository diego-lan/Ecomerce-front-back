from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Producto(Base):
    __tablename__ = "productos"   # nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    stock = Column(Integer)
