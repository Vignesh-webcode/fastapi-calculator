from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Import the database helper and model directly from main
from main import get_db, DBProduct

router = APIRouter(
    prefix="/products",
    tags=["Products Management"]
)

class ProductCreate(BaseModel):
    name: str
    price: float

# 1. THE POST ENDPOINT (For saving data via Docs/Postman)
@router.post("/")
def save_product(item: ProductCreate, db: Session = Depends(get_db)):
    new_product = DBProduct(name=item.name, price=item.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Saved via clean architecture!", "product_id": new_product.id}

# 2. THE GET ENDPOINT (This will make your browser link work!)
@router.get("/")
def fetch_products(db: Session = Depends(get_db)):
    all_products = db.query(DBProduct).all()
    return {"total_items": len(all_products), "products": all_products}
