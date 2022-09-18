from flask import Flask, render_template, request, send_file, redirect, send_from_directory, flash
from werkzeug.utils import secure_filename
from stltogcode import gcode_convert
from plytostl import stl_convert

import string
import os
import io
import random
import tempfile

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 10E6
app.config["UPLOAD_EXTENSIONS"] = [".las", ".txt"]
app.config["UPLOAD_FOLDER"] = tempfile.gettempdir()

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files["file"]
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) + secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename), buffer_size=16384)
    stl_filename = stl_convert(filename, app.config["UPLOAD_FOLDER"])
    gcode_filename = gcode_convert(stl_filename, app.config["UPLOAD_FOLDER"])
    return {"filename": filename}, 200

@app.route("/print/<name>", methods=["GET"])
def print(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)

        
