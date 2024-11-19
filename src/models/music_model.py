"""Classes e funções referentes ao banco de dados"""

from datetime import datetime
from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func

table_registry = registry()


@table_registry.mapped_as_dataclass
class Music:
    "Classe Music no banco de dados"
    __tablename__ = "music"

    id: Mapped[int]                 = mapped_column(init=False, primary_key=True)
    created_at: Mapped[datetime]    = mapped_column(init=False, server_default=func.now())
    name: Mapped[str]               = mapped_column(unique=True)
    description: Mapped[str]        = mapped_column(nullable=True, default=None)
    type: Mapped[str]               = mapped_column(nullable=True, default=None)
