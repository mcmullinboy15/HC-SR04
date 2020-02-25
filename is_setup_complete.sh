#!/bin/sh

IFS=","
notline1=false
first_f1_is_setup_complete=false
setup_complete=false

while read -r f1 f3
do
        if [ "$f1" = 'setup_complete' ]
        then
            first_f1_is_setup_complete=true
        fi

        if  $notline1  &&  $first_f1_is_setup_complete
        then
            # What do I want to do with the value here. Maybe I'll add all
            #  this to script_setup.sh and then in here I'll change a value
            #  to True or False depending on if the value is 1 or -1
            if [ "$f1" = 1 ]
            then
              setup_complete=true
              echo $setup_complete
#            else
#              sed -i -e 's/-1/1/1' user_data.csv #> "user_data.csv"
            fi
        fi

        if  $notline1
        then
            notline1=false
        else
            notline1=true
        fi

done < user_data.csv

