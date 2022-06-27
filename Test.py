from flask import Flask , request,json,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://name:pass@pg:5432/testdb'
db=SQLAlchemy(app)


class Person(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    def __init__(self,id,name):
        self.id=id
        self.name=name

@app.route("/",methods=["GET","POST"])
def fn():
    if(request.method=="GET"):return render_template("1.html")
    elif(request.method=="POST"):
        id=request.form["id"]
        name=request.form["name"]
        db.session.add(Person(id,name))
        db.session.commit()
        return render_template("2.html",persons=Person.query.all())

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0",port=5000,debug=True)