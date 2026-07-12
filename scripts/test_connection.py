import psycopg
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')

print(f"Usuario leído: '{user}'")
print(f"Password leído: '{password}'")
print(f"DB leída: '{db}'")

conn = psycopg.connect(
    host='localhost',
    port=5432,
    user=user,
    password=password,
    dbname=db
)
print("¡Conexión exitosa!")
conn.close()