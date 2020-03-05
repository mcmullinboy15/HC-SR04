
# https://www.youtube.com/watch?v=WgcNBjIJNYs

echo "Enableing ssh server"
sudo systemctl enable ssh

echo "starting something??  maybe ssh"
sudo systemctl start ssh

echo "maybe Enableing ssh server"
sudo mv /boot/boot_enable_ssh.rc /boot/boot.rc

echo "this could get you the ip address"
hostname -i or -I





echo "update password"
sudo passwd pi

