from pydantic import BaseModel, UUID4, Field

class UserSchema(BaseModel):
  id: UUID4
  username: str
  email: str
  is_super_user: bool
  
  class Config:
    from_attributes=True


class UserSchemaCreate(UserSchema):
  id: UUID4 = Field(exclude=True)


class UserLogin(BaseModel):
  username: str
  email: str