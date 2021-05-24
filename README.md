# Desafio Horus

## 👨🏻‍🔧 Install

First things first, you must have `python3`, `pip3` and `venv` installed. 

At the root folder of the project you need to active the environment with `venv`.

```
source env/bin/activate
```

Some dependencies are needed, go ahead and install them.

```
pip3 install -r requirements.txt
```

Must set a few variables

```
export FLASK_ENV=development
export FLASK_APP=server.py
```

We're almost done. Go to `services/db.py` and change the database variables for yours.

You will find a sql file named `schema.sql`, you have to import it to the database you set at `services/db.py`.

Now run the following code, and if everything went right you are ready to go.

```
flask run
```

### Install with docker

if you prefer you also can run the project with docker, with the .env correctly set up run the following command to build a docker image

```
docker-composer build
```

As the image is built run up the container

```
docker-composer up -d
```

That's all that you need 🎉!

## 🛣️ Routes

### Contacts

Description:

A array with all of the contacts

Request:

```
Get /contacts
```
Responses:

```
200 - OK.
500 - Server Error.
```

If everything goes right the server will return a json:

```
{"contacts": [
  {"id": 24, "name": "Teste1", "phone": "719982837"},
  {"id": 25, "name": "Teste2", "phone": "7199828387"}
]}
```

### Store a contact

Description:

Store a contact in the database

Request:

```
Post /contact/insert
```

Request:

```
{
  "name": "Contact1",
  "phone": "7181271827"
}
```

Responses:

```
200 - OK.
401 - Bad Request.
500 - Server Error.
```

If everything goes right the server will return a json:

```
{'message': 'Contact successfully registered'}
```

### Update a contact

Description:

Update a contact in the database

Request:

```
Post /contact/update/:id
```

Request:

```
{
  "name": "Contact2",
  "phone": "7181271827"
}
```

Responses:

```
200 - OK.
401 - Bad Request.
404 - Not Found.
500 - Server Error.
```

If everything goes right the server will return a json:

```
{'message': 'Successfully updated'}
```

### Delete a contact

Description:

Delete a contact by id

Request:

```
Get /contact/delete/:id
```

Responses:

```
200 - OK.
401 - Bad Request.
404 - Not Found.
500 - Server Error.
```

If everything goes right the server will return a json:

```
{'message': 'Deleted user'}
```

