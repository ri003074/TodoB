FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /code 
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN apt-get update && apt-get install sqlite3 libsqlite3-dev -y


#add
CMD gunicorn project.wsgi:application --bind 0.0.0.0:$PORT
