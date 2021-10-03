FROM python:3.8.0-slim

RUN apt-get update \
&& apt-get install gcc  libc-dev -y \
&& apt-get clean

COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pipenv
RUN pipenv install --system --ignore-pipfile --dev

RUN mkdir /calculator
COPY . /calculator
WORKDIR /calculator

EXPOSE 8000
