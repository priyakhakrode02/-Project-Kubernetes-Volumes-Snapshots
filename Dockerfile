FROM python:3.8.0-slim

RUN pip install --upgrade pip

WORKDIR /myapp

COPY . /myapp

RUN apt-get update -y && apt-get upgrade -y

RUN pip install -r requirements.txt

CMD ["python", "Hello-flask.py"]
~                                  
