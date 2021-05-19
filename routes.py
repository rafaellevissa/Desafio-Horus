from flask import Blueprint, Response, json, request, jsonify
from db import cursor, database

router = Blueprint('routes', __name__)

@router.route('/contacts', methods=['GET'])
def get_contacts():

    query = 'SELECT name, phone FROM contacts WHERE status = "1"'

    cursor.execute(query)

    contacts = cursor.fetchall()
    datas = []

    for index in range(len(contacts)):
        name = contacts[index][0]
        phone = contacts[index][1]
        data = {
            'name': name,
            'phone': phone
        }

        datas.append(data)

    response = {"contacts": datas}

    return Response(json.dumps(response), status=200, mimetype='application/json')


@router.route('/contact/insert', methods=['POST'])
def set_contacts():
    get_contact_from_request = request.get_json()

    if 'name' in get_contact_from_request and 'phone' in get_contact_from_request:
        name = get_contact_from_request['name']
        phone = get_contact_from_request['phone']

        query = 'SELECT COUNT(id) FROM contacts WHERE phone = {}'.format(phone)

        cursor.execute(query)
        get_phone = cursor.fetchall()
        amount = get_phone[0][0]

        if amount == 0:
            query_insert = 'INSERT INTO contacts (`name`, `phone`, `status`) VALUES ("{}", "{}", "1")'.format(name, phone)

            cursor.execute(query_insert)

            success_response = json.dumps({'message': 'Contact successfully registered'})

            return Response(success_response, status=200, mimetype='application/json')
        else:
            error_response = json.dumps({'message': 'Phone already registred'})

            return Response(error_response, status=401, mimetype='application/json')


    else:
        error_response = json.dumps({'message': 'Name and phone is required'})

        return Response(error_response, status=400, mimetype='application/json')

@router.route('/contact/update/<id>', methods=['POST'])
def update_contact(id = 0):

    if int(id) != 0:
        query = 'SELECT COUNT(id), name, phone FROM contacts WHERE id = {}'.format(id)

        cursor.execute(query)
        result = cursor.fetchall()

        amount = result[0][0]

        if amount > 0:
            get_body_request = request.get_json()

            name = result[0][1]
            phone = result[0][2]

            if 'phone' in get_body_request:
                phone = get_body_request['phone']

            if 'name' in get_body_request:
                name = get_body_request['name']

            query_update = 'UPDATE contacts SET `phone` = "{}", `name` = "{}"'.format(phone, name)
            cursor.execute(query_update)

            message_response = {'message': 'Successfully updated'}

            return Response(json.dumps(message_response), status=200, mimetype='application/json')
        else:
            message = {'message': 'Contact not exists'}

            return Response(json.parse(message), status=404, mimetype='application/json')
    else:
        error_response = {'message': 'ID is required'}

        return Response(json.dumps(error_response), status=401, mimetype='application/json')

@router.route('/contact/delete/<id>', methods=['POST'])
def delete_user(id = 0):
    if int(id) != 0:
        query = 'SELECT status FROM contacts WHERE id = {}'.format(id)

        cursor.execute(query)
        result = cursor.fetchall()

        if result[0]['status'] == '1':
            query_delete = 'UPDATE contacts SET status = "0" WHERE id = {}'.format(id)

            cursor.execute(query_delete)

            message = {'message': 'Deleted user'}

            return Response(json.dumps(message), status=200, mimetype='application/json')
        else:
            message = {'message': 'User does not exist'}

            return Response(json.dumps(message), status=404, mimetype='application/json')
    else:
        error_message = {'message': 'ID is required'}

        return Response(json.dumps(error_message), status=401, mimetype='application/json')

@router.route('/', methods=['GET'])
def index():
    response = '{"response": "Everything working around here"}'

    return Response(response, status=200, mimetype='application/json')