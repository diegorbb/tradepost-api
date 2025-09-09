# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List

# This schema will be used when we return a User, so it doesn't show their password
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

# This is our base schema for an Item, with the fields that are common
# to both creating and viewing an item.
class ItemBase(BaseModel):
    title: str
    description: str | None = None

# This schema is specifically for creating an Item. For now it's simple,
# but it gives us flexibility to add more fields for creation later.
class ItemCreate(ItemBase):
    pass

# This is the schema for the data we will send back to the user.
# It includes the data from ItemBase, plus the id, owner_id, and
# the nested owner information.
class ItemResponse(ItemBase):
    id: int
    owner_id: int
    owner: UserResponse

    class Config:
        from_attributes = True