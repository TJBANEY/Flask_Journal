from peewee import *
import datetime

DATABASE = SqliteDatabase('entries.db')

class Entry(Model):
	title = CharField(max_length=255, null=True)
	date = DateTimeField(default=datetime.datetime.now(), null=True)
	time_spent = CharField(null=True)
	resources = TextField(null=True)
	learned = TextField(null=True)

	class Meta:
		database = DATABASE

DATABASE.connect()