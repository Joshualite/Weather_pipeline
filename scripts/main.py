from transform import transform
from extract import extract , cities
from load import load_insert_uniques
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os


if __name__ == '__main__':
    city = "CDMX"
    lat , long = cities[city]
    raw_data = extract(latitud=lat,longitud=long)
    df = transform(raw_data, city= city)
    print(df.head())

    load_dotenv()
    user =  os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    db = os.getenv('POSTGRES_DB')

    db_conexion = f'postgresql+psycopg://{user}:{password}@localhost:5432/{db}'

    engine = create_engine(db_conexion)
    load_insert_uniques(df=df , table_name= 'weather', engine=engine)
