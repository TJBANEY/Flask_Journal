from peewee import *
import datetime

DATABASE = SqliteDatabase('entries.db')

class Entry(Model):
	title = CharField(max_length=255)
	date = DateTimeField(default=datetime.datetime.now())
	time_spent = IntegerField(default=0)
	resources = CharField()
	learned = TextField()

	class Meta:
		database = DATABASE