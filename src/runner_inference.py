"""
This module provides functionality for running
inference on a trained ML model.

This script initializes the ModelInferenceService, loads the model,
and predicts the rent for a given set of features.
"""

from loguru import logger

from model.model_inference import ModelInferenceService


@logger.catch
def main():
    """
    Run the application.

    Initialize the ModelInferenceService, load the ML model,
    and log the predicted rent for a given set of features.
    """
    ml_svc = ModelInferenceService()
    ml_svc.load_model()
    feature_list = {
        'area': 100,
        'rooms': 3,
        'bedrooms': 2,
        'bathrooms': 1,
        'garden': 0,
        'balcony_yes': 1,
        'storage_yes': 1,
        'parking_yes': 1,
        'furnished_yes': 1,
        'garage_yes': 1,
    }
    pred = ml_svc.predict(list(feature_list.values()))
    logger.info(f'Predicted rent: {pred[0]}')


if __name__ == '__main__':
    main()
