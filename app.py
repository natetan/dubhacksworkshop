from flask import Flask
from flask import render_template
from flask import request
import unirest

app = Flask(__name__)
#Put code below here

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/yoda')
def yoda():
	# These code snippets use an open-source library. http://unirest.io/python
	sentence = request.args.get("text")

	response = unirest.get("https://yoda.p.mashape.com/yoda?sentence=" + sentence,
	  	headers={
	    	"X-Mashape-Key": 
	    	"TOKPt5V7Whmsh6TeuEKGV5v9nQo7p1m7NfTjsn9PhM41rDqUaM",
	    	"Accept": "text/plain"
	 	}
	)
	return response.body

@app.route('/about')
def about():
	return "This is the about page"

# Put code above here
if __name__ == '__main__':
    app.run(debug=True)