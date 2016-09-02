#!/bin/bash

DATE=$(date +%a-%b-%d)
NODE1_BACKUP=/mnt/Backup-Drive/Backups/Node1
BACKUP_DIRS="/etc /file-pool"

tar czf $NODE1_BACKUP/ARCHIVE/$DATE.tar.gz $NODE1_BACKUP/etc $NODE1_BACKUP/file-pool

for i in $BACKUP_DIRS; do
    rsync -av $i $NODE1_BACKUP/
done

