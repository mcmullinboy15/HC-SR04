SECONDS=0
echo "Running script_setup.sh"
. script_setup.sh

echo "Pulling new data"
git pull

echo "Setting up CronTab"
. _crontab.sh

echo "Running the sensor"
python3 exe_ver_1.0.py

sleep 3
duration=$SECONDS
echo "run.sh has been running for $(($duration / 60)) minutes and $(($duration % 60)) seconds."


# where am I going to put the git pull!
# I think I could use crontab

#I have determined I need to use crontab
# or maybe I need to have run.sh run once
# a day and then have exe_ver_1.0.py run
# for one day and stop.
