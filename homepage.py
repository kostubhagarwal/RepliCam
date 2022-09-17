from flask import Flask, render_template, request, send_file
from test_filemod import samplefilemod
import io

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 10E6
app.config["UPLOAD_EXTENSIONS"] = [".las", ".txt"]

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        return send_file(samplefilemod(request.files["file"]), as_attachment=True, download_name="unnamed.txt", mimetype="text/plain")
        
    else:
        return render_template("index.html")
