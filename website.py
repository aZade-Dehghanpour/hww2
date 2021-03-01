from flask import Flask, render_template, request, redirect

app = Flask(__name__)

PROGRAMS = ["Software Engineering", "Product Management", "Interaction Design"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/firstpage", methods=["POST"])
def firstpage():
    if request.method == "POST":
        name = request.form.get("name")
    return render_template("firstpage.html", name = "name", programs = PROGRAMS)


@app.route("/info", methods =["GET", "POST"])
def info():
    
    program = request.form.get("programs")
    return render_template("info.html", program = program)



if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

