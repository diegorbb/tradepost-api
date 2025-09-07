from pydantic import BaseModel, EmailStr

# Properties to receive via API on user creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Properties to return via API, hiding the password
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True