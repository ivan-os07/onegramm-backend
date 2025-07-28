import uuid
import bcrypt

from sqlalchemy.orm import mapped_column, Mapped

from db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]

    @property
    def password(self):
        raise AttributeError("Password is not readable")

    @password.setter
    def password(self, password: str):
        """Хэширует пароль и сохраняет его в password_hash."""
        self._password_hash = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, password: str) -> bool:
        """Проверяет, соответствует ли введенный пароль хэшу."""
        return bcrypt.checkpw(
            password.encode("utf-8"), self.password_hash.encode("utf-8")
        )
