from app.database import engine
from sqlalchemy import inspect

# Crear un inspector para mirar la base de datos
inspector = inspect(engine)

# Listar todas las tablas que existen
print("Tablas en la base de datos:", inspector.get_table_names())
