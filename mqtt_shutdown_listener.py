#!/usr/bin/python3
import paho.mqtt.client as mqtt
import os
import logging
import logging.handlers
import sys

LOG_FILENAME = "/tmp/mqtt_shutdown_service.log"
LOG_LEVEL = logging.INFO

class MyLogger(object):
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level
        
    def write(self, message):
        if message.rstrip() != "":
            self.logger.log(self.level, message.rstrip())
            
def on_connect(client, userdata, flags, rc):
    print("connected with result code:" + str(rc))
    client.subscribe("shutdown")

def on_message(client, userdata, msg):
    # print("Topic", msg.topic + "\nMessage: " + str(msg.payload))
    print("Topic", msg.topic + "\nMessage: " + msg.payload.decode('utf-8'))
    if msg.payload.decode('utf-8') == "raspberrypi4":
        print("shutting down")
        os.system("systemctl poweroff")
        
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
formatter=logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
logger.addHandler(handler)
            
sys.stdout = MyLogger(logger, logging.INFO)
sys.stderr = MyLogger(logger, logging.ERROR)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.18")
client.loop_forever()