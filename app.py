from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def register():
	name = request.form.get("name")
	dorm = request.form.get("household")
	income = request.form.get("income")
	if not name or not dorm or not income:
		return render_template("failure.html")
	return render_template("success.html")