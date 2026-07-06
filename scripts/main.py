from transform import transform
from extract import extract

LATITUDE = 19.43
LONGITUDE = -99.13

if __name__ == '__main__':
    raw_data = extract(latitud=LATITUDE,longitud=LONGITUDE)
    df = transform(raw_data)
    print(df.head())
