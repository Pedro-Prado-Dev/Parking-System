from flask import Blueprint, render_template, request, redirect, url_for
import requests

bp = Blueprint('main', __name__, template_folder='templates')  # Define o diretório de templates

backend_url = 'http://backend:5000'

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/vehicles', methods=['GET'])
def vehicle_list():
    response = requests.get(f'{backend_url}/vehicles')
    vehicles = response.json()
    return render_template('vehicle_list.html', vehicles=vehicles)

@bp.route('/vehicles/add', methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        data = {
            'plate_number': request.form['plate_number'],
            'owner_name': request.form['owner_name'],
            'phone_number': request.form['phone_number']
        }
        response = requests.post(f'{backend_url}/vehicles', json=data)
        return redirect(url_for('main.vehicle_list'))
    return render_template('vehicle_form.html', action=url_for('main.add_vehicle'))

@bp.route('/vehicles/<int:id>/edit', methods=['GET', 'POST'])
def edit_vehicle(id):
    response = requests.get(f'{backend_url}/vehicles/{id}')
    vehicle = response.json()

    if request.method == 'POST':
        data = {
            'plate_number': request.form['plate_number'],
            'owner_name': request.form['owner_name'],
            'phone_number': request.form['phone_number']
        }
        response = requests.put(f'{backend_url}/vehicles/{id}', json=data)
        return redirect(url_for('main.vehicle_list'))

    return render_template('vehicle_form.html', vehicle=vehicle, action=url_for('main.edit_vehicle', id=id))

@bp.route('/vehicles/<int:id>/delete', methods=['POST'])
def delete_vehicle(id):
    response = requests.delete(f'{backend_url}/vehicles/{id}')
    return redirect(url_for('main.vehicle_list'))
