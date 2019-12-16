
from __future__ import print_function
from __future__ import division
from time import sleep
from easygopigo3 import EasyGoPiGo3

import time
import gopigo3
import signal
import easygopigo3 as easy
import csv

GPG = easy.EasyGoPiGo3()
gpg_motor = gopigo3.GoPiGo3()


print("hi")
distance = GPG.init_distance_sensor()
print("no")

def square_loop():
    reading1 = format(distance.read_mm())
    
    while (int(reading1) >= 500):
        
        GPG.drive_cm(25)
        
    
        GPG.turn_degrees(90)
                                         
        print("Reading1 is: " + reading1 + "mm ")
        reading2 = format(distance.read_mm())
        f.write(str(gpg_motor.get_motor_encoder(gpg_motor.MOTOR_LEFT))) 
        
        print("Reading2 is: " + reading2 + "mm ")
        while (int(reading2) < 500):
            GPG.turn_degrees(180)
            left_loop()
            
        else:
            square_loop()
            f.close()
            f.open('csvfile.csv' , 'a')
def left_loop():
    GPG.turn_degrees(-90)
    reading3 = format(distance.read_mm())
    while (int(reading3) > 500):
        GPG.drive_cm(25)
        GPG.turn_degrees(-90)
        reading4 = format(distance.read_mm())
        while (int(reading4) < 500):
            GPG.turn_degrees(180)
            GPG.stop()
            GPG.turn_degrees(90)
            square_loop()

         
"""
print("Encoder L: %6d R: %6d" % (gpg_motor.get_motor_encoder(gpg_motor.MOTOR_LEFT), gpg_motor.get_motor_encoder(gpg_motor.MOTOR_RIGHT)))
for i in range(0, 361):
            gpg_motor.set_motor_position(gpg_motor.MOTOR_LEFT + gpg_motor.MOTOR_RIGHT , i)
            time.sleep(0.01)
    
    for i in range(0, 361):
        gpg_motor.set_motor_position(gpg_motor.MOTOR_LEFT + gpg_motor.MOTOR_RIGHT , i)
        time.sleep(0.01)
        print("Encoder L: %6d R: %6d" % (gpg_motor.get_motor_encoder(gpg_motor.MOTOR_LEFT), gpg_motor.get_motor_encoder(gpg_motor.MOTOR_RIGHT)))       
            
 """

while (int(format(distance.read_mm())) < 500):
    GPG.turn_degrees(180)
    square_loop()

while True:
    f =open ('csvfile.csv' , 'w')
    f.write('"Index" , "Wheel Encoder" , "Distance Sensor"')
    f.write('"Index" , "Wheel 2Encoder" , "Distance Sensor"')
    square_loop()
    
