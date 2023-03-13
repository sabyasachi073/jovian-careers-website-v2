from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

jobs = load_jobs_from_db()


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)
  
'''
Here we are getting the "id" of the job from the URL. If anything with route as "/jobs/<id>" is searched than the variable "id" will store the content after "/jobs/". 
Example: If the route is "jobs/3" than the variable "id" will be equal to 3.
'''
@app.route("/job/<id>") 
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    # Sending the Error message with the error code or status
    return "Not Found", 404 
    
  return render_template("jobpage.html", job = job);

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)