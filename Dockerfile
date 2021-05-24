FROM python:3.8-slim-buster

WORKDIR /app

ENV FLASK_ENV=development
ENV FLASK_APP=server.py

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]