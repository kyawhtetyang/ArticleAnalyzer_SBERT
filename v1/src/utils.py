import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    """Load CSV dataset into pandas DataFrame."""
    return pd.read_csv(path)

def add_clean_column(df: pd.DataFrame, text_col: str, cleaner) -> pd.DataFrame:
    """Add a clean text column using the provided cleaning function."""
    df['clean_content'] = df[text_col].apply(cleaner)
    return df

