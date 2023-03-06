from flask import Flask, render_template, jsonify
# To use the template we use the render_template function from flask
# "jsonify" takes an object and converts it into a json object

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': 'Rs. 12,00,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'salary': '$120,000'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='Jovian')


@app.route("/jobs")  # API route or endpoint
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
'''
In flask we can access any file stored in static folder by giving the path-> /static/filename

Anything that we put inside the static folder is called an asset
'''
'''
When we say REST API or JSON API or API ENDPOINT then it means that our webserver is returning some information but not as HTML but as JSON which is also accessible and we can do anything with that

The difference between creating a HTML endpoint and creating a JSON endpoint is that instead of rendering a template(in HTML endpoint) we are

Note: To differentiate between HTML pages and non HTML pages we put '/api' before the pathname in the route. API don't return any HTML page rather it returns structured data in the form of JSON which than can be programmatically analyzed.

API -> Application PRogramming Interface
'''
'''
In order to deploy our website to "Render" we need to create a "requirements.txt" file.

In Python ecosystem, its a standard that if we have a python project than we need to mention all the libraries and packages that our project needs in the file -> 'requirements.txt'
'''
'''
"Flask" is a development server and we can't use it for production.
"gunicorn" is a production server for Python.
Whenever we want to put any Flask applicaion into production, we need to use "gunicorn" library.
'''
'''
Build command in Render:
command>> pip intstall -r requirements.txt

"-r requirements.txt" instructs pip to install all the libraries which in present in each line of the "requirements.txt" file.

Start command in Render:
command>> gunicorn file_to_be_executed:x
[Here, x is the name of the actua; variable which contains the Flask application that we want to run. Here x is app.
We are talking about this 'app' variable -> "app = Flask(__name__)"]
For this project command>> gunicorn app:app
'''
