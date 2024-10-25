from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, cast
from typing_extensions import Self

from bcrypt import checkpw, gensalt, hashpw

from src.domain.entities.user import UserEntity
from src.infrastructure.repository.base import BaseUserRepository
from src.service_layer.exceptions.login import LogInException


@dataclass
class BaseUserAuthorizationService(ABC):
    default_encoding: ClassVar[str] = "utf-8"
    invalid_credentials_message: ClassVar[str] = (
        "Неверное имя пользователя или пароль."
    )

    repository: BaseUserRepository

    _user: UserEntity = field(init=False)

    @property
    def user(self: Self) -> UserEntity:
        return self._user

    @staticmethod
    def _hash_password(pwd_bytes: bytes, decode_from: str = default_encoding) -> str:
        return hashpw(pwd_bytes, gensalt()).decode(decode_from)

    @staticmethod
    def _compare_passwords(password: bytes, hashed_password: bytes) -> bool:
        return checkpw(password=password, hashed_password=hashed_password)

    def _validate_credentials(self: Self, username: str, password: str) -> None:
        self._validate_user(username)
        self._validate_user_password(password)

    def _get_user(self: Self, username: str) -> UserEntity | None:
        return self.repository.get_by_username(username)

    def _validate_user(self: Self, username: str) -> None:
        user: UserEntity | None = self._get_user(username)

        if user is None:
            raise LogInException(self.invalid_credentials_message)

        self._user = user
        cast(UserEntity, self._user)

    def _validate_user_password(self: Self, password: str) -> None:
        if not self._compare_passwords(
            password=password.encode(self.default_encoding),
            hashed_password=self._user.password,
        ):
            raise LogInException(self.invalid_credentials_message)

    @abstractmethod
    def login(self: Self, username: str, password: str) -> UserEntity:
        raise NotImplementedError
