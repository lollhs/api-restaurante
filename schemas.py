from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int
    class Config:
        from_attributes  = True

class PlatoBase(BaseModel):
    nombre: str
    precio: float
    id_categoria: int

class PlatoCreate(PlatoBase):
    pass

class Plato(PlatoBase):
    id: int
    class Config:
        orm_mode = True

class ClienteBase(BaseModel):
    nombre: str
    telefono: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    class Config:
        orm_mode = True

class MeseroBase(BaseModel):
    nombre: str

class MeseroCreate(MeseroBase):
    pass

class Mesero(MeseroBase):
    id: int
    class Config:
        orm_mode = True

class PedidoBase(BaseModel):
    id_cliente: int
    id_mesero: int
    total: float

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    class Config:
        orm_mode = True
