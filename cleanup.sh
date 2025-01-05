#!/usr/bin/env sh
echo $CERTBOT_DOMAIN
echo $CERTBOT_VALIDATION
ssh api@dynv6.com hosts $CERTBOT_DOMAIN records del _acme-challenge txt data $CERTBOT_VALIDATION
sleep 9
exit 0
