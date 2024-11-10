"""
The module is responsible for building the model.

The model is built using the `build_model` function
from the `model` module.
"""

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelBuilderService:
    """
    The service class for building the model.

    The class provides functionalities to train
    the model and save it to a specified path.

    Attributes:
        model_path (str): Path to the model directory.
        model_name (str): Name of the model file.

    Methods:
        __init__: Initializes the ModelBuilderService.
        train_model: Trains the model and saves it to a
        specified directory.
    """

    def __init__(self) -> None:
        """Initialize the ModelBuilderService."""
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def train_model(self) -> None:
        """
        Train the model from a specified path and
        save to the model's directory.
        """
        logger.info(
            f'Building the model file at '
            f'{self.model_path}/{self.model_name}',
        )
        build_model()
