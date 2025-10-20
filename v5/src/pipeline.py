from src.nlp_utils import load_dataset, add_clean_column, enrich_articles, init_db, save_to_db
import sqlite3

def full_pipeline(config: dict):
    df = load_dataset(config["dataset_path"])
    df = add_clean_column(df, config.get("text_col","content"))
    df, sim_matrix = enrich_articles(df, config)

    conn = init_db(config.get("database_path","data/news_v5.db"))
    save_to_db(conn, df)
    conn.close()

    return df, sim_matrix

