import uuid
import app.src.repository.company as companyRepo

from typing import List, Union

from app.src.schemas.company import CompanySchema, CompanySchemaCreate

async def getCompanies() -> List[CompanySchema]:
  return await companyRepo.getAllCompanies()

async def getCompany(id: uuid.UUID) -> CompanySchema:
  return await companyRepo.getCompanyInfo(id=id)


async def getUsersCompanies(user_id: uuid.UUID) -> List[CompanySchema]:
  return await companyRepo.getCompaniesByUser(user_id=user_id)


async def createCompany(company: CompanySchemaCreate) -> Union[CompanySchema, None]:
  return await companyRepo.createCompany(
    name=company.name,
    description=company.description
  )


async def updateCompany(company: CompanySchema):
  return await companyRepo.updateCompany(
    id=company.id,
    name=company.name,
    description=company.description
  )

async def deleteCompany(id: uuid.UUID):
  return await companyRepo.deleteCompany(id=id)