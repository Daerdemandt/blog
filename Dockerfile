FROM python:3-slim

RUN pip install --upgrade pip

RUN pip install pytz

COPY . /src

WORKDIR /src

CMD python3 main.py
