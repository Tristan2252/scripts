#! /bin/bash

USER="ubuntu"
HOSTS="$@"

ping_host() {
    ping -c 1 $1

    if [ $? -ne 0 ]; then 
        exit -1
    fi
}

for i in $HOSTS; do
    
    # check of host exists    
    ping_host $i

    # for every host in hosts run update and upgrade command
    ssh $USER@$i "sudo apt-get update && sudo apt-get upgrade -y"

    if [ $? != 0  ]; then 
        echo "ERROR: exited with non 0"
    fi
done 
