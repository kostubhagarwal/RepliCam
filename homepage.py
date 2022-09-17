from flask import Flask, render_template, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 10E6

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        print(dir(request))
        return "Success", 200
    else:
        return render_template("index.html")
