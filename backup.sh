#!/bin/bash

# Date used for archive tar name
DATE=$(date +%a-%b-%d)

# Backup host value to test if script needs to use remote commands
BACKUP_HOST="Crimson-Node-1"

# Dir to backup to for local and remote 
BACKUP_DIR=/mnt/Backup-Drive/Backups

# Files to backup
BACKUP="/etc $@"


# test for backup host
if [ $HOSTNAME == $BACKUP_HOST ]; then
    
    # remove old archives
    rm -v /mnt/Backup-Drive/ARCHIVE/*

    # Archive all files in BACKUP_DIR
    for i in $(ls $BACKUP_DIR); do
        tar czf /mnt/Backup-Drive/ARCHIVE/$i-$DATE.tar.gz $BACKUP_DIR/$i/
    done

    # Backup host with rsync
    for i in $BACKUP; do
        rsync -av $i $BACKUP_DIR/$HOSTNAME/
    done

# if remote host run below code block
else
    for i in $BACKUP; do

        # make dir if it doesnt exist
        ssh server@node1 "mkdir -p $BACKUP_DIR/$HOSTNAME$i"
        rsync -arvzhe ssh --relative $i server@Node1:$BACKUP_DIR/$HOSTNAME$i
    done
fi

