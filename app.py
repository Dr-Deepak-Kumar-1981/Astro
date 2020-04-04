from flask import Flask, render_template
import requests
app=Flask(__name__)

@app.route("/")
def index():
	url='http://api.open-notify.org/astros.json'
	p=requests.get(url).json()
	a=p['people']
	c=p['number']
	
	new1=[]
	for k in a:
		new1.append(k['name'])

	return render_template("index.html",new1=new1, c=c)

if __name__ == "__main__":
	app.run(debug = True)