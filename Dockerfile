# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask==3.0.*
RUN pip install fastf1

# install app
COPY app.py /
COPY templates /templates

# final configuration
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]