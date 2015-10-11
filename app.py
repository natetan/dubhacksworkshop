from flask import Flask
from flask import render_template
from flask import request
import unirest

app = Flask(__name__)
#Put code below here

@app.route('/')
def home():
	return render_template("home.html")

@app.route("/about")
def about():
	return "This is the about page"

# Put code above here
if __name__ == '__main__':
    app.run(debug=True)