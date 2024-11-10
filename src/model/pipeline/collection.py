"""
This module is responsible for extracting data from the database.

It uses a function to extract data from the RentApartments table in
the database and load it into a pandas DataFrame.
It uses SqlAlchemy to retrieve data from the database for further
analysis or processing.
"""

from loguru import logger
import pandas as pd
from sqlalchemy import select

from config import engine
from db.db_model import RentApartments


def load_data_from_db() -> pd.DataFrame:
    """
    Load data from the RentApartments table in the database.

    Returns:
        pd.DataFrame: DataFrame containing the RentApartments data
    """
    logger.info("Extracting data from database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)
