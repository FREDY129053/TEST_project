from typing import List, Union
import uuid

from app.src.db.models import UserAndCompany, User, Company
from app.src.enums.role import UserRole

async def getAllCompanies() -> List[UserAndCompany]:
  return await UserAndCompany.all()


async def createUserAndCompany(user_id: uuid.UUID, company_id: uuid.UUID, role: UserRole = UserRole.member) -> Union[UserAndCompany, None]:
  user = await User.get_or_none(id=user_id)
  company = await Company.get_or_none(id=company_id)

  if not user or not company:
    return None

  return await UserAndCompany.create(user=user, company=company, role=role)