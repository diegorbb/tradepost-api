# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List

# Schemas for Items

# This is our base schema for an Item, with common fields.
class ItemBase(BaseModel):
    title: str
    description: str | None = None

# This is the schema for returning an Item.
# We define it here so UserResponse can reference it.
class ItemResponse(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

# Schemas for Users

# This schema is used for returning user data.
# It now correctly includes a list of the items the user owns.
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    items: List[ItemResponse] = [] # The list of items owned by the user

    class Config:
        from_attributes = True

# It defines the fields required to create a new user.
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schemas for Creating/Updating Items

# This schema is for creating an Item.
class ItemCreate(ItemBase):
    pass

# This is a more detailed Item response that INCLUDES the owner info.
# We will use this in our "get all items" endpoint in the future if we wish.
class ItemResponseWithOwner(ItemResponse):
    owner: UserResponse

# Schemas for Auth/Tokens

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int | None = None