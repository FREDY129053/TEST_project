import uuid

from .users_and_companies import UserAndCompany

from tortoise import fields
from tortoise.models import Model


class User(Model):
  id = fields.UUIDField(pk=True, default=uuid.uuid4)
  username = fields.CharField(max_length=50, unique=True)
  email = fields.CharField(max_length=50, unique=True)
  is_superuser = fields.BooleanField(default=False) 

  companies: fields.ReverseRelation["UserAndCompany"]

  class Meta:
    table = "users"