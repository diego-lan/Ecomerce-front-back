from pydantic import BaseModel, constr, conint

class ProductoBase(BaseModel):
    nombre: constr(min_length=1, max_length=50)
    precio: float
    stock: conint(ge=0)

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: constr(min_length=1, max_length=50) | None = None
    precio: float | None = None
    stock: conint(ge=0) | None = None

class Producto(ProductoBase):
    id: int

    class Config:
        # Ajuste para Pydantic v2
        from_attributes = True
