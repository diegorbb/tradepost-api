from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from typing import List, Optional # <-- Import Optional
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

# Get all items with Pagination and Search
@router.get("/", response_model=List[schemas.ItemResponse])
def get_items(db: Session = Depends(get_db), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    
    items = db.query(models.Item).filter(
        models.Item.title.contains(search)).limit(limit).offset(skip).all()
    
    return items

# Endpoint to create a new item
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    new_item = models.Item(owner_id=current_user.id, **item.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Get one specific item by ID
@router.get("/{id}", response_model=schemas.ItemResponse)
def get_item(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id: {id} was not found")
    
    return item

# Endpoint to delete an item
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    item_query = db.query(models.Item).filter(models.Item.id == id)
    item = item_query.first()
    
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id: {id} does not exist")
    
    if item.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    item_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Endpoint to update an item
@router.put("/{id}", response_model=schemas.ItemResponse)
def update_item(id: int, updated_item: schemas.ItemCreate, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    item_query = db.query(models.Item).filter(models.Item.id == id)
    item = item_query.first()

    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with id: {id} does not exist")

    if item.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    item_query.update(updated_item.model_dump(), synchronize_session=False)
    db.commit()

    return item_query.first()