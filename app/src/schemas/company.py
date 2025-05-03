from pydantic import BaseModel, UUID4

class CompanySchema(BaseModel):
  id: UUID4
  name: str
  description: str

  class Config:
    from_attributes=True


class CompanySchemaCreate(BaseModel):
  name: str
  description: str