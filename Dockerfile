# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install flask==3.0.*
RUN pip3 install fastf1
RUN pip3 install gunicorn

# install app
COPY app.py /
COPY templates /templates
COPY static /static

# final configuration
EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "--timeout", "180", "app:app"]