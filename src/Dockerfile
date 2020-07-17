FROM python:alpine
COPY main.py /
RUN pip install requests influxdb  schedule
CMD ["python","main.py"]
