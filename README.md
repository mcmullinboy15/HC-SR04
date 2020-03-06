# HC-SR04

Originally Created by `mcmullinboy15` and the Repository has been Transfered to `ezsaltdevenv`


Setup and run Sam.sh:

    Connecting to the USB:
    
        * sudo mkdir /media/usb
        * sudo chown -R pi:pi /media/usb
        * sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi
        
    Entering the USB:
    
        * cd /media/usb
    
    Running Sam.sh:
    
        * source Sam.sh
        
Running the Sensor:

    Sam.sh should have put you in the correct folder of the downloaded code
    
    If your path is ~/Documents/EZ_Salt/HC-SR04/ continue but if not go there.
    
    Now Run [ run.sh ] by doing {  . run.sh  }
    
    If it is the first time running run.sh it will setup the and install all of the nessecary packages and libraries to make this project work.
    
    If it is not the first time:
        - The setup and imports will be skipped. 
        - The program will call `git pull` to download any updates
        - Then runs the file `exe_ver_1.0.py` which runs the sensor loop
        
        
exists
    vaild 25 id
    
manual idea
    get email to send as id/create Id
    
send grid
    