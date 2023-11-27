/etc/systemd/system/buptnet_autologin.service

systemctl enable --now buptnet_autologin.service
systemctl status buptnet_autologin.service
systemctl disable --now buptnet_autologin.service
