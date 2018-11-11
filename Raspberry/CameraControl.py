#Servo camera control and Send message to arduino


import serial, time
import RPi.GPIO as GPIO
import binascii

GPIO.setmode(GPIO.BOARD)   

GPIO.setup(13,GPIO.OUT)   

p = GPIO.PWM(13,50)       

p.start(7.5)


arduino=serial.Serial('/dev/ttyACM0',115200)
time.sleep(2)
goback=0
duty=7

#file = open("/home/pi/Projects/SharedFile/sharedf.txt", "r")
#print file.read(5)
try:
 while(1):
  file = open("/home/pi/Projects/SharedFile/sharedf.txt", "r")
  data=file.read(1)
  file.close()
  #print data
  #print duty
  
  #arduino.write(data)
  if(data=='r' and duty < 10): #leer de fichero
   duty=duty+0.1
   p.ChangeDutyCycle(duty)
   print duty
   time.sleep(2)  

  
  elif(data=='l' and duty > 5):
   duty=duty-0.1
   p.ChangeDutyCycle(duty)
   print duty
   time.sleep(2)       
   
	 
  if(duty >= 7 and  duty <=8):
   arduino.write('m')  
  elif(duty <7.0 and duty >= 6.0):
   arduino.write('k')
  elif(duty <6.0 and duty >= 5.0):
   arduino.write('l')
  elif(duty >8.0 and duty <= 9):
   arduino.write('t')
  elif(duty >9.0 and duty <= 10):
   arduino.write('r')
   
  if(data=='m'):
	print "Step"

except KeyboardInterrupt:         #CONTROL+C 
 p.stop()                      
 GPIO.cleanup()    
 serial.Serial('/dev/ttyACM0', 115200).close()
