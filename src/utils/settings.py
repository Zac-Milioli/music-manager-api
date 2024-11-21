"Classe e funções para aplicação geral de bancos por .env"

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    "Classe para integração do banco em .env"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")
    DATABASE: str
