from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import pandas as pd
from transform import transform
from extract import extract , cities








def load(df: pd.DataFrame, table_name: str) -> None:
    load_dotenv()
    user =  os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    db = os.getenv('POSTGRES_DB')

    db_conexion = f'postgresql+psycopg://{user}:{password}@localhost:5432/{db}'

    engine = create_engine(db_conexion)
    with engine.begin() as connection:
         df.to_sql(table_name, con= connection , if_exists= 'append' , index=False)

    print('exito con la carga')


   





