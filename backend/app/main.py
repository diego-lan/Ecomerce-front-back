from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, database, models, schemas


app = FastAPI()


# Dependencia para obtener la sesión de DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/productos")
def listar_productos(db: Session = Depends(get_db)):
    return crud.get_productos(db)


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database, crud

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# CREATE
@app.post("/productos", response_model=schemas.Producto)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    return crud.crear_producto(db, producto)

# READ (todos)
@app.get("/productos", response_model=list[schemas.Producto])
def listar_productos(db: Session = Depends(database.get_db)):
    return crud.listar_productos(db)

# READ (uno)
@app.get("/productos/{producto_id}", response_model=schemas.Producto)
def obtener_producto(producto_id: int, db: Session = Depends(database.get_db)):
    producto = crud.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# UPDATE
@app.put("/productos/{producto_id}", response_model=schemas.Producto)
def actualizar_producto(producto_id: int, datos: schemas.ProductoUpdate, db: Session = Depends(database.get_db)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# DELETE
@app.delete("/productos/{producto_id}", response_model=schemas.Producto)
def eliminar_producto(producto_id: int, db: Session = Depends(database.get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto
