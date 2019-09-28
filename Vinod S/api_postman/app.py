from flask import Flask,  request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db= SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    college = db.Column(db.String(200))

    

@app.route('/', methods=['GET'])
def get_user():
    users = User.query.all()
    output=[]
    for user in users:
        userdata = {}
        userdata['id']=user.id
        userdata['name']=user.name
        userdata['college']=user.college
        output.append(userdata)
    
    return jsonify({'user': output})

@app.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(id=data['id'],name=data['name'],college=data['college'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'New user created!!'})
   

if __name__ == "__main__":
    app.run(debug=True)