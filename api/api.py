from api import *

@server.route('/trash', methods=["GET"])
def get_all_trash():
	trashes = Trash.query.all()

	output = []

	for trash in trashes:
		trash_data = {}
		trash_data['id'] = trash.id
		trash_data['lat'] = trash.lat
		trash_data['lng'] = trash.lng
		trash_data['location'] = trash.location
		trash_data['weight'] = trash.weight
		trash_data['height'] = trash.height
		output.append(trash_data)

	return jsonify({'trashes' : output})

@server.route('/trash/<id>', methods=["GET"])
def get_trash(id):
	trash = Trash.query.filter_by(id=id).first()
	trash_data = {}
	trash_data['lat'] = trash.lat
	trash_data['lng'] = trash.lng
	trash_data['location'] = trash.location
	trash_data['weight'] = trash.weight
	trash_data['height'] = trash.height

	return jsonify({'trashes' : trash_data})

@server.route('/trash', methods=["POST"])
def add_trash():
	lat = request.args['lat']
	lng = request.args['lng']
	location = request.args['location']
	weight = request.args['weight']
	height = request.args['height']

	new_trash = Trash(lat,lng,location,weight,height)
	dbase.session.add(new_trash)
	dbase.session.commit()
	return jsonify({'messege' : 'Added New Trash Bin!'})

@server.route('/trash/<id>',methods=["PUT"])
def update_trash(id):
	trash = Trash.query.filter_by(id=id).first()

	trash.weight = request.args['weight']
	trash.height = request.args['height']
	dbase.session.commit()

	return jsonify({'Trash' : 'Updated weight and height'})

@server.route('/trash/location/<id>',methods=["PUT"])
def update_trash_location(id):
	trash = Trash.query.filter_by(id=id).first()

	trash.lat = request.args['lat']
	trash.lng = request.args['lng']
	trash.location = request.args['location']
	dbase.session.commit()

	return jsonify({'Trash' : 'Updated location'}) #update weight and height

@server.route('/trash/<id>',methods=["DELETE"])
def delete_trash(id):
	trash = Trash.query.filter_by(id=id).first()
	dbase.session.delete(trash)
	dbase.session.commit()
	return jsonify({'Trash' : 'successfully deleted'})
