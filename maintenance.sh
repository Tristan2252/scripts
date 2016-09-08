#! /bin/bash

USER="ubuntu"
HOSTS="$@"

for i in $HOSTS; do
    ssh $USER@$i "sudo apt-get update && sudo apt-get upgrade -y"
done 
