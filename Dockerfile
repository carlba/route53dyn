FROM python:3

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install -e .

CMD route53dyn

