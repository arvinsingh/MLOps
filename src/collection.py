import pandas as pd
from config import settings
from loguru import logger

from config import engine
from db_model import RentApartments
from sqlalchemy import select

def load_data(path=settings.data_file_name):
    logger.info(f"Loading csv data from {path}")
    return pd.read_csv(path)

def load_data_from_db():
    logger.info("Extracting data from database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)
