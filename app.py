from flask import Flask,render_template, flash, redirect,request
import time
app = Flask(__name__)
app.secret_key = "super secret key"

sat=0
sun=0
either=0

@app.route("/")
def index():
	start = time.time()
	local_time = time.ctime(start)
	dateperiod= local_time
	return render_template('index.html',dateperiod=dateperiod)

@app.route("/vote",methods=['POST'])
def vote():
	global sat
	global sun
	global either
	button = request.form["button"]
	flash('Thanks for voting.')
	if button=='sat':
		sat=sat+1
	elif button=='sun':
		sun=sun+1
	elif button=='either':
		either=either+1
	return render_template('results.html',sat=sat,sun=sun,either=either)

@app.route("/results",methods=['POST'])
def results():
	flash('Results time.')
	return render_template('results.html',sat=sat,sun=sun,either=either)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)