FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /var/www/byson
WORKDIR /var/www/byson
ADD requirements.txt /var/www/byson/
RUN pip install -r requirements.txt
ADD . /var/www/byson/
