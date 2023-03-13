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


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))

    return jobs


'''
Here, in the function 'load_job_from_db(id)' the function is getting its variable "id" from the URL where we have route as "/job/id".

Now, in the statement:-
result = conn.execute(text("select * from jobs where id = :val"), val = id)

, we are inserting the value of "val" from the parameter "id" that is available. In the query we are mentioning the variable 'val' in a special way and this is a special way of doing string formatting in sqlalchemy. The value of ':val' will be replaced with the value of 'id' coming from the parameter which is actually coming from the route .
'''
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from jobs where id = :val"), {"val": id})
    
    rows = result.all()

    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._mapping)