import pandas as pd

def load_data(path='rent_appartments.csv'):
    return pd.read_csv(path)
