    FROM python:3.13.0

    WORKDIR /root

    COPY . .

    ENTRYPOINT ["python", "/root/ovmTest.py"]
