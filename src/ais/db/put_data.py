import sqlite3
import polars as pl
from pathlib import Path
from ais.db.config import DB_PATH

def create_db(db_file: str = DB_PATH):
    sqlite3.connect(DB_PATH)


def ingest(chunk_size: int = 10000):
    # create_db()
    data = (
        pl
        .scan_csv('data/AIS_2020_03_21.csv', infer_schema_length=5000)
        .collect_batches(chunk_size=chunk_size)
    )

    for u in data:
        print(u)
        break
    

if __name__ == "__main__":
    ingest()