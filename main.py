from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API REST - Restaurante")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Categorías ---
@app.get("/categorias", response_model=list[schemas.Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.get_categorias(db)

@app.post("/categorias", response_model=schemas.Categoria)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.create_categoria(db, categoria)

@app.delete("/categorias/{categoria_id}")
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    return crud.delete_categoria(db, categoria_id)

# --- Platos ---
@app.get("/platos", response_model=list[schemas.Plato])
def listar_platos(db: Session = Depends(get_db)):
    return crud.get_platos(db)

@app.post("/platos", response_model=schemas.Plato)
def crear_plato(plato: schemas.PlatoCreate, db: Session = Depends(get_db)):
    return crud.create_plato(db, plato)

@app.delete("/platos/{plato_id}")
def eliminar_plato(plato_id: int, db: Session = Depends(get_db)):
    return crud.delete_plato(db, plato_id)

# --- Clientes ---
@app.get("/clientes", response_model=list[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db)

@app.post("/clientes", response_model=schemas.Cliente)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db, cliente)

@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return crud.delete_cliente(db, cliente_id)

# --- Meseros ---
@app.get("/meseros", response_model=list[schemas.Mesero])
def listar_meseros(db: Session = Depends(get_db)):
    return crud.get_meseros(db)

@app.post("/meseros", response_model=schemas.Mesero)
def crear_mesero(mesero: schemas.MeseroCreate, db: Session = Depends(get_db)):
    return crud.create_mesero(db, mesero)

@app.delete("/meseros/{mesero_id}")
def eliminar_mesero(mesero_id: int, db: Session = Depends(get_db)):
    return crud.delete_mesero(db, mesero_id)

# --- Pedidos ---
@app.get("/pedidos", response_model=list[schemas.Pedido])
def listar_pedidos(db: Session = Depends(get_db)):
    return crud.get_pedidos(db)

@app.post("/pedidos", response_model=schemas.Pedido)
def crear_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return crud.create_pedido(db, pedido)

@app.delete("/pedidos/{pedido_id}")
def eliminar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    return crud.delete_pedido(db, pedido_id)
