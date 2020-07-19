SECONDS=0
echo "\033[34m  Running script_setup.sh  \033[0m"
. script_setup.sh

echo "\033[34m  Pulling new data  \033[0m"
git pull

echo "\033[34m  Running the sensor  \033[0m"
python3 exe_ver_1.0.py

sleep 3
duration=$SECONDS
echo "\033[34m  run.sh has been running for $(($duration / 60)) minutes and $(($duration % 60)) seconds.  \033[0m"


# where am I going to put the git pull!
# I think I could use crontab

#I have determined I need to use crontab
# or maybe I need to have run.sh run once
# a day and then have exe_ver_1.0.py run
# for one day and stop.
