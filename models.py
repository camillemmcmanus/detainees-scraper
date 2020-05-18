import peewee


db = peewee.SqliteDatabase(
	'detainees.db',
	pragmas={'foreign_keys': 1}
)


class Detainees(peewee.Model):
	# last_name = peewee.CharField(primary_key=True)
	# first_name = peewee.CharField()
	# middle_name = peewee.CharField()
	# suffix = peewee.CharField()
	name = peewee.CharField()
	height = peewee.CharField()
	weight = peewee.IntegerField()
	sex = peewee.CharField()
	eyes = peewee.CharField()
	hair = peewee.CharField()
	race = peewee.CharField()
	age = peewee.IntegerField()
	city = peewee.CharField()
	state = peewee.CharField()

	class Meta:
		database = db

class Details(peewee.Model):
	case_num = peewee.CharField()
	charge_description = peewee.CharField()
	charge_status = peewee.CharField()
	bail_amount = peewee.IntegerField()
	bond_type = peewee.CharField()
	court_date = peewee.DateField()
	court_time = peewee.TimeField()
	court_of_jurisdiction = peewee.CharField()

	class Meta:
		database = db



db.connect()
db.create_tables([Detainees, Details])