from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, FilePath
from sqlalchemy import create_engine

from loguru import logger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_encoding='utf-8')

    data_file_name: FilePath
    model_path: DirectoryPath
    model_name: str
    log_level: str
    db_conn_str: str
    rent_apart_table_name: str

settings = Settings()

logger.remove()
logger.add("app.log", rotation="1 day", retention="7 days", compression="zip", level=settings.log_level)

engine = create_engine(settings.db_conn_str)