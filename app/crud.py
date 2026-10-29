from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def register_movement(db: Session, product_id: int, movement: schemas.MovementCreate):
    product = get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    if movement.type == "OUT":
        if product.quantity < movement.amount:
            raise HTTPException(status_code=400, detail="Estoque insuficiente")
        product.quantity -= movement.amount
    else:
        product.quantity += movement.amount

    db_movement = models.StockMovement(
        product_id=product_id,
        type=movement.type,
        amount=movement.amount
    )
    
    db.add(db_movement)
    db.commit()
    db.refresh(product)
    return {"message": "Movimentação registrada com sucesso", "current_stock": product.quantity}
