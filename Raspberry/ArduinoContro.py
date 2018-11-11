#/home/pi/Projects/SharedFile

import serial, time
import RPi.GPIO as GPIO
import binascii

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD

GPIO.setup(13,GPIO.OUT)    #Ponemos el pin 21 como salida

p = GPIO.PWM(13,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo

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
   p.ChangeDutyCycle(duty)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda  
   #arduino.write('r')
   print duty
   time.sleep(2)  #pausa de medio segundo

  
  elif(data=='l' and duty > 5):
   duty=duty-0.1
   p.ChangeDutyCycle(duty)    #Enviamos un pulso del 4.5% para girar el servo h$ 
   #arduino.write('l') 
   print duty
   time.sleep(2)           #pausa de medio segundo
   
	 
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

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
 p.stop()                      #Detenemos el servo 
 GPIO.cleanup()    
 serial.Serial('/dev/ttyACM0', 115200).close()