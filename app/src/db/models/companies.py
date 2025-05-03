import uuid

from .users_and_companies import UserAndCompany

from tortoise import fields
from tortoise.models import Model


class Company(Model):
  id = fields.UUIDField(pk=True, default=uuid.uuid4)
  name = fields.CharField(max_length=50, unique=True)
  description = fields.TextField()
  
  users: fields.ReverseRelation["UserAndCompany"]

  class Meta:
    table = "companies"