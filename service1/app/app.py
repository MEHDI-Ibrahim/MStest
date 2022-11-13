# importing Flask and other modules
from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os
# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/register', methods =["GET", "POST"])
def register():
	if request.method == "POST":
		IdNum = request.form.get("IdNum")
		NomPrenom = "Ibrahim MEHDI"
		Profession = requests.get('http://localhost:5052').json()
		flash(str(NomPrenom, Profession), "green")
		return redirect(url_for('register'))
	else:
		pass
	return render_template('result.html')


if __name__=='__main__':
	app.run(debug=True, host = '0.0.0.0' , port=5050)
