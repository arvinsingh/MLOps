"""
This module provides functionality for making
predictions using a ML model.

It contains the ModelInferenceService class that offers
methods to load a model and make predictions.
"""

from pathlib import Path
import pickle as pkl

from loguru import logger

from config import model_settings


class ModelInferenceService:
    """
    The service class for making predictions using a ML model.

    The class provides functionalities to load a model and make
    predictions using the model.

    Attributes:
        model (object): The ML model object.
        model_path (str): Path to the model directory.
        model_name (str): Name of the model file.

    Methods:
        __init__: Initializes the ModelInferenceService.
        load_model: Loads the model from a specified path.
        predict: Makes predictions using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelInferenceService."""
        self.model = None
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def load_model(self) -> None:
        """
        Load the model from a specified path

        Raises:
            FileNotFoundError: If the model file does not exist.
        """
        logger.info(
            f'Checking for existing model file at '
            f'{self.model_path}/{self.model_name}',
        )
        model_path = Path(
            f'{self.model_path}/{self.model_name}',
        )

        if not model_path.exists():
            raise FileNotFoundError(
                f'Model file {self.model_name} does not exist!',
            )

        logger.info(f'Loading existing model -> {model_path}')
        with open(model_path, 'rb') as model_file:
            self.model = pkl.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """Make predictions using the loaded model."""
        logger.info('Making predictions')
        return self.model.predict([input_parameters])
