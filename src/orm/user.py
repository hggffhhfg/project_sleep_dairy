from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.orm.base import BaseORM
from src.orm.mixins import MetaInfo


class UserORM(MetaInfo, BaseORM):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[bytes]
