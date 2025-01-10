#!/usr/bin/env sh
cp /home/ran/.certbot/config/live/example.com/fullchain.pem /home/ran/keys/fullchain.pem
cp /home/ran/.certbot/config/live/example.com/privkey.pem /home/ran/keys/privkey.pem
sudo systemctl restart fox1.service
sudo systemctl restart fox2.service
sudo systemctl restart fox3.service
sudo systemctl restart fox4.service
sudo systemctl restart fox6.service
sudo systemctl restart fox7.service
sudo systemctl restart unbound.service
sudo systemctl restart murmur-new.service
#sudo rm /etc/systemd/system/timers.target.wants/certbot.timer
sudo systemctl daemon-reload
exit 0
