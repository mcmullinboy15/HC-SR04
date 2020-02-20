#!/bin/bash

# Most Help
# https://www.golinuxcloud.com/create-schedule-cron-job-shell-script-linux/


   if [ `id -u` -ne 0 ]; then
      echo "This script can be executed only as root, Exiting.."
      exit 1
   fi

case "$1" in
   install|update)

	CRON_FILE="/var/spool/cron/pi"

#        touch $CRON_FILE
#        /usr/bin/crontab $CRON_FILE
#        echo "0 0 * * * rm -f /tmp/pi/*" >> $CRON_FILE
#        crontab -u pi -l

	if [ ! -f $CRON_FILE ]; then
	   echo "cron file for root doesnot exist, creating.."
	   touch $CRON_FILE
	   /usr/bin/crontab $CRON_FILE
	fi

	# Method 1
	grep -qi "cleanup_script" $CRON_FILE
	if [ $? != 0 ]; then
	   echo "Updating cron job for cleaning temporary files"
           /bin/echo "0 0 * * * rm -f /home/deepak/cleanup_script.sh" >> $CRON_FILE
	fi

	# Method 2
#	grep -qi "cleanup_script" $CRON_FILE
#	if [ $? != 0 ]; then
#	   echo "Updating cron job for cleaning temporary files"
#	   crontab -u deepak -l >/tmp/crontab
 #          /bin/echo "0 0 * * * rm -f /home/deepak/cleanup_script.sh" >> /tmp/crontab
#	   crontab -u deepak /tmp/crontab
#	fi

	;;
	
	*)
	
	echo "Usage: $0 {install|update}"
#	exit 1
    ;;

#esac
