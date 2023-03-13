# Connecting to database and use it to extract some data using SQLAlchemy
'''
Command to install SQLAlchemy >> pip install sqlalchemy
'''
# import sqlalchemy
# print(sqlalchemy.__version__) # To check version of sqlalchemy

from sqlalchemy import create_engine, text
import os
'''
"db_connection_string" contains all the sensitive information like username, password, etc. which can be used to connect to the database. So, since we are uploading everything into Github in public repository directly than everyone will get the credentials of our database and they can do anything they want with our database. Hence, we should make it a secret.
In Replit we can hide anything sensitive data using 'Secrets' which will be accessible only to the owner of the Replit account.

To access the secret we need to use the "os" module of python.
'''

db_connection_string = os.environ['DB_CONNECTION_STRING']

# Creating an engine
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
'''
SQLAlchemy internally depending t=on which kind of database we want to connect to requires some libraries which can serve as a connector. SQLAlchemy can connect to many databases so it by default don't come with all the built-in connectors, so we need to separately install a connector based on which kind of database we are using.

Here, since we are using mysql with "pymysql" as connector so we need to download the connector "pymysql"
Command>> pip install pymysql
'''

#  We need to connect to the engine we created and than we can use the connection to execute the commands in that database

# Connecting to engine
with engine.connect() as conn:
  result = conn.execute(text(
    "select * from jobs"))  # It returns all the rows present in the database
  print("type(result):", type(result))
  result_all = result.all()
  print("type(result_all): ", type(result_all))
  # Print all the rows present in the database
  print("result.all(): ", result_all)
  first_result = result_all[0]
  print("type(first_result):", type(first_result))
  # Converting the row of the table to dictionary type
  first_result_dict = dict(result_all[0]._mapping)
  print("type(first_result_dict): ", type(first_result_dict))
  print(first_result_dict)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))

    return jobs
