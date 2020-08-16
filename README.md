# HC-SR04

Originally Created by `mcmullinboy15` and the Repository has been Transfered to `ezsaltdevenv`

## Code Created by me to connect a Raspberry Pi 3 B+ to the HC-SR04 ultrasonic sensor
    This project is made to email a user of the sensor at 8:00 o'clock everyday if the sensors detects a reading of 15% or less
    
## This Project has moved to use a D1 Mini, an Arduino capable device to work with the HC-SR04 sensor, and is no longer in use
    
### Setup and run Sam.sh:

    Connecting to the USB:
    
        * sudo mkdir /media/usb
        * sudo chown -R pi:pi /media/usb
        * sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi
        
    Entering the USB:
    
        * cd /media/usb
    
    Running Sam.sh:
    
        * source Sam.sh
        
### Running the Sensor:

    Sam.sh should have put you in the correct folder of the downloaded code
    
    If your path is ~/Documents/EZ_Salt/HC-SR04/ continue but if not go there.
    
    Now Run [ run.sh ] by doing {  . run.sh  }
    
    If it is the first time running run.sh it will setup the and install all of the nessecary packages and libraries to make this project work.
    
    If it is not the first time:
        - The setup and imports will be skipped. 
        - The program will call `git pull` to download any updates
        - Then runs the file `exe_ver_1.0.py` which runs the sensor loop
        
        
if sensor does not exist in server database the database will give it a vaild 25 digit id and will use that to identify the Sensor.
