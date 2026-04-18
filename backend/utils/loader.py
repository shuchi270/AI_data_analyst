import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def get_schema(df):
    return {
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "sample": df.head(5).to_dict()
    }