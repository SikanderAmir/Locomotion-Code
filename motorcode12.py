# -*- coding: utf-8 -*-
"""
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

"""


import RPi.GPIO as io
import time 
io.setmode(io.BCM)
PWM_MAX = 100
io.setwarnings(False)
#HC-SR04 (Sonar)
TRIG = 21      
ECHO = 24

#L298 M1 M2 M3
EN1 = 25
EN2 = 5
EN3 = 20

#IBT2----(LEFT MOTOR)
L_L_EN = 22 # leftmotor_in1_pin
L_R_EN = 23 # leftmotor_in2_pin
L_L_PWM = 18 # leftmotorpwm_pin_l
L_R_PWM = 17 # leftmotorpwm_pin_r

#IBT2----(RIGHT MOTOR)
R_L_EN = 13 # rightmotor_in1_pin
R_R_EN = 19 # rightmotor_in2_pin
R_L_PWM = 12 # rightmotorpwm_pin_l
R_R_PWM = 6 # rightmotorpwm_pin_r

#/////////////////////////// For SONAR /////////////////////
io.setup(TRIG,io.OUT)                  
io.setup(ECHO,io.IN)

#/////////////////////////// For PUMP MOTOR ///////////////
io.setup(EN1, io.OUT)
io.setup(EN2, io.OUT)
io.setup(EN3, io.OUT)

io.output(EN1,io.LOW)
io.output(EN2,io.LOW)
io.output(EN3,io.LOW)

#////////////////////////// FOR IBT2 MOTOR ////////////////
leftmotor_in1_pin = L_L_EN
leftmotor_in2_pin = L_R_EN
rightmotor_in1_pin = R_L_EN
rightmotor_in2_pin = R_R_EN

io.setup(leftmotor_in1_pin, io.OUT)
io.setup(leftmotor_in2_pin, io.OUT)
io.setup(rightmotor_in1_pin, io.OUT)
io.setup(rightmotor_in2_pin, io.OUT)

#State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
io.output(leftmotor_in1_pin, True)
io.output(leftmotor_in2_pin, True)
io.output(rightmotor_in1_pin, True)
io.output(rightmotor_in2_pin, True)

leftmotorpwm_pin_l = L_L_PWM 
leftmotorpwm_pin_r = L_R_PWM
rightmotorpwm_pin_l = R_L_PWM
rightmotorpwm_pin_r = R_R_PWM

io.setup(leftmotorpwm_pin_l, io.OUT)
io.setup(leftmotorpwm_pin_r, io.OUT)
io.setup(rightmotorpwm_pin_l, io.OUT)
io.setup(rightmotorpwm_pin_r, io.OUT)

#To create a PWM instance:p = IO.PWM(channel, frequency)
leftmotorpwm_l = io.PWM(leftmotorpwm_pin_l,100)
leftmotorpwm_r = io.PWM(leftmotorpwm_pin_r,100)
rightmotorpwm_l = io.PWM(rightmotorpwm_pin_l,100)
rightmotorpwm_r = io.PWM(rightmotorpwm_pin_r,100)

#To start PWM: p.start(dc)# where dc is the duty cycle (0.0 <= dc <= 100.0)
leftmotorpwm_l.start(0)
leftmotorpwm_r.start(0)
rightmotorpwm_l.start(0)
rightmotorpwm_r.start(0)
#To change the duty cycle:p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0
leftmotorpwm_l.ChangeDutyCycle(0)
leftmotorpwm_r.ChangeDutyCycle(0)
rightmotorpwm_l.ChangeDutyCycle(0)
rightmotorpwm_r.ChangeDutyCycle(0)



while True:

  io.output(TRIG, False)                 #Set TRIG as LOW
  print ('Waitng For Sensor To Settle')
  time.sleep(2)                            #Delay of 2 seconds

  io.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  io.output(TRIG, False)                 #Set TRIG as LOW

  while io.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while io.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance > 10 :      #Check whether the distance is within range
    print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
    def setMotorMode(mode , spray):
       
        if mode == "reverse":
                io.output(leftmotor_in1_pin, True)
                io.output(leftmotor_in2_pin, False)
                io.output(rightmotor_in1_pin, False)
                io.output(rightmotor_in2_pin, True)  
        elif  mode == "forward":
                 io.output(leftmotor_in1_pin, False)
                 io.output(leftmotor_in2_pin, True)
                 io.output(rightmotor_in1_pin, True)
                 io.output(rightmotor_in2_pin, False)
                 if spray == "True":
                     io.output(EN1,io.HIGH)
                     io.output(EN2,io.HIGH)
                     io.output(EN3,io.HIGH)
                     
                
        elif  mode == "LEFT":
                 io.output(leftmotor_in1_pin, False)
                 io.output(leftmotor_in2_pin, False)
                 io.output(rightmotor_in1_pin, True)
                 io.output(rightmotor_in2_pin, False)
        elif  mode == "RIGHT":
                 io.output(leftmotor_in1_pin, False)
                 io.output(leftmotor_in2_pin, True)
                 io.output(rightmotor_in1_pin, False)
                 io.output(rightmotor_in2_pin, False)
        else:
                io.output(leftmotor_in1_pin, False)
                io.output(leftmotor_in2_pin, False)
                io.output(rightmotor_in1_pin, False)
                io.output(rightmotor_in2_pin, False)
        

  else:
    print ("DANGER")
    break


#///////////////////SHUTTING MOTORS OFF/////
io.output(leftmotor_in1_pin, False)
io.output(leftmotor_in2_pin, False)
io.output(rightmotor_in1_pin, False)
io.output(rightmotor_in2_pin, False)

#///////////////////SHUTTING PUMPS OFF/////
io.output(EN1,io.LOW)
io.output(EN2,io.LOW)
io.output(EN3,io.LOW)





