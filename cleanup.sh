#!/usr/bin/env sh
echo $CERTBOT_DOMAIN
echo $CERTBOT_VALIDATION
ssh -i /home/ran/.ssh/dynv6 api@dynv6.com hosts $CERTBOT_DOMAIN records del _acme-challenge txt
sleep 10
exit 0
