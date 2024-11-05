from pathlib import Path
import pickle as pkl
from model import build_model
from config import settings

class ModelService:

    def __init__(self):
        self.model = None
    
    def load_model(self):
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            build_model()
        
        self.model = pkl.load(open(model_path, 'rb'))

    def predict(self, input_parameters):
        return self.model.predict(input_parameters)
    