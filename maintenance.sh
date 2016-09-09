#! /bin/bash

USER="ubuntu"
HOSTS="$@"

for i in $HOSTS; do

    # for every host in hosts run update and upgrade command
    ssh $USER@$i "sudo apt-get update && sudo apt-get upgrade -y"
    if [ $? != 0  ]; then 
        echo "ERROR: exited with non 0"
    fi
done 
