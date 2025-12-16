# E-Commerce Front & Back

This is a full-stack e-commerce project built from scratch.  
The backend is implemented with FastAPI and SQLite, and the frontend will be added soon.

## Backend Features

- FastAPI server with full CRUD for products
- SQLite database using SQLAlchemy ORM
- Pydantic v2 models for input/output validation
- Interactive API docs via Swagger UI (`/docs`)
- Modular architecture: `main.py`, `crud.py`, `models.py`, `schemas.py`, `database.py`

## Endpoints

- `POST /productos` → Create a new product
- `GET /productos` → List all products
- `GET /productos/{id}` → Get product by ID
- `PUT /productos/{id}` → Update product fields
- `DELETE /productos/{id}` → Delete product

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ecommerce-front-back.git
   cd ecommerce-front-back

## Install dependencies: 
pip install fastapi uvicorn sqlalchemy pydantic

## Run the server:
uvicorn app.main:app --reload --app-dir backend

## Open in browser:
http://127.0.0.1:8000/docs

