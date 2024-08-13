#!/usr/bin/python3
# -*- coding: utf-8 -*-
import ssl, json, datetime, subprocess

minimum_lifetime = 14
cer_iso_time = r'%b %d %H:%M:%S %Y %Z'

cert_1 = "/home/ran/keys/fullchain.pem"
command_1 = "/home/ran/certbotenv/certbotenv_1/bin/python /home/ran/certbotenv/certbotenv_1/bin/certbot certonly --config /home/ran/keys/cli.ini"
timestamp_1 = str(datetime.datetime.utcnow()) + " UTC\n"

def cert_fox_sniff(domain, renew):
    load_cert = ssl._ssl._test_decode_cert(domain)
    j = json.loads(json.dumps(load_cert))
    time_left = datetime.datetime.strptime(j['notAfter'], cer_iso_time)
    days_left = time_left - datetime.datetime.utcnow()
    finaldays = days_left < datetime.timedelta(days=minimum_lifetime)
    if (finaldays == True):
        process = subprocess.Popen(renew.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        output, error = process.communicate()
        #print(output)
        print(timestamp_1, error)
    elif (finaldays == False):
        pass
    else:
        pass

cert_fox_sniff(cert_1, command_1)
