from pathlib import Path
import pickle as pkl

from loguru import logger

from config import model_settings


class ModelInferenceService:

    def __init__(self):
        self.model = None
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def load_model(self):
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

    def predict(self, input_parameters):
        logger.info('Making predictions')
        return self.model.predict([input_parameters])
