FROM python:3.9-slim

RUN pip install flask
RUN pip install --upgrade google-cloud-datastore


WORKDIR /app

COPY . .
CMD ["python3", "app.py"]
EXPOSE 5000
