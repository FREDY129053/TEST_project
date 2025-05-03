from app.src.enums.role import UserRole

from tortoise import fields
from tortoise.models import Model


class UserAndCompany(Model):
  id = fields.IntField(pk=True)
  user = fields.ForeignKeyField("models.User", related_name="company", to_field="id", on_delete=fields.CASCADE)
  company = fields.ForeignKeyField("models.Company", related_name="user", to_field="id", on_delete=fields.CASCADE)
  role = fields.CharEnumField(UserRole, default=UserRole.member)

  class Meta:
    table = "user_company"