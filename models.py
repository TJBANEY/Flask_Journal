from peewee import *
import datetime

DATABASE = SqliteDatabase('entries.db')

class Entry(Model):
	title = CharField(max_length=255, null=True)
	date = DateTimeField(default=datetime.datetime.now(), null=True)
	time_spent = IntegerField(default=0, null=True)
	resources = TextField(null=True)
	learned = TextField(null=True)

	class Meta:
		database = DATABASE