from loguru import logger

from model.model_service import ModelService


@logger.catch
def main():
    ml_svc = ModelService()
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
