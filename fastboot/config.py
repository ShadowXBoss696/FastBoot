from pydantic_settings import BaseSettings


class Config(BaseSettings):
    port: int = 8080
