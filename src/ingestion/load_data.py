import pandas as pd
from src.config import load_config

def load_dataset():

    config = load_config()

    data_path = config["data"]["raw_data_path"]

    df = pd.read_csv(data_path)

    return df