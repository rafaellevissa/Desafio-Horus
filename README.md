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