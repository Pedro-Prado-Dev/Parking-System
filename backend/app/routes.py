from flask import Blueprint, request, jsonify
from .models import db, Vehicle

bp = Blueprint('main', __name__)

@bp.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify([{
        'id': vehicle.id,
        'plate_number': vehicle.plate_number,
        'owner_name': vehicle.owner_name,
        'phone_number': vehicle.phone_number
    } for vehicle in vehicles])

@bp.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.json
    plate_number = data.get('plate_number')
    owner_name = data.get('owner_name')
    phone_number = data.get('phone_number')  

    new_vehicle = Vehicle(plate_number=plate_number, owner_name=owner_name, phone_number=phone_number)
    db.session.add(new_vehicle)
    db.session.commit()

    return jsonify({'message': 'Vehicle added successfully'}), 201

@bp.route('/vehicles/<int:id>', methods=['GET'])
def get_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    return jsonify({
        'id': vehicle.id,
        'plate_number': vehicle.plate_number,
        'owner_name': vehicle.owner_name,
        'phone_number': vehicle.phone_number  
    })
    
@bp.route('/vehicles/<int:id>', methods=['PUT'])
def update_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    data = request.json
    
    if 'plate_number' in data:
        vehicle.plate_number = data['plate_number']
    if 'owner_name' in data:
        vehicle.owner_name = data['owner_name']
    if 'phone_number' in data:
        vehicle.phone_number = data['phone_number']  
    
    db.session.commit()
    
    return jsonify({'message': 'Vehicle updated successfully'})

@bp.route('/vehicles/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    
    return jsonify({'message': 'Vehicle deleted successfully'})
