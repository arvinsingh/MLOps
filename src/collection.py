import pandas as pd
from config import settings
from loguru import logger

def load_data(path=settings.data_file_name):
    logger.info(f"Loading csv data from {path}")
    return pd.read_csv(path)
