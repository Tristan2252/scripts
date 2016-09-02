# Scripts File

This repo contains scripts that i commonly use across servers such as backup
scripts and mounting scripts.  

_______________________________________________________________________________

##backup.sh:  

Script that can be placed on a server and configured to backup to a host as well
as backup the host itself. For example if Node1 is the host of the backup drive,
Node1 can set to the `$BACKUP_HOST` variable. If the script tests the hostname
not to be equal to `$BACKUP_HOST` then it runs `rsync` over ssh to the host
backup directory. If the script tests that `$BACKUP_HOST` is equal then the
script backs up the host to the backup directory.  

By default the only directory set to backup is `/etc/`. If other directories
need to be backed up they can be entered as arguments for `backup.sh`.  

`backup.sh` also makes an archive of the backed up folders and stores it as a
tar file titled with the date.  

_______________________________________________________________________________

##nfs_mount:

This script is used to mount an nfs share or bring up the host if it is down. It
is a python script that calls bash command based on the status of the nfs host.
If the host is down `etherwake` is used to bring up the host via `wake on lan`.
After this is done the script waits till the host is up by pinging it and then
waiting 10s for a retry. Once the host is up and pingable, the script runs the
nfs mount command.
