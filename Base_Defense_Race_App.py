from flask import Flask, render_template
# import request module to handle incoming form data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/DavyJones")
def DavyJones():
    return render_template("DavyJones.html")

@app.route("/EldritchSpawn-dark")
def EldritchSpawn():
    return render_template("EldritchSpawn-dark.html")

@app.route("/GamblingAddict")
def venv():
    return render_template("GamblingAddict.html")

@app.route("/Hesperides")
def Hesperides():
    return render_template("Hesperides.html")

@app.route("/HordeLich-dark")
def HordeLich():
    return render_template("HordeLich-dark.html")

@app.route("/PlagueCzar")
def PlagueCzar():
    return render_template("PlagueCzar.html")

@app.route("/PuppetMaster")
def PuppetMaster():
    return render_template("PuppetMaster.html")

@app.route("/SealBreaker")
def SealBreaker():
    return render_template("SealBreaker.html")

if __name__ == "__main__":
    app.run(debug=True)