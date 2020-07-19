datapath="$HOME/Documents/EZ_Salt/HC-SR04/user_data.csv"
if [  -f "$datapath"  ]
then
  echo "\033[34m  $datapath exists  \033[0m"
else
  echo 'setup_complete,email,name,phone_number,username,password,home_address,WIFI_username,WIFI_password,size_of_container,single_noti_1,single_noti_2,single_noti_3,daily_noti,send_daily,time_of_day
-1,"ezsalt.dev.env@gmail.com","Andrew","8018973786","ezsalt","ezsalt98","3869 w 9380 s, West Jordan, Ut 84088","oldfarm-5G","OldFarmpa$$",121.5,50,30,-1,15,TRUE,8' > $datapath
fi
