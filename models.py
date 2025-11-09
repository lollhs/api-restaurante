from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True)
    platos = relationship("Plato", back_populates="categoria")

class Plato(Base):
    __tablename__ = "platos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    precio = Column(Float)
    id_categoria = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="platos")

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    telefono = Column(String)
    pedidos = relationship("Pedido", back_populates="cliente")

class Mesero(Base):
    __tablename__ = "meseros"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    pedidos = relationship("Pedido", back_populates="mesero")

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id"))
    id_mesero = Column(Integer, ForeignKey("meseros.id"))
    total = Column(Float)
    cliente = relationship("Cliente", back_populates="pedidos")
    mesero = relationship("Mesero", back_populates="pedidos")
