import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # That is BCM pin number

MotorPinForward1 = #the pin in which we connect 1st motor for forward
MotorPinForward2 = #the pin in which we connect 2nd motor for forward
MotorPinBackward1 = #the pin in whiich we connect 1st motor for backward
MotorPinBackward2 = #the pin in whiich we connect 2nd motor for backward

GPIO.setup(MotorPinForward1,GPIO.OUT)
GPIO.setup(MotorPinForward1,GPIO.OUT)
GPIO.setup(MotorPinBackward1,GPIO.OUT)
GPIO.setup(MotorPinBackward1,GPIO.OUT)


pf1=GPIO.PWM(MotorPinForward1,50) # HERE I AM GIVING FREQUENCY AS 50Hz, CAN BE CHANGED LATER
pf2=GPIO.PWM(MotorPinForward2,50) # HERE I AM GIVING FREQUENCY AS 50Hz, CAN BE CHANGED LATER
pb1=GPIO.PWM(MotorPinBackward1,50) # HERE I AM GIVING FREQUENCY AS 50Hz, CAN BE CHANGED LATER
pb2=GPIO.PWM(MotorPinBackward2,50) # HERE I AM GIVING FREQUENCY AS 50Hz, CAN BE CHANGED LATER

pf1.start(0)   # We should start at the duty cycle at which motor runs at 0 speed. I guess it should be 0
pf2.start(0)   # We should start at the duty cycle at which motor runs at 0 speed. I guess it should be 0
pb1.start(0)   # We should start at the duty cycle at which motor runs at 0 speed. I guess it should be 0
pb2.start(0)   # We should start at the duty cycle at which motor runs at 0 speed. I guess it should be 0
print("PRESS F/f TO GO FORWARD")
print("PRESS B/b TO GO BACKWARD")
c= input("PLEASE ENTER YOUR CHOICE ")

while(True):

    if c == 'F' or c=='f':
        print("ENTER THE SPEED ON A SCALE FROM 1 - 100 TO GO IN FORWARD DIRECTION")
        s = input()
        pf1.changeDutyCycle(s)
        pf2.changeDutyCycle(s)
    elif c == 'B' or c=='b':
        print("ENTER THE SPEED ON A SCALE FROM 1 - 100 TO GO IN BACKWARD DIRECTION")
        s = input()
        pb1.changeDutyCycle(s)
        pb2.changeDutyCycle(s)
    
    #In the above function, I am assuming that for a duty cycle of 0 the motor has 0 speed  and for duty cycle of 100, the motor runs in full speed.
    #We can calibrate this by testing with the motor we use, and consider speed variation with respect to duty cycle as linear. 
    #Hence, we would be able to vary the speed, based on duty cycle for which spped is 0, and maximum.

    print("DO YOU WANT TO CHANGE DIRECTION OF MOTION? (Y/N) ")
    c1 = input()
    if c1 =='Y' or c1 =='y':
        c= input("PLEASE ENTER YOUR CHOICE ")
        continue
    else:
        print("DO YOU WANT TO STOP? (Y/N) ")
        c2 = input()
        if c2=='Y' or c2=='y':
            break
        else:
            continue

pf1.stop()
pf2.stop()
pb1.stop()
pb2.stop()
GPIO.cleanup()  
