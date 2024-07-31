from flask import Flask, render_template, request, make_response, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50))
    second_name=db.Column(db.String(50))
    email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg', methods=['POST',  'GET'])
def index():
    if request.method == 'POST':
         first_name=request.form['first_name']
         last_name=request.form['last_name']
         email=request.form['email']
         password=request.form['password']

         new_user=User(first_name=first_name,last_name=last_name, email=email,password=password)
         db.session.add(new_user)
         db.session.commit()
	     return redirect('/')
    
    return render_template('form.html')