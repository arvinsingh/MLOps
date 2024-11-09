from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelBuilderService:

    def __init__(self):
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def load_model(self):
        logger.info(
            f'Building the model file at '
            f'{self.model_path}/{self.model_name}',
        )
        build_model()
