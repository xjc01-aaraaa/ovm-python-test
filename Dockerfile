FROM python:3.13.0

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "ovmTest.py"]
