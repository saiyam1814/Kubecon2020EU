from influxdb import InfluxDBClient
import schedule
import time
import socket

def influx():
    print("starting")
    client = InfluxDBClient(host='192.168.1.129', port=31713)
    client.create_database('kubecon')
    client.switch_database('kubecon')
    current = time.strftime('%Y-%m-%d %H:%M:%S')
    tempFile = open('/sys/class/thermal/thermal_zone0/temp')
    temp = float(tempFile.read())
    tempC = temp/1000
    print(tempC)
    print(type(tempC))
    json_body = [
    {
        "measurement": "Temp",
        "tags": {
            "system": "{}".format(socket.gethostname()),
        },
        "time": "{}".format(current),
        "fields": {
            "temperature": tempC
        }
    }]
    client.write_points(json_body)

schedule.every(5).seconds.do(influx)   
while 1:
    schedule.run_pending()
    time.sleep(1)
