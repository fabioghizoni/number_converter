FROM python:3.7-alpine

WORKDIR /number_converter

COPY . /number_converter

RUN pip install --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt
