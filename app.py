# Module always have lowercase

from flask import Flask  # Here we are importing the class Flask from the flask package

# Here we are importing functionalities of flask and insert it into the "app" variable
app = Flask(__name__)  # Creating flask application with a name
'''
Within any Python script we have a variable named, "__name__". It indicates how a script was invoked.


When we run the file using the "python" command than we will get "__name__" as "__main__" 

print(__name__) 
--> O/P: __main__
'''
'''
After creating an appication we add routes to it. We will tell the python when a url is requested.

In a URL the part after the domain name is called as "route" or "path name".
Ex: If URL--> www.abc.com/learn
Here, "/learn" part is called route
'''

# Registering route
'''
Here '@' called decorators which is used for special functionalities.
'''


@app.route("/")
def hello_world():
  return "Hello Sabya"


'''
By using the decorater above, we have informed flask that when the url with "/" route is accessed than show "Hello World"
'''

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  # To run the app locally we will
