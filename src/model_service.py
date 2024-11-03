from pathlib import Path
import pickle as pkl
from model import build_model
class ModelService:

    def __init__(self):
        self.model = None
    
    def load_model(self, model_name='rf_v1'):
        model_path = Path(f'models/{model_name}')

        if not model_path.exists():
            build_model()
        
        self.model = pkl.load(open(model_path, 'rb'))

    def predict(self, input_parameters):
        return self.model.predict(input_parameters)
    