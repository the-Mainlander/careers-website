import sqlalchemy
from sqlalchemy import create_engine,text

db_connection_string="mysql+pymysql://jwddjrwg4s1kf7syx4nr:pscale_pw_jXwdLywqKqrutMJcbzBpb6S5BxkCH4WM8pQLxrDIYC@aws.connect.psdb.cloud/deuscareers?charset=utf8mb4"

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
