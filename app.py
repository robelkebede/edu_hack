
from flask import Flask,render_template,request,jsonify
from sklearn.cluster import KMeans
import numpy as np


app = Flask(__name__,static_url_path="/static")

def unsupervised_ml(score):

    X = np.load("stud_data.npy")
    X = np.append(score,X)[:,np.newaxis]

    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    labels = np.array(kmeans.labels_)[:,np.newaxis]
    stud_id = np.array([i for i in range(len(labels))])[:,np.newaxis]

    print(labels.shape)
    print(stud_id.shape)
    table = np.concatenate([stud_id,labels],axis=1)
    return table,X


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
    table,X = unsupervised_ml(student_score)

    print(student_score)

    stud_id = table[:,0]
    cl = table[:,1]

    table = np.concatenate([table,X],axis=1)

    #return render_template("result.html",stud_id=stud_id,score=score)
    return render_template("result.html",table=table)


if __name__ == "__main__":
    app.run(debug=True)

