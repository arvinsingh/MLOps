import pandas as pd
import re
from collection import load_data

def prepare_data():
    
    data = load_data()
    data_encoded = enode_cat_cols(data)
    df = parse_garden_col(data_encoded)

    return df


def enode_cat_cols(data):

    return pd.get_dummies(data,
                          columns=['balcony',
                                   'storage',
                                   'parking',
                                   'furnished',
                                   'garage'],
                          drop_first=True,
                          dtype=int)

def parse_garden_col(data):
    for i in range(len(data)):
        if data.garden[i] == "Not present":
            data.garden[i] = 0
        else:
            data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])
        
    return data