#!/bin/sh

IFS=","
line2=0
first_f1_is_setup_complete=False
setup_complete=False

while read f1 f2 f3
do
        if [ $f1 = 'setup_complete' ]
        then
            first_f1_is_setup_complete=True
        fi

        if [ $line2 = 1 ] && [ $first_f1_is_setup_complete ]
        then
            # What do I want to do with the value here. Maybe I'll add all
            #  this to script_setup.sh and then in here I'll change a value to
            #  True or False depending on if the value is 1 or -1
            if [ $f1 = 1 ]
            then
                setup_complete=True
            fi
        fi

        line2=1
done < user_data.csv

echo $setup_complete