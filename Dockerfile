FROM python:3.8-slim-buster

WORKDIR /app

ENV FLASK_ENV=development
ENV FLASK_APP=server.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]