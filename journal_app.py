from flask import Flask, render_template, redirect, url_for, make_response, request
from models import *

import json

app = Flask(__name__)
app._static_folder = "./static/"

@app.route('/')
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

@app.route('/delete/<id>')
def delete_view(id):
	entry = Entry.select().where(Entry.id == id).get()
	entry.delete_instance()

	return redirect(url_for('index'))

@app.route('/entry', methods=['POST', 'GET'])
@app.route('/entry/<id>', methods=['POST', 'GET'])
def edit_add_view(id=0):
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

			return render_template('edit.html', **context)

app.run(debug=True, port=8000, host='0.0.0.0')