"""
This module contains the model configuration settings for the application.

This module uses Pydantic's BaseSettings to manage configuration,
allowing settings to be read from environment variables and a .env file.
"""

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    Model configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        model_path (DirectoryPath): Path to the model directory.
        model_name (str): Name of the model file.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_encoding='utf-8',
        extra='ignore',
    )

    model_path: DirectoryPath
    model_name: str


model_settings = ModelSettings()
