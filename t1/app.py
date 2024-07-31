from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/', methods=['POST',  'GET'])
def index():
    if request.method == 'POST':
	    print(request.form)
	    res = make_response("")
	    res.set_cookie("name", request.form.get('name','email'), None)
	    return render_template('hi.html')
    
    return render_template('form.html')

@app.route("/greetings", methods=['POST',  'GET'])
def index():
    if request.method == 'POST':
	    res = make_response("")
	    res.set_cookie("name", request.form.get('name','email'), max_age=0)
	    return render_template('form.html')
    
    return render_template('hi.html')