#!/usr/bin/python
# This shows a service of an MQTT subscriber.
# Copyright (c) 2010-2015, By openthings@163.com.

import sys
import datetime
import socket, sys
import paho.mqtt.publish as publish

def transmitMQTT(strMsg):
    #strMqttBroker = "localhost"
    strBroker = "192.168.1.111"
    strMqttChannel = "/inode/mychannel"
    print(strMsg)
    publish.single(strMqttChannel, strMsg, hostname = strBroker)

if __name__ == '__main__':
    #transmitMQTT("Hello,MQTT Proxy, I am client inside python.")
    transmitMQTT("test!!")
    print "Send msg ok."
