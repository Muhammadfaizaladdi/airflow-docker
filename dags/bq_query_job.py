import os
from airflow import models
import logging
from airflow.models import Variable
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from query_update_manual_dag.sql import query_update_manual_sql
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

DAG_ID = 'bq_query_example_dag'

configs = Variable.get(DAG_ID, deserialize_json=True)

default_args = {
    'owner': 'Angga',
    'depends_on_past': False,
    'start_date': configs['start_date'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    DAG_ID,
    default_args=default_args,
    max_active_runs=1,
    description='Query Daily Update Example',
    tags=['bigquery'],
    schedule_interval=configs['interval'])

migrations = configs.get('migrations', [])
sql_query = query_update_manual_sql.SQL_QUERY

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = configs["service_account"]
PROJECT_ID = os.environ.get("GCP_PROJECT_ID", configs["project_id"])


start = DummyOperator(
    task_id='start',
    dag=dag)

completed = DummyOperator(
    task_id='completed',
    dag=dag)

for migration in migrations:
    DATASET_NAME = os.environ.get("GCP_BIGQUERY_DATASET_NAME", migration["dataset_name"])
    insert_query_job = BigQueryInsertJobOperator(
            task_id="insert_query_job_" + migration["query"],
            configuration={
                "query": {
                    "query": sql_query[migration["query"]],
                    "useLegacySql": False,
                }
            },
            dag=dag,
            gcp_conn_id=configs['gcp_conn_id']
        )    


    start >> insert_query_job >> completed