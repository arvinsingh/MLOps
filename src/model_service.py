from pathlib import Path
import pickle as pkl
from model import build_model
from config import settings
from loguru import logger

class ModelService:

    def __init__(self):
        self.model = None
    
    def load_model(self):
        logger.info(f'Loading model from {settings.model_path}/{settings.model_name}')
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.warning(f'Model not found at {model_path} -> Building model {settings.model_name}')
            build_model()
        
        logger.info(f'Loading model from {model_path}')
        self.model = pkl.load(open(model_path, 'rb'))

    def predict(self, input_parameters):
        logger.info(f'Making predictions')
        return self.model.predict(input_parameters)
    