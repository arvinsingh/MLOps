from model_service import ModelService
from loguru import logger

@logger.catch
def main():
    ml_svc = ModelService()
    ml_svc.load_model()
    pred = ml_svc.predict([[100, 3, 2, 2, 1, 1, 1, 1, 1, 1]])
    logger.info(f'Predicted rent: {pred[0]}')

if __name__ == '__main__':
    main()