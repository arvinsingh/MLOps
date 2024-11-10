"""
The module is used for preprocessing the data before it is used for
training the model.

It consists of functions to load data from a database, encode categorical
columns, and parse specific columns for further processing.
"""

import re

import pandas as pd
from loguru import logger

from model.pipeline.collection import load_data_from_db


def prepare_data() -> pd.DataFrame:
    """
    Prepare the dataset for analysis and modelling. This involves loading
    the data, encoding categorical columns, and parsing the 'garden' column.

    Returns:
        pd.DataFrame: The processed dataset.
    """
    logger.info('Preporcessing data pipeline started')
    data = load_data_from_db()
    data_encoded = encode_cat_cols(data)
    df = parse_garden_col(data_encoded)
    return df


def encode_cat_cols(data: pd.DataFrame) -> pd.DataFrame:
    """
    Encode specific categorical columns into dummy variables.

    Args:
        data (pd.DataFrame): The original dataset.

    Returns:
        pd.DataFrame: Dataset with categorical columns encoded.
    """
    cols = ['balcony', 'storage', 'parking', 'furnished', 'garage']
    logger.info('Encoding categorical columns: {cols}')
    return pd.get_dummies(data,
                          columns=cols,
                          drop_first=True,
                          dtype=int)


def parse_garden_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Parse the 'garden' column in the dataset. If the garden data is not
    prsent, it is replaced with 0, otherwise extract the number from the
    string.

    Args:
        dataframe (pd.DataFrame): The dataset with a 'garden' column.

    Returns:
        pd.DataFrame: The dataset with the 'garden' column parsed.
    """
    logger.info('Parsing garden column')
    dataframe['garden'] = dataframe['garden'].apply(
        lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0]),
    )
    return dataframe
