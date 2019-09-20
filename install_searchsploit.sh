#!/bin/bash

#command -v searchsploit
#command -v msfconsle

if [[ ! $(command -v searchsploit) ]]; then
	cd /opt
        wget https://raw.githubusercontent.com/offensive-security/exploitdb/master/searchsploit
	chmod +x /opt/searchsploit
	ln -s /opt/searchsploit /usr/bin/searchsploit
fi
