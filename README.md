# HC-SR04

Originally Created by `mcmullinboy15` and the Repository has been Transfered to `ezsaltdevenv`


Setup and run Sam.sh:

    Connecting to the USB:
    
        sudo mkdir /media/usb
        sudo chown -R pi:pi /media/usb
        sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi
        
    Entering the USB:
    
        cd /media/usb
    
    Running Sam.sh:
    
        source Sam.sh
        
Running the Sensor:

    Sam.sh should have put you in the correct folder of the 
    downloaded code
    
    If your path is ~/Documents/EZ_Salt/HC-SR04/ you are able
    to run the file exe_ver_1.0.py. 
    If not go there.  
    
    Now Run [run.sh] by doing {. run.sh}
    
    if first time...
    
    or...
    