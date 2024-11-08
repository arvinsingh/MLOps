from pathlib import Path
import pickle as pkl

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelService:

    def __init__(self):
        self.model = None

    def load_model(self):
        logger.info(
            f'Loading model from '
            f'{model_settings.model_path}/{model_settings.model_name}',
        )
        model_path = Path(
            f'{model_settings.model_path}/{model_settings.model_name}',
        )

        if not model_path.exists():
            logger.warning(
                f'Model not found at {model_path} '
                f'-> Building model {model_settings.model_name}',
            )
            build_model()

        logger.info(f'Loading model from {model_path}')
        self.model = pkl.load(open(model_path, 'rb'))

    def predict(self, input_parameters):
        logger.info('Making predictions')
        return self.model.predict([input_parameters])
