import pandas as pd
import re
from collection import load_data
from loguru import logger
def prepare_data():
    logger.info("Preporcessing data pipeline started")
    data = load_data()
    data_encoded = enode_cat_cols(data)
    df = parse_garden_col(data_encoded)

    return df


def enode_cat_cols(data):
    cols = ['balcony', 'storage', 'parking', 'furnished', 'garage']
    logger.info("Encoding categorical columns: {cols}")
    return pd.get_dummies(data,
                          columns=cols,
                          drop_first=True,
                          dtype=int)

def parse_garden_col(data):
    logger.info("Parsing garden column")
    for i in range(len(data)):
        if data.garden[i] == "Not present":
            data.garden[i] = 0
        else:
            data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])
        
    return data