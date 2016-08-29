from flask import Flask, render_template, redirect, url_for, make_response, request
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

@app.route('/entry', methods=['POST', 'GET'])
def edit_view():
	if request.method == 'POST':
		if 'title' in request.POST:
			title = request.POST['title']
		else:
			title = None

		if 'date' in request.POST:
			date = request.POST['date']
		else:
			date = None

		if 'timeSpent' in request.POST:
			time = request.POST['timeSpent']
		else:
			time = None

		if 'whatILearned' in request.POST:
			learned = request.POST['whatILearned']
		else:
			learned = None

		if 'resourcesToRemember' in request.POST:
			resources = request.POST['resourcesToRemember']
		else:
			resources = None

		Entry.create(title=title, date=date, time_spent=time, resources=resources, learned=learned)

		return redirect(url_for('index'))
	else:
		return render_template('new.html')

app.run(debug=True, port=8000, host='0.0.0.0')