from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Hash the password from the user request
    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password

    # Create a new SQLAlchemy User model instance
    new_user = models.User(**user.model_dump())
    
    # Add the new user to the session, commit to the database, and refresh
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user