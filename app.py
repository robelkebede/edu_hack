
from flask import Flask,render_template,request


app = Flask(__name__)


def grade(s_ans,ans):
    correct = 0

    for i in range(len(ans)):
        if s_ans[i]==ans[i]:
            correct+=1

    return correct

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
    living = request.form['8']  
    s_ans = [year,atom,gas,clouds,alt,study,layer,living]
    answer = ["Troposphere","Oxygen","Troposphere","meteorology","Exosphere",
    "Thermosphere"," Ernst Haeckel","b"]

    student_score = grade(s_ans,answer)

    print(student_score)

    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)

