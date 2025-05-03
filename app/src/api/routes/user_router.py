from app.src.helpers.jwt import create_jwt_token
import app.src.schemas.user as userSchemas
import app.src.services.user as userService
from app.src.api.middlewares.only_admin import admin_required

from typing import Dict, List
from uuid import UUID

from fastapi import APIRouter, HTTPException, status, Response, Depends
from fastapi.responses import JSONResponse


user_router = APIRouter(prefix='/user', tags=["Users"])


@user_router.post('/login')
async def login_user(data: userSchemas.UserLogin, response: Response):
  user = await userService.loginUser(username=data.username, email=data.email)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail="user not found"
    )
  
  # Генерация токена лучше вынести в services и возвращать его, а не так
  token = create_jwt_token({
    "uuid": str(user.id),
    "is_admin": user.is_superuser
  })

  response = JSONResponse(content={"message": "nice!"})
  response.set_cookie(key="test", value=token, httponly=True)

  return response

@user_router.get('/all', response_model=List[userSchemas.UserSchema])
async def get_all_users():
  """### Получение всех пользователей"""
  result = await userService.getUsers()

  return result

@user_router.get('/{id}', response_model=Dict[str, userSchemas.UserSchema])
async def get_user_info(id: UUID):
  """### Получение данных о пользователе по UUID"""
  result = await userService.getUser(id)

  if result:
    return JSONResponse(
      content={"user": userSchemas.UserSchema.model_validate(result)},
      status_code=status.HTTP_200_OK,
    )

  raise HTTPException(
    detail="user not found!",
    status_code=status.HTTP_404_NOT_FOUND,
  )

@user_router.get('/users/{company_uuid}', response_model=List[userSchemas.UserSchema])
async def get_all_users_of_company(company_uuid):
  result = await userService.getCompanyUsers(company_id=company_uuid)

  return result

@user_router.post('/', response_model=Dict[str, str])
async def create_user(user: userSchemas.UserSchemaCreate):
  result = await userService.createUser(user=user)

  if result:
    return JSONResponse(
      content={"message": "user created successfully"},
      status_code=status.HTTP_200_OK
    )
  
  raise HTTPException(
    detail="user not found!",
    status_code=status.HTTP_404_NOT_FOUND
  )

@user_router.put('/', response_model=Dict[str, str])
async def update_user(user: userSchemas.UserSchema):
  result = await userService.updateUser(user=user)

  if result:
    return JSONResponse(
      content={"message": "user updated successfully"},
      status_code=status.HTTP_200_OK
    )
  
  raise HTTPException(
    detail="user not found!",
    status_code=status.HTTP_404_NOT_FOUND
  )

@user_router.delete('/{id}', response_model=Dict[str, userSchemas.UserSchema])
async def delete_user_(id: UUID, _=Depends(admin_required)):
  """### Удаление данных о пользователе по UUID(ТОЛЬКО АДМИНЫ)"""
  result = await userService.deleteUser(id)

  if result:
    return JSONResponse(
      content={"message": "user deleted successfully"},
      status_code=status.HTTP_200_OK,
    )

  raise HTTPException(
    detail="user not found!",
    status_code=status.HTTP_404_NOT_FOUND,
  )