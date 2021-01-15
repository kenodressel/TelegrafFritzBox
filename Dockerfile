FROM python:slim-buster

WORKDIR /opt/fritzbox-metrics

# Copy the requirements and install them
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./*.py .

CMD ["python3", "-u", "main.py"]
