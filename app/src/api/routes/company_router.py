import app.src.services.company as companyService
import app.src.schemas.company as companySchemas

from uuid import UUID
from typing import Dict, List

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

company_router = APIRouter(prefix='/company', tags=["Companies"])

@company_router.get('/all', response_model=List[companySchemas.CompanySchema])
async def get_all_companies():
  """### Получение всех компаний"""
  result = await companyService.getCompanies()

  return result

@company_router.get('/{id}', response_model=Dict[str, companySchemas.CompanySchema])
async def get_company_info(id: UUID):
  result = await companyService.getCompany(id)

  if result:
    return JSONResponse(
      content={"company": companySchemas.CompanySchema.model_validate(result)},
      status_code=status.HTTP_200_OK,
    )

  raise HTTPException(
    detail="company not found!",
    status_code=status.HTTP_404_NOT_FOUND,
  )

@company_router.get('/companies/{user_uuid}', response_model=List[companySchemas.CompanySchema])
async def get_all_companies_of_user(user_uuid):
  result = await companyService.getUsersCompanies(user_id=user_uuid)

  return result

@company_router.post('/', response_model=Dict[str, str])
async def create_company(company: companySchemas.CompanySchemaCreate):
  result = await companyService.createCompany(company=company)

  if result:
    return JSONResponse(
      content={"message": "company created successfully"},
      status_code=status.HTTP_200_OK
    )
  
  raise HTTPException(
    detail="company not found!",
    status_code=status.HTTP_404_NOT_FOUND
  )

@company_router.put('/', response_model=Dict[str, str])
async def update_company(company: companySchemas.CompanySchema):
  result = await companyService.updateCompany(company=company)

  if result:
    return JSONResponse(
      content={"message": "company updated successfully"},
      status_code=status.HTTP_200_OK
    )
  
  raise HTTPException(
    detail="company not found!",
    status_code=status.HTTP_404_NOT_FOUND
  )


@company_router.delete('/{id}', response_model=Dict[str, companySchemas.CompanySchema])
async def delete_company(id: UUID):
  """### Удаление данных о компании по UUID"""
  result = await companyService.deleteCompany(id=id)

  if result:
    return JSONResponse(
      content={"message": "company deleted successfully"},
      status_code=status.HTTP_200_OK,
    )

  raise HTTPException(
    detail="company not found!",
    status_code=status.HTTP_404_NOT_FOUND,
  )