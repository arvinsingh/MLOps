"""
This module is responsible for configuring the logger.

Pydantic is used to load the log level from the environment variables.
The logger is configured using the loguru library.
"""

from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    """
    Logger configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        log_level (str): Log level for the logger.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_encoding='utf-8',
        extra='ignore',
    )
    log_level: str


def configure_logging(level: str) -> None:
    """
    Configures the logger with the specified log level.
    """
    logger.remove()
    logger.add(
        'logs/app.log',
        rotation='1 day',
        retention='7 days',
        compression='zip',
        level=level,
    )


configure_logging(LoggerSettings().log_level)
