
from flask import Flask,render_template,request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/handle_data",methods=["GET","POST"])
def index2():
    year = request.form['year']
    atom = request.form['atm']
    gas = request.form['gas']
    clouds = request.form['clouds']
    alt = request.form['alt']
    study = request.form['study']
    layer = request.form['layer']  
    print([year,atom,gas,clouds,alt,study,layer])

    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)

