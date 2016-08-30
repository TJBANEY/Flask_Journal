from flask import Flask, render_template, redirect, url_for, make_response, request
from models import *

import json

app = Flask(__name__)
app._static_folder = "./static/"

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

@app.route('/details/<id>')
def detail_view(id):
	entry = Entry.select().where(Entry.id == id).get()
	context = {'entry': entry}

	return render_template('detail.html', **context)

@app.route('/entry', methods=['POST', 'GET'])
@app.route('/entry/<id>', methods=['POST', 'GET'])
def edit_view(id):
	if request.method == 'POST':
		if not id:
			title = request.form.get('title')
			date = request.form.get('date')
			time = request.form.get('timeSpent')
			learned = request.form.get('whatILearned')
			resources = request.form.get('resourcesToRemember')

			Entry.create(title=title, date=date, time_spent=time, 
						resources=resources, learned=learned)

		else:
			entry = Entry.select().where(Entry.id == id).get()

			entry.title = request.form.get('title')
			entry.date = request.form.get('date')
			entry.time = request.form.get('timeSpent')
			entry.learned = request.form.get('WhatILearned')
			entry.resources = request.form.get('resourcesToRemember')

		return redirect(url_for('index'))
	else:
		if not id:
			return render_template('new.html')
		else: 
			entry = Entry.select().where(Entry.id == id).get()

			context = {'entry': entry}

			return render_template('new.html', **context)

app.run(debug=True, port=8000, host='0.0.0.0')