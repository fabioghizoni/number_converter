FROM python:3.7-alpine

WORKDIR /number_converter

COPY . /number_converter

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

ENV PYTHONPATH /number_converter/src/

CMD ["python", "app.py"]
