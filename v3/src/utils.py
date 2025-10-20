import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def add_clean_column(df: pd.DataFrame, text_col: str, cleaner) -> pd.DataFrame:
    df['clean_content'] = df[text_col].apply(cleaner)
    return df

