
FROM python:3.8-slim

WORKDIR /api-Fernanda

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "servicios-cloud-Fernanda.py"]
