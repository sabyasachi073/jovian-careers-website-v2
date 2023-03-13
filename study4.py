from flask import Flask, render_template, jsonify
from database import load_jobs_from_db  # Since, we have created a database.py file so we can use it as a module and import it

app = Flask(__name__)

jobs = load_jobs_from_db()


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=jobs, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
'''
After we have created our database in Planet Scale, wwe will try to connect to the database using "MySQL Workbench". "MySQL Workbench" is a downloadable tool that we can download on our computer to connect to the database that we created in the Planet Scale.
'''
