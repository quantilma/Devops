FROM ubuntu:latest
MAINTAINER Julian Nino "juliannino01@hotmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
ADD . /flask-app
WORKDIR /flask-app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/usr/bin/python3"]
CMD ["flask-docker.py"]
