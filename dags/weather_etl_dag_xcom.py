from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sys

import json

sys.path.append('/opt/airflow/scripts')

from extract import extract, cities
from transform import transform
from load import load_insert_uniques, engine

def task_extract_fn(**kwargs):
    city = "CDMX"
    lat, lon = cities[city]
    raw_data = extract(latitud=lat, longitud=lon)  

    ruta = "/tmp/weather_raw.json"
    with open(ruta, "w") as f:
        json.dump(raw_data, f)

    return ruta 

def task_transform_fn(**kwargs):
    ti = kwargs['ti']
    ruta_raw = ti.xcom_pull(task_ids='extract_weather') 

    with open(ruta_raw, "r") as f:
        raw_data = json.load(f)  

    df = transform(raw_data, city="CDMX")   

    ruta_clean = "/tmp/weather_clean.csv"
    df.to_csv(ruta_clean, index=False)   

    return ruta_clean

def task_load_fn(**kwargs):
    ti = kwargs['ti']
    ruta_clean = ti.xcom_pull(task_ids='transform_weather')

    df = pd.read_csv(ruta_clean)

    load_insert_uniques(df=df, table_name='weather', engine=engine) 

default_args = {
    'owner': 'Josue',
    'retries': 2
}


with DAG (
    dag_id = 'weather_pipeline_xcom',
    description = 'Pipeline de weather con Xcom , 3 tareas separadas',
    default_args = default_args,
    start_date = datetime(2026,7,1),
    schedule = '@daily',
    catchup = False,
) as dag:

    task_extract = PythonOperator(
        task_id = 'extract_weather',
        python_callable = task_extract_fn
    )

    task_transform = PythonOperator(
        task_id = 'transform_weather',
        python_callable = task_transform_fn
    )

    task_load = PythonOperator(
        task_id = 'load_weather',
        python_callable = task_load_fn
    )

task_extract >> task_transform >> task_load
