#!/bin/bash
# run git pull on repo to make sure it is up 
# to date and then run ansible to take care 
# of the rest. NOTE: this file should be ln'ed
# to cron.daily to run daily...

# make sure repo is up to date
git pull

# run ansible
ansible-playbook ansible/manage.yml 
