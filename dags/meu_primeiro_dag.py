from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

with DAG(
  'meu_primeiro_dag',
  start_date=days_ago(1),
  schedule_interval='@daily',
) as dag:

   tarefa_1 = EmptyOperator(task_id='tarefa_1')
   tarefa_2 = EmptyOperator(task_id='tarefa_2')
   tarefa_3 = EmptyOperator(task_id='tarefa_3')

   tarefa_4 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p "/home/dimitri/dimitri/airflowalura/pasta={{data_interval_end}}"'
      )

   tarefa_1 >> [tarefa_2, tarefa_3] 
   tarefa_3 >> tarefa_4