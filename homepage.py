from flask import Flask, render_template, request, send_file, redirect, send_from_directory, flash
from test_filemod import samplefilemod
from werkzeug.utils import secure_filename
import string
import os
import io
import random

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 10E6
app.config["UPLOAD_EXTENSIONS"] = [".las", ".txt"]
app.config["UPLOAD_FOLDER"] = "/tmp"

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("no file found")
        return redirect(request.url)
    file = request.files["file"]
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=16)) + secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return {"filename": filename}, 200

@app.route("/download/<name>", methods=["GET"])
def download(name):
    print("I find")
    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)

        
