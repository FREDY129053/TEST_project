import uuid

from typing import List

from app.src.db.models import Company, UserAndCompany


async def getAllCompanies() -> List[Company]:
  companies = await Company.all()

  return companies


async def getCompanyInfo(id: uuid.UUID) -> Company:
  company = await Company.get_or_none(id=id)

  return company

async def getCompaniesByUser(user_id: uuid.UUID) -> List[Company]:
  companies = await UserAndCompany.filter(user=user_id).prefetch_related("company")

  return [company.company for company in companies]



async def createCompany(name: str, description: str):
  return await Company.create(name=name, description=description)


async def updateCompany(id: uuid.UUID, name: str, description: str):
  company = await Company.get_or_none(id=id)
  if not company:
    return None
  
  company.name = name
  company.description = description

  return await company.save()


async def deleteCompany(id: uuid.UUID):
  company = await Company.get_or_none(id=id)
  if not company:
    return None

  return await company.delete()
