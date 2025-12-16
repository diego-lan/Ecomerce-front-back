from app.database import SessionLocal
from app.crud import crear_producto

# Abrir sesión
db = SessionLocal()

# Insertar un producto de prueba
producto = crear_producto(db, nombre="Laptop", precio=1200.0, stock=5)

print("Producto insertado:", producto.id, producto.nombre, producto.precio, producto.stock)

# Cerrar sesión
db.close()
