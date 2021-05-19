from flask import Blueprint, Response, request

from controllers.contacts_controller import ContactsController

router = Blueprint('routes', __name__)

@router.route('/contacts', methods=['GET'])
def get_contacts():
    return ContactsController.get_contacts()

@router.route('/contact/insert', methods=['POST'])
def set_contacts():
    return ContactsController.set_contact(request.get_json())

@router.route('/contact/update/<id>', methods=['POST'])
def update_contact(id = 0):
    return ContactsController.update_user(id)

@router.route('/contact/delete/<id>', methods=['GET'])
def delete_contact(id = 0):
    return ContactsController.delete_contact(id)

@router.route('/', methods=['GET'])
def index():
    response = '{"response": "Everything working around here"}'

    return Response(response, status=200, mimetype='application/json')