from mqtt_app.management.commands.mqtt_update import MqttConnect
import time
from datetime import datetime
from random import uniform
import json
from paho.mqtt.client import Client
import threading
# import os
# import django
from django.core.management.base import BaseCommand
from mqtt_app.models import Usermaster

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mqtt.settings")
# django.setup()

mq = MqttConnect()
mq.topic = ["661526019560586","324164884510875"]
mqttBroker = "4.240.114.7"
port = 1883
username = "BarifloLabs"
password = "Bfl@123"


def post_data_to_publish():
    mq.connect_to_broker()
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        rand_num = uniform(1.0, 2.0)
        rand_num2 = uniform(1.0, 2.0)
        for i in mq.topic:
            mq.data_publish({"dataPoint": now, "paramType": 'Sensor1', "paramValue": rand_num, "deviceId": i})
            mq.data_publish({"dataPoint": now, "paramType": 'Sensor2', "paramValue": rand_num2, "deviceId": i})
        time.sleep(1)



def data_subscribe():
    mqtt_client = Client()
    mqtt_client.on_connect = mq.on_connect
    mqtt_client.on_message = mq.on_sub_message
    mqtt_client.username_pw_set(username, password)
    mqtt_client.connect(mqttBroker, port=port)
    mqtt_client.loop_start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        mqtt_client.loop_start()





class Command(BaseCommand):
    help = """ (HELP Document)  This is the command For run the mqtt Script File with specific command \n\n\n\n 
    This will execute the mqtt_script file and also it is get the mqtt_update.py file"""
    def handle(self, *args, **options):
        threading.Thread(target=post_data_to_publish).start()
        threading.Thread(target=data_subscribe).start()