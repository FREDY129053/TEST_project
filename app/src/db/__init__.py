from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:1234@db_test:5432/test"},
    "apps": {
        "models": {
            "models": ["app.src.db.models"],
            "default_connection": "default",
        }
    },
    "logging": True,
}


async def init_db_tortoise(_app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    # Для автоматической генерации описанных схем
    # await Tortoise.generate_schemas()
    register_tortoise(
      app=_app,
      config=TORTOISE_ORM,
    )
