import sqlite3
import os
from flask import Flask, render_template, request, url_for, flash, redirect, send_file
from werkzeug.exceptions import abort 
from werkzeug.utils import secure_filename
import generate
import image

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)

ALLOWED_EXTENSIONS = {"png"}

app.config["SECRET_KEY"] = "verySwag"
app.config["UPLOAD_FOLDER"] = "uploads/"



@app.route("/")
def index():
	return render_template("index.html")


@app.route("/genterrain", methods=("GET", "POST"))
def genTerrain():
	if request.method == "POST":
		try:
			xSize = int(request.form["xSize"])
			ySize = int(request.form["ySize"])
			seed = int(request.form["seed"])
			bias = float(request.form["bias"])
			smoothing = int(request.form["smoothing"])
			normals = bool(request.form["normal"])

			image.prodImg(xSize, ySize, "generated/image.png", seed, smoothing, bias, 25)
			generate.runGen(xSize, ySize, "generated/terrain.obj", "generated/image.png", normals)

			#Download file
			return send_file("generated/terrain.obj", as_attachment=True)
		except:
			flash("Wrong data types!")
			return render_template("genHeightmap.html")
	return render_template("genTerrain.html")

@app.route("/genheightmap", methods=("GET", "POST"))
def genHeightmap():
	if request.method == "POST":
		try:
			xSize = int(request.form["xSize"])
			ySize = int(request.form["ySize"])
			seed = int(request.form["seed"])
			bias = float(request.form["bias"])
			smoothing = int(request.form["smoothing"])

			image.prodImg(xSize, ySize, "generated/image.png", seed, smoothing, bias, 25)
			
			#Download file
			return send_file("generated/image.png", as_attachment=True)
		except:
			flash("Wrong data type!")
			return render_template("genHeightmap.html")
	return render_template("genHeightmap.html")

@app.route("/loadheightmap", methods=("GET", "POST"))
def loadHeightmap():
	if request.method == 'POST':
		uploaded_file = request.files['fileS']
		if uploaded_file.filename != '':
			uploaded_file.save(app.config['UPLOAD_FOLDER'] + "img.png")
			try:
				xSize = int(request.form["xSize"])
				ySize = int(request.form["ySize"])
				normals = bool(request.form["normals"])

				generate.runGen(xSize, ySize, "generated/terrain.obj", "uploads/img.png", normals)

				#Download file
				return send_file("generated/terrain.obj", as_attachment=True)
			except:
				flash("Wrong data type!")
				return render_template("loadHeightmap.html")
		return redirect(url_for('loadHeightmap'))
	return render_template("loadHeightmap.html")