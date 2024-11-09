from loguru import logger

from model.model_builder import ModelBuilderService


@logger.catch
def main():
    logger.info('Running builder application')
    ml_svc = ModelBuilderService()
    ml_svc.train_model()


if __name__ == '__main__':
    main()
