import uuid
import app.src.repository.user as userRepo

from typing import List, Union

from app.src.schemas.user import UserSchema, UserSchemaCreate

async def getUsers() -> List[UserSchema]:
  return await userRepo.getAllUsers()


async def getUser(id: uuid.UUID) -> Union[UserSchema, None]:
  return await userRepo.getUserInfo(id=id)


async def getCompanyUsers(company_id: uuid.UUID) -> List[UserSchema]:
  return await userRepo.getCompanyUsers(company_id=company_id)


async def createUser(user: UserSchemaCreate) -> Union[UserSchema, None]:
  return await userRepo.createUser(
    username=user.username,
    email=user.email,
    is_super_user=user.is_super_user
  )


async def updateUser(user: UserSchema):
  return await userRepo.updateUser(
    id=user.id,
    username=user.username,
    email=user.email,
    is_super_user=user.is_super_user
  )

async def deleteUser(id: uuid.UUID):
  return await userRepo.deleteUser(id=id)

async def loginUser(username: str, email: str):
  return await userRepo.loginUser(username=username, email=email)