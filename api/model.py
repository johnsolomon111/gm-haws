from api import dbase

class Trash(dbase.Model):
	__tablename__ = 'trash'

	id = dbase.Column(dbase.Integer, primary_key=True)
	lat = dbase.Column(dbase.Float)
	lng = dbase.Column(dbase.Float)
	location = dbase.Column(dbase.String(200))
	height = dbase.Column(dbase.Float)
	weight = dbase.Column(dbase.Float)

	def __init__(self, lat='',lng='',location='',height='',weight=''):
		self.lat = lat
		self.lng = lng
		self.location = location
		self.height = height
		self.weight = weight