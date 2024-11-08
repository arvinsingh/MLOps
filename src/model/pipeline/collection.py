from loguru import logger
import pandas as pd
from sqlalchemy import select

from config import engine
from db.db_model import RentApartments


def load_data_from_db():
    logger.info("Extracting data from database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)
