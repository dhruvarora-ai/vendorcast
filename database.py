import sqlite3
import pandas as pd

DB_NAME = "sales.db"

def save_to_db(df, table_name="monthly_data"):
    conn = sqlite3.connect(DB_NAME)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def load_from_db(table_name="monthly_data"):
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df