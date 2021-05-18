# -*- coding: utf-8 -*-
"""
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

"""


import RPi.GPIO as io
io.setmode(io.BCM)
PWM_MAX = 100
io.setwarnings(False)


L_L_EN = 22 # leftmotor_in1_pin
L_R_EN = 23 # leftmotor_in2_pin
L_L_PWM = 18 # leftmotorpwm_pin_l
L_R_PWM = 17 # leftmotorpwm_pin_r

R_L_EN = 13 # rightmotor_in1_pin
R_R_EN = 19 # rightmotor_in2_pin
R_L_PWM = 12 # rightmotorpwm_pin_l
R_R_PWM = 6 # rightmotorpwm_pin_r


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

def setMotorMode(motor, mode):
   if motor == "leftmotor":
      if mode == "reverse":
         io.output(leftmotor_in1_pin, True)
         io.output(leftmotor_in2_pin, False)
      elif  mode == "forward":
         io.output(leftmotor_in1_pin, False)
         io.output(leftmotor_in2_pin, True)
      else:
         io.output(leftmotor_in1_pin, False)
         io.output(leftmotor_in2_pin, False)
   elif motor == "rightmotor":
      if mode == "reverse":
         io.output(rightmotor_in1_pin, False)
         io.output(rightmotor_in2_pin, True)      
      elif  mode == "forward":
         io.output(rightmotor_in1_pin, True)
         io.output(rightmotor_in2_pin, False)
      else:
         io.output(rightmotor_in1_pin, False)
         io.output(rightmotor_in2_pin, False)
   else:
      io.output(leftmotor_in1_pin, False)
      io.output(leftmotor_in2_pin, False)
      io.output(rightmotor_in1_pin, False)
      io.output(rightmotor_in2_pin, False)


def setMotorLeft(power):
   int(power)
   if power < 0:
      pwm = -int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      leftmotorpwm_l.ChangeDutyCycle(pwm)
      leftmotorpwm_r.ChangeDutyCycle(0)	  
   elif power > 0:
      pwm = int(PWM_MAX * power)
      if pwm > PWM_MAX:
         pwm = PWM_MAX
      leftmotorpwm_l.ChangeDutyCycle(0)
      leftmotorpwm_r.ChangeDutyCycle(pwm)
   else:
      leftmotorpwm_l.ChangeDutyCycle(0)
      leftmotorpwm_r.ChangeDutyCycle(0)


def setMotorRight (power):
   int (power)
   if power <0:
      # Backward mode for the right motor
      #setMotorMode ("rightmotor", "reverse")
      pwm = -int (PWM_MAX * power)
      if pwm> PWM_MAX:
         pwm = PWM_MAX
      rightmotorpwm_l.ChangeDutyCycle (pwm)
      rightmotorpwm_r.ChangeDutyCycle (0)
   elif power> 0:
      # Forward mode for the right motor
      #setMotorMode ("rightmotor", "forward")
      pwm = int (PWM_MAX * power)
      if pwm> PWM_MAX:
         pwm = PWM_MAX
      rightmotorpwm_l.ChangeDutyCycle (0)
      rightmotorpwm_r.ChangeDutyCycle (pwm)
   else:
      # Stop mode for the right motor
      rightmotorpwm_l.ChangeDutyCycle (0)
      rightmotorpwm_r.ChangeDutyCycle (0)


