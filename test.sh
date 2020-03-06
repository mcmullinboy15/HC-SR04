#!/bin/bash



if [ "$(. is_setup_complete.sh)" = 'true' ]
then
  echo "Skipping Setup because its Already Done"
else
  echo "updating raspberry pi"
fi




desired_python_version="Python 3.7"
if [[ "$( python3 --version )" =~ $desired_python_version ]]
then
  echo "PYTHON Already exists"
else
  echo "upgrading python"
fi


start=$(date "+%S")
sleep 20
end=$(date "+%S")
echo $($end-$start)   #   /Users/amcmullin/Documents/EZ_Salt/HC-SR04/test.sh: line 20: 52-32: command not found




echo -ne '#####                     (33%)\r'
sleep 1
echo -ne '#############             (66%)\r'
sleep 1
echo -ne '#######################   (100%)\r'
echo -ne '\n'



i=1
sp="/-\|"
echo -n ' '
while true
do
    printf "\b${sp:i++%${#sp}:1}"
    sleep 1
done


