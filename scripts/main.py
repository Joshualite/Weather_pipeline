from transform import transform
from extract import extract , cities
from load import load


if __name__ == '__main__':
    city = "CDMX"
    lat , long = cities[city]
    raw_data = extract(latitud=lat,longitud=long)
    df = transform(raw_data, city= city)
    print(df.head())
    load(df=df , table_name= 'WEATHER')
