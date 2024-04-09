# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask==3.0.*
RUN pip install fastf1
RUN pip install gunicorn

# install app
COPY app.py /
COPY templates /templates
COPY static /static

# final configuration
EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "app:app"]