# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List

# This schema is used for returning user data (no password)
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

# THIS IS THE MISSING SCHEMA
# It defines the fields required to create a new user.
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# This is our base schema for an Item, with common fields.
class ItemBase(BaseModel):
    title: str
    description: str | None = None

# This schema is for creating an Item.
class ItemCreate(ItemBase):
    pass

# This is the schema for data we send back to the user.
# It includes the owner's details by nesting the UserResponse schema.
class ItemResponse(ItemBase):
    id: int
    owner_id: int
    owner: UserResponse 

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None