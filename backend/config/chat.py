from pydantic import BaseSettings


class Settings(BaseSettings):
    OPENAI_KEY = ""
    OPENAI_BASE_URL = ""

    class Config:
        env_prefix = 'CHAT_'
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
