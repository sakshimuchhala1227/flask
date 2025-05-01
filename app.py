from flask import Flask
from flask import request,render_template,redirect,url_for,jsonify
# created a simple flask application
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "welcome to homepage"

@app.route("/index",methods=["GET"])
def index():
    return "helo hehehe"

# variable rule
@app.route("/sucess/<int:score>")         #("/sucess/<score>")
def passed(score):
    return "Total score of student is " + str(score) + " and the student is pass"

@app.route("/fail/<int:score>")         #("/sucess/<score>")
def fail(score):
    return "Total score of student is " + str(score) + " and the student is fail"

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
        res=""
        if average_marks>=50:
            res="passed"
        else:
            res="fail"

        return redirect(url_for(res,score=average_marks))
        # return render_template("form.html",score=average_marks)

@app.route("/api",methods=["POST"])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)["a"])
    b_val=float(dict(data)["b"])    
    return jsonify(a_val+b_val)

if __name__=="__main__" :
    app.run(debug=True)