#Script to mount filesystem from another machine 
#use: sshfs user@domain:/remote/directory/ /local/directory/

sshfs pi@192.168.1.102://home/pi/Projects/SharedFile/ /home/nvidia/Projects/SharedFile/ 

