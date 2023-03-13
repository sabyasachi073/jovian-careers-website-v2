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
