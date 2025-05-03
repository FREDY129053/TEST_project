from app.src.enums.role import UserRole

from pydantic import BaseModel, UUID4

class UserAndCompany(BaseModel):
  user_id: UUID4
  company_id: UUID4
  role: str

class UserAndCompanyCreate(BaseModel):
  user_id: UUID4
  company_id: UUID4
  role: UserRole

