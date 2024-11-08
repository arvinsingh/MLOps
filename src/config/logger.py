from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_encoding='utf-8',
        extra='ignore',
    )
    log_level: str


def configure_logging(level: str):
    logger.remove()
    logger.add(
        'logs/app.log',
        rotation='1 day',
        retention='7 days',
        compression='zip',
        level=level,
    )


configure_logging(LoggerSettings().log_level)
