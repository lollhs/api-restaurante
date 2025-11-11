from sqlalchemy.orm import Session
from models import Categoria, Plato, Cliente, Mesero, Pedido
from schemas import CategoriaCreate, PlatoCreate, ClienteCreate, MeseroCreate, PedidoCreate


#  categorias
def get_categorias(db: Session):
    return db.query(Categoria).all()

def create_categoria(db: Session, categoria: CategoriaCreate):
    nueva_categoria = Categoria(nombre=categoria.nombre)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

def delete_categoria(db: Session, categoria_id: int):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if categoria:
        db.delete(categoria)
        db.commit()
        return True
    return False


# crud platos
def get_platos(db: Session):
    return db.query(Plato).all()

def create_plato(db: Session, plato: PlatoCreate):
    nuevo_plato = Plato(
        nombre=plato.nombre,
        precio=plato.precio,
        id_categoria=plato.id_categoria
    )
    db.add(nuevo_plato)
    db.commit()
    db.refresh(nuevo_plato)
    return nuevo_plato

def delete_plato(db: Session, plato_id: int):
    plato = db.query(Plato).filter(Plato.id == plato_id).first()
    if plato:
        db.delete(plato)
        db.commit()
        return True
    return False


# clientes
def get_clientes(db: Session):
    return db.query(Cliente).all()

def create_cliente(db: Session, cliente: ClienteCreate):
    nuevo_cliente = Cliente(
        nombre=cliente.nombre,
        telefono=cliente.telefono
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

def delete_cliente(db: Session, cliente_id: int):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente:
        db.delete(cliente)
        db.commit()
        return True
    return False


# meseros
def get_meseros(db: Session):
    return db.query(Mesero).all()

def create_mesero(db: Session, mesero: MeseroCreate):
    nuevo_mesero = Mesero(
        nombre=mesero.nombre,
        turno=mesero.turno
    )
    db.add(nuevo_mesero)
    db.commit()
    db.refresh(nuevo_mesero)
    return nuevo_mesero

def delete_mesero(db: Session, mesero_id: int):
    mesero = db.query(Mesero).filter(Mesero.id == mesero_id).first()
    if mesero:
        db.delete(mesero)
        db.commit()
        return True
    return False


# pedidos
def get_pedidos(db: Session):
    return db.query(Pedido).all()

def create_pedido(db: Session, pedido: PedidoCreate):
    nuevo_pedido = Pedido(
        id_cliente=pedido.id_cliente,
        id_mesero=pedido.id_mesero,
        id_plato=pedido.id_plato,
        fecha=pedido.fecha
    )
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)
    return nuevo_pedido

def delete_pedido(db: Session, pedido_id: int):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if pedido:
        db.delete(pedido)
        db.commit()
        return True
    return False
