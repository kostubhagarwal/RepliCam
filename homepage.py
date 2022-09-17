from flask import Flask, render_template, request
from test_filemod import samplefilemod
import io

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 10E6
app.config["UPLOAD_EXTENSIONS"] = [".las", ".txt"]

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        samplefilemod(request.files["file"])
        return "Success", 200
        
    else:
        return render_template("index.html")
