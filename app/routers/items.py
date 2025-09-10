from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

# Endpoint to get all items
@router.get("/", response_model=List[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

# Endpoint to create a new item
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    # Create a new item model instance, linking it to the logged-in user
    new_item = models.Item(owner_id=current_user.id, **item.model_dump())
    
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    
    return new_item