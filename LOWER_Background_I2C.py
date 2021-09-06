import smbus
import time
import Jetson.GPIO as GPIO
import os
import os
# Nvidia Jetson Nano i2c Bus 0
bus = smbus.SMBus(0)


def I2C_Event(channel):
    GPIO.remove_event_detect(29)
    print("I2C Int!!")
    command = bytes(readNumber(0xFD,3))
    if command[0] == 0x15:
        if command[1] == 0x18:
            if command[2] == 0x65:
                print("shutdown!!")
                time.sleep(3)
                os.system('shutdown -h now')

    print("0x" + command.hex())
    time.sleep(0.001)
    GPIO.add_event_detect(29, GPIO.FALLING, callback=I2C_Event)


# This is the address we setup in the Arduino Program
GPIO.setwarnings(False)
address = 0x08
GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
GPIO.setup(29,GPIO.IN)
GPIO.add_event_detect(29, GPIO.FALLING, callback=I2C_Event)



def writeNumber(value):
    #bus.write_byte(address, value)
    bus.write_byte_data(address, 0, value)
    return -1

def readNumber(Cmd,NumBytes):
    number = bus.read_i2c_block_data(address,Cmd,NumBytes)
    # number = bus.read_byte_data(address, 1)
    return number

# send the cmd to change the mode to measure
bus.write_byte_data(address, 0x00, 0x02)
while True:

    #bus.write_byte_data(address, 0x15, 0x85)
    time.sleep(0.5)
    #number = readNumber(0x85,3)
    #print(number)