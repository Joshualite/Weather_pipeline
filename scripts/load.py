from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
import pandas as pd
from transform import transform
from extract import extract , cities


load_dotenv()
user =  os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')

db_conexion = f'postgresql+psycopg://{user}:{password}@localhost:5432/{db}'

engine = create_engine(db_conexion)


def load_to_sql(df: pd.DataFrame, table_name: str, engine) -> None:
   
    with engine.begin() as connection:
         df.to_sql(table_name, con= connection , if_exists= 'append' , index=False)


def load_insert_uniques(df: pd.DataFrame, table_name: str, engine) -> None:
    records = df.to_dict(orient='records')
    with engine.begin() as connection:
        connection.execute(
            text(f"""
                INSERT INTO {table_name} (time, temperature_2m, latitude, longitude, city)
                VALUES ( :time, :temperature_2m, :latitude, :longitude, :city)
                ON CONFLICT (time, latitude, longitude) DO NOTHING;
            """),
            records
        )
          
          




   





