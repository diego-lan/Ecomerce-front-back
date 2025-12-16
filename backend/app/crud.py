from sqlalchemy.orm import Session
from . import models, schemas

# CREATE
def crear_producto(db: Session, producto: schemas.ProductoCreate):
    nuevo = models.Producto(**producto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# READ (todos)
def listar_productos(db: Session):
    return db.query(models.Producto).all()

# READ (uno)
def obtener_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

# UPDATE
def actualizar_producto(db: Session, producto_id: int, datos: schemas.ProductoUpdate):
    producto = obtener_producto(db, producto_id)
    if not producto:
        return None
    for campo, valor in datos.dict(exclude_unset=True).items():
        setattr(producto, campo, valor)
    db.commit()
    db.refresh(producto)
    return producto

# DELETE
def eliminar_producto(db: Session, producto_id: int):
    producto = obtener_producto(db, producto_id)
    if not producto:
        return None
    db.delete(producto)
    db.commit()
    return producto
