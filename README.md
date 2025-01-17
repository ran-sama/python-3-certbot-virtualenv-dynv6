# python3-certbot-virtualenv-dynv6
Certbot virtualenv, bash hooks and python 3 script to issue letsencrypt wildcard certs for dynv6 domains.  
First issuance nominal:  
![alt text](https://raw.githubusercontent.com/ran-sama/python-3-certbot-virtualenv-dynv6/refs/heads/master/images/issuance_successful.png)  
Renewal nominal:  
![alt text](https://raw.githubusercontent.com/ran-sama/python-3-certbot-virtualenv-dynv6/refs/heads/master/images/renew_successful.png)  

Using a Debian headless server is very enjoyable, until you run into the realization how outdated the stable packages are. Luckily if the package is part of the Python Package Index (PyPI) the mitigation for this is almost trivial, refer to these websites:
```
https://pypi.org/
https://certbot.eff.org/
https://virtualenv.pypa.io/en/latest/
https://www.rust-lang.org/tools/install
```
The scope of this repo will focus on setting up a virtualenv, compiling the Python cryptography package inside it, setting up certbot and hooks for the DNS and domain provider dynv6 with the goal to issue wildcard certs for a domain.

We will start with dependencies:
```
sudo apt install python3-virtualenv
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
In our home dir we setup a directory to store our virtual environments, this dir can house as many environments as we currently see fit:
```
mkdir certbotenv
cd certbotenv
virtualenv certbotenv_1 --download
source certbotenv_1/bin/activate
```
You should see that your terminal session is prefixed now with an indicator of the virtualenv:
```
(certbotenv_1) ran@odroidhc1:~/certbotenv$
```
We can start installing into this virtualenv now without breaking system packages, as virtualizing (rather an isolated container) protects our *NIX OS:
```
pip3 install certbot
```
Regularly check if any wheel or package is outdated, so it can be built and upgraded.  
```
pip3 list
pip3 list --outdated
certbot --version
```
It is up-to-date:
```
certbot 3.1.0
```
We leave the virtualenv:
```
(certbotenv_1) ran@odroidhc1:~/certbotenv$ deactivate
ran@odroidhc1:~/certbotenv$
```
That's really all to it! If you don't want to sign-in you can also call it from outside the virtualenv's console:
```
/home/ran/certbotenv/certbotenv_1/bin/python /home/ran/certbotenv/certbotenv_1/bin/certbot certonly --config /home/ran/keys/cli.ini
```
As you see, you have local copies or links to binaries that are isolated from the OS itself. It is very elegant and simple once you familiarized yourself with it. If you set-up a ```cli.ini``` for certbot, you can let the certbot inside the virtualenv know how you would like to renew your domain and with what parameters.

Don't pass all parameters in a one-liner as many people suggest. That just brings pain. Static files with your settings are portable across installations and can be easily rsynced if needed.

## zone_records.json
Example how to populate your dynv6 records for wildcard certs to work.  
```
REST API:
Two CAA records for example.com and *.example.com
Two A-records for subdomain1.example.com and subdomain2.example.com
```
Notice:
```
Update API:
Main A-record for example.com is NOT included, as it is set through the default update API.
```

## certfox.py
A Python 3 script to renew letsencrypt certs based on when they expire, can be used as helper if you don't like the systemd timer of certbot. Which I particularly did not want to use because the virtualenv is on a very specific path.  

Overengineered but with nice features:

* checks if a cert needs to be renewed
* can configure minimum lifetime (default 14 days)
* checking is done locally and doesn't waste quota
* easy to add extra features

```
chmod +x certfox.py
sudo crontab -e -u ran
30 2 * * * python3 /home/ran/certfox.py >> /home/ran/certfox_error.log
```

Use with:

https://github.com/ran-sama/systemd-service-examples  
https://github.com/ran-sama/python3-https-tls1-3-microserver  


## License
Licensed under the WTFPL license.
