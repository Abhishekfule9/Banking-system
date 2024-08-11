import smbus
import RPi.GPIO as GPIO
from time import sleep, strftime, time
import thingspeak
import sys
import random
import datetime
import telepot
import os
channel_id =2023857
write_key = 'IEG2Q0NU6YWH7L6P'
channel = thingspeak.Channel(id=channel_id,api_key=write_key)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Got command: %s' % command)
    print("chat id:%s"%chat_id)
bot = telepot.Bot('5734791433:AAHmuzl31YjNitmcP9n25Vd6cy0EwWOSrYg')
bot.message_loop(handle)
print ('I am listening...')


GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10,GPIO.OUT,initial=GPIO.LOW)
address = 0x48
bus = smbus.SMBus(1)
while True:
    sleep(0.7)
    bus.write_byte(address,1)
    sleep(0.7)
    value = bus.read_byte(address)
    voltage=0.04705*value
    print("Voltage "+str(voltage)+" V")
    sleep(1)
    bus.write_byte(address,2)
    sleep(0.7)
    value1=bus.read_byte(address)
    voltage1=0.0647*value
    curr=voltage1*0.001
    print("Current "+str(curr)+"mA")
    sleep(1)
    bus.write_byte(0x48,3)
    sleep(0.9)
    value2=bus.read_byte(0x48)
    temp=value2*0.196
    print("Temperature= "+str(temp)+" C")
    file = open("/home/pi/ADC/bms_log.csv", "a")
    file.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(voltage),str(curr),str(temp)))
    response = channel.update({'field1': voltage,'field2':curr,'field3':temp})
    if(voltage<7.0):
        lat,lan = os.popen('curl ipinfo.io/loc').read().split(',')
        print()
        print("Latitude is ",lat)
        print("Longitude is ",lan)
        print()
        link = "Charging Station\nGoogle map link=\nhttps://www.google.com/maps/dir/?api=1&destination="+lat+","+lan+"\n"
        bot.sendMessage(1216740058,link )
    sleep(2)
