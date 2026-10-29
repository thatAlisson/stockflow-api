from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    sku: str = Field(..., min_length=3, max_length=50)
    quantity: int = Field(..., ge=0)
    min_threshold: int = Field(..., ge=0)

class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True

class MovementCreate(BaseModel):
    amount: int = Field(..., gt=0)
    type: str = Field(..., pattern="^(IN|OUT)$")
