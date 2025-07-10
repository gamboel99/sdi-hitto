import pandas as pd

def read_data(path):
    return pd.read_csv(path)

def write_data(df, path):
    df.to_csv(path, index=False)

def authenticate(user):
    return True