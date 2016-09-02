#!/bin/bash

DATE=$(date +%a-%b-%d)
BACKUP_SERVER="Crimson-Node-1"
BACKUP=/mnt/Backup-Drive/Backups
BACKUP_DIRS="/etc /file-pool"



if [ $HOSTNAME == $BACKUP_SERVER ]; then
    tar czf $BACKUP/Node1/ARCHIVE/$DATE.tar.gz $BACKUP/Node1/etc $BACKUP/Node1/file-pool

    for i in $BACKUP_DIRS; do
        rsync -av $i $BACKUP/Node1/
    done
else
    rsync -avzhe ssh $i server@Node1:$BACKUP/$HOSTNAME/$i
fi

