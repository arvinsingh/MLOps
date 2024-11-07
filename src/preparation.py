import pandas as pd
import re
from collection import load_data_from_db
from loguru import logger


def prepare_data():
    logger.info("Preporcessing data pipeline started")
    data = load_data_from_db()
    data_encoded = encode_cat_cols(data)
    df = parse_garden_col(data_encoded)

    return df


def encode_cat_cols(data):
    cols = ['balcony', 'storage', 'parking', 'furnished', 'garage']
    logger.info("Encoding categorical columns: {cols}")
    
    return pd.get_dummies(data,
                          columns=cols,
                          drop_first=True,
                          dtype=int)

def parse_garden_col(data):
    logger.info("Parsing garden column")
    for i in range(len(data)):
        if data.loc[i, "garden"] == "Not present":
            data.loc[i, "garden"] = 0
        else:
            data.loc[i, "garden"] = int(re.findall(r'\d+', data.loc[i, "garden"])[0])
        
    return data