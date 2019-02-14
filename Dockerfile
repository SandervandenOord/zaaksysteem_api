FROM ubuntu:latest

LABEL maintainer="Sander van den Oord"

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

COPY . /calculator_app
WORKDIR /calculator_app

RUN pip3 install -r requirements.txt

CMD ["python3", "calculator_app.py"]