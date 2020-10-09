
from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/handle_data",methods=["GET","POST"])
def index2():
    year = request.form['1']
    atom = request.form['2']
    gas = request.form['3']
    clouds = request.form['4']
    alt = request.form['5']
    study = request.form['6']
    layer = request.form['7']  
    print([year,atom,gas,clouds,alt,study,layer]) 
    """
    answer ["Troposphere","Oxygen","Troposphere","meteorology","Exosphere",
    "Thermosphere"," Ernst Haeckel","Living beings that feed on dead or decayed organic matter"]
    """

    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)

