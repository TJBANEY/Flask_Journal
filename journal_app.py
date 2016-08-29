from flask import Flask, render_template, redirect, url_for, make_response
from models import *

import json

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Treehouse'):
	return 'Hello from {}'.format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
	data = get_saved_data()
	context = {'num1': num1, 'num2': num2, 'saves': data}
	return render_template('numbers.html', **context)

@app.route('/save', methods=['POST'])
def save():
	response = make_response(redirect(url_for('index')))
	response.set_cookie('character', json.dumps(dict(request.form.items())))
	return redirect(url_for('index'))

def get_saved_data():
	try:
		data = json.loads(request.cookies.get('character'))
	except TypeError:
		data = {}
	return data

@app.route('/list')
def list_view():
	entries = Entry.select()

	context = {'entries': entries}

	return render_template('index.html', **context)

@app.route('/details')
def detail_view():
	pass

@app.route('/entry')
def edit_view():
	pass

app.run(debug=True, port=8000, host='0.0.0.0')