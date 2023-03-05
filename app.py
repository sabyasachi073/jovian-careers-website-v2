from flask import Flask, render_template
# To use the template we use the render_template function from flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
'''
In flask we can access any file stored in static folder by giving the path-> /static/filename

Anything that we put inside the static folder is called an asset
'''
