echo "Running script_setup.sh"
source script_setup.sh

echo "Running the sensor"
python3 exe_ver_1.0.py




# where am I going to put the git pull!
# I think I could use crontab

#I have determined I need to use crontab
# or maybe I need to have run.sh run once
# a day and then have exe_ver_1.0.py run
# for one day and stop.