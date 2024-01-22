import sqlalchemy
from sqlalchemy import create_engine,text
import os

db_connection_string= os.environ['DB_CONNECTION_STRING']

engine=create_engine(
  db_connection_string,
  connect_args={
    "ssl":{
      "ssl_ca":"/etc/ssl/cert.pem"
    }
  }
)
                     
with engine.connect() as conn:
  result=conn.execute(text('select * from jobs'))
  print(result.all())

  result_dicts=[]
  for row in result.all():
    result_dicts.append(dict(row))
  print(result_dicts)

def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text('select * from jobs'))
    jobs=[]
    for row in result.all():
      jobs.append(dict(row))
    return jobs