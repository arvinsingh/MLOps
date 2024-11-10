"""
This module provides functionality for training a ML model.

This script initializes the ModelBuilderService, trains and saves the model,
and logs the output. A typical workflow of an ML model builder service.
"""

from loguru import logger

from model.model_builder import ModelBuilderService


@logger.catch
def main():
    """
    Run the application.

    Initialize the ModelBuilderService, train the ML model,
    and log the output.
    """
    logger.info('Running builder application')
    ml_svc = ModelBuilderService()
    ml_svc.train_model()


if __name__ == '__main__':
    main()
