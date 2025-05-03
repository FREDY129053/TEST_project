import uuid

from typing import List, Union

from app.src.db.models import User, UserAndCompany

async def getAllUsers() -> List[User]:
  users = await User.all()

  return users


async def getUserInfo(id: uuid.UUID) -> Union[User, None]:
  user = await User.get_or_none(id=id)

  return user

async def getCompanyUsers(company_id: uuid.UUID) -> List[User]:
  links = await UserAndCompany.filter(company=company_id).prefetch_related("user")
  
  return [link.user for link in links]


async def createUser(username: str, email: str, is_super_user: bool = False):
  return await User.create(username=username, email=email, is_superuser=is_super_user)


async def updateUser(id: uuid.UUID, username: str, email: str, is_super_user: bool) -> bool:
  user = await User.get_or_none(id=id)
  if not user:
    return False
  
  user.username = username
  user.email = email
  user.is_superuser = is_super_user

  updated = await user.save()

  return updated is None


async def deleteUser(id: uuid.UUID) -> bool:
  user = await User.get_or_none(id=id)
  if not user:
    return False

  return await user.delete() is None


async def loginUser(username: str, email: str):
  return await User.get_or_none(username=username, email=email)