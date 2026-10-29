from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StockFlow API",
    description="API de Gerenciamento de Estoque e Logística",
    version="1.0.0"
)

@app.post("/products/", response_model=schemas.ProductResponse, status_code=201)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.sku == product.sku).first()
    if db_product:
        raise HTTPException(status_code=400, detail="SKU já cadastrado no sistema")
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=List[schemas.ProductResponse])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.post("/products/{product_id}/movement")
def stock_movement(product_id: int, movement: schemas.MovementCreate, db: Session = Depends(get_db)):
    return crud.register_movement(db=db, product_id=product_id, movement=movement)
