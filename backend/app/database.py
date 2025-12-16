# Importamos lo necesario de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión a la base de datos
# Usamos SQLite local, que crea un archivo llamado test.db en tu carpeta
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Motor de conexión
# connect_args={"check_same_thread": False} es necesario para SQLite en modo multihilo
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sesión local
# Esta clase SessionLocal nos permite abrir y cerrar sesiones con la base
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos ORM
# Todos tus modelos (tablas) van a heredar de esta Base
Base = declarative_base()

# Dependencia para FastAPI
# Esta función se usa en los endpoints con Depends(get_db)
# Abre una sesión, la entrega al endpoint y luego la cierra automáticamente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
