from flask import Flask,render_template,request,redirect
from reg import*

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    msg=""
    if request.method=="POST":
        registration(request.form["name"],request.form["age"],request.form["address"],request.form["course"])
        msg="Registration was Finshed"
    data=read_json()
      
    return render_template("well.html",students=data["students"],message=msg)

@app.route("/delete/<id>")
def delete(id):
    delete_stud(id)
    return redirect("/")

@app.route("/update/<id>",methods=["POST","GET"])
def update(id):
      update_stud(id,request.form["name"],request.form["age"],request.form["address"],request.form["course"])
      return redirect("/")
    
    

if __name__=="__main__":
 app.run(debug=True,host="0.0.0.0",port=5022)

