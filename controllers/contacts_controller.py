from flask import Response, json, request
from models.contacts_model import ContactsModel

class ContactsController:

    def get_contacts() -> Response:

        contacts = ContactsModel.get_contacts()
        datas = []

        for index in range(len(contacts)):
            id = contacts[index][0]
            name = contacts[index][1]
            phone = contacts[index][2]
            data = {
                'id': id,
                'name': name,
                'phone': phone
            }

            datas.append(data)

        response = {"contacts": datas}

        return Response(json.dumps(response), status=200, mimetype='application/json')

    def set_contact(request: any) -> Response:
        if 'name' in request and 'phone' in request:
            name = request['name']
            phone = request['phone']

            get_phone = ContactsModel.get_phone(phone)
            amount = get_phone[0][0]

            if amount == 0:
                ContactsModel.create_contact(name, phone)

                success_response = json.dumps({'message': 'Contact successfully registered'})

                return Response(success_response, status=200, mimetype='application/json')
            else:
                error_response = json.dumps({'message': 'Phone already registred'})

                return Response(error_response, status=401, mimetype='application/json')
        else:
            error_response = json.dumps({'message': 'Name and phone is required'})

            return Response(error_response, status=400, mimetype='application/json')

    def update_user(id: int) -> Response:
        if int(id) != 0:
            get_contact_by_id = ContactsModel.get_contact_by_id(id)

            amount = get_contact_by_id[0][0]

            if amount > 0:
                get_body_request = request.get_json()

                name = get_contact_by_id[0][1]
                phone = get_contact_by_id[0][2]

                if 'phone' in get_body_request:
                    phone = get_body_request['phone']

                if 'name' in get_body_request:
                    name = get_body_request['name']

                ContactsModel.update_contact(phone, name, id)

                message_response = {'message': 'Successfully updated'}

                return Response(json.dumps(message_response), status=200, mimetype='application/json')
            else:
                message = {'message': 'Contact not exists'}

                return Response(json.parse(message), status=404, mimetype='application/json')
        else:
            error_response = {'message': 'ID is required'}

            return Response(json.dumps(error_response), status=401, mimetype='application/json')

    def delete_contact(id: int) -> Response:
        if int(id) != 0:
            get_status_contact = ContactsModel.get_contact_by_id(id)

            if get_status_contact[0][3] == '1':
                ContactsModel.delete_contact(id)

                message = {'message': 'Deleted user'}

                return Response(json.dumps(message), status=200, mimetype='application/json')
            else:
                message = {'message': 'User does not exist'}

                return Response(json.dumps(message), status=404, mimetype='application/json')
        else:
            error_message = {'message': 'ID is required'}

            return Response(json.dumps(error_message), status=401, mimetype='application/json')