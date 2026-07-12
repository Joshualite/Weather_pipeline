from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import pandas as pd
from transform import transform
from extract import extract

LATITUDE = 19.43
LONGITUDE = -99.13

load_dotenv()
user =  os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')

db_conexion = f'postgresql+psycopg://{user}:{password}@localhost:5432/{db}'


engine = create_engine(db_conexion)



def load(df: pd.DataFrame, table_name: str, engine) -> None:
    df.to_sql(table_name, con= engine , if_exists= 'append' , index=False)

if __name__ == '__main__':
    

    raw_data = extract(latitud=LATITUDE,longitud=LONGITUDE)
    weather_df = transform(raw_data)
    print(weather_df.head())
    load(df=weather_df , table_name= 'WEATHER', engine= engine)



