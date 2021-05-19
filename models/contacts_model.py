from services.db import Database

instance = Database()

class ContactsModel:
    def get_contacts() -> dict:
        query = 'SELECT name, phone FROM contacts WHERE status = "1"'

        cursor = instance.connect()

        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def get_phone(phone: str) -> dict:
        query = 'SELECT COUNT(id) FROM contacts WHERE phone = {}'.format(phone)

        cursor = instance.connect()

        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def create_contact(name: str, phone: str) -> any:
        query_insert = 'INSERT INTO contacts (`name`, `phone`, `status`) VALUES ("{}", "{}", "1")'.format(name, phone)

        cursor = instance.connect()

        cursor.execute(query_insert)

        instance.commit()

    def get_contact_by_id(id: int) -> dict:
        query = 'SELECT COUNT(id), name, phone, status FROM contacts WHERE id = {}'.format(id)

        cursor = instance.connect()

        cursor.execute(query)
        result = cursor.fetchall()

        return result

    def update_contact(phone: str, name: str, id: int) -> any:
        query_update = 'UPDATE contacts SET `phone` = "{}", `name` = "{}" WHERE id = {}'.format(phone, name, id)
        
        cursor = instance.connect()

        cursor.execute(query_update)
        instance.commit()
        

    def delete_contact(id: int) -> any:
        query_delete = 'UPDATE contacts SET status = "0" WHERE id = {}'.format(id)
        
        cursor = instance.connect()

        cursor.execute(query_delete)
        instance.commit()