from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys

sys.path.append('/opt/airflow/scripts')

from extract import extract , cities
from transform import transform
from load import load_insert_uniques , engine

def run_pipeline():

    city = "CDMX"
    lat, lon = cities[city]
    raw_data = extract(latitud=lat, longitud=lon)
    df = transform(raw_data, city=city)
    load_insert_uniques(df=df, table_name='weather', engine=engine)

default_args = {
    'owner':'Josue',
    'retries':2
}

with DAG(
    dag_id = 'weather_pipeline_simple',
    description = 'Pipeline de clima , extract , transform  y load en una sola tarea',
    default_args= default_args,
    start_date = datetime(2026,7 , 1),
    schedule = '@daily',
    catchup = False,
) as dag:

    task_run_pipeline = PythonOperator(
        task_id = 'run_full_pipeline',
        python_callable= run_pipeline,
    )
