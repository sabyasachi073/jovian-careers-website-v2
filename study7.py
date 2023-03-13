from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)

  if not job:
    return "Not Found", 404

  return render_template("jobpage.html", job=job)


@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_db(id)
  return jsonify(job)


'''
@app.route("/job/<id>/apply")
def applt_to_job(id):
  # In the url what ever is present after '?' that can be accessed using "request" variable in flask
  data = request.args 
  
  # The data that we received can be used to ->
  #   > Store in the database
  #   > Send an email
  #   > Display an acknowledgement
  
  return jsonify(data)
'''
'''
When a route used the method "post" than the route "/job/<id>/apply" expects data to be posted by the browser and not sent in the url. When the method is 'post' than nothing is captured in "request.args", as "request.args" captures the data from URL. The information submitted in the form is captured in the "request.form".

When we send by post than nothing is present in URL shown in the URL but the information is posted.
'''


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)

  add_application_to_db(
    id, data)  # It stores the application data into the database

  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
