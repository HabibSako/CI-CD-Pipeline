FROM python:3.13.0a4-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 5003

CMD ["python", "ornek.py"]
