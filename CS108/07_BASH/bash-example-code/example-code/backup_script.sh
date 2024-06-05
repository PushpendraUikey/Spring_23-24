#!/bin/bash

# check if you have entered exactly two arguments
if [ $# -ne 2 ]; then
	echo "Usage: backup_scipt.sh <source_directory> <destination_directory>"
 	echo "Please try again"
	exit 1
fi

# check to see if rsync is installed.
if ! command -v rsync > /dev/null 2/&1
then
	echo "This script requires rsync to be installed."
	echo "Please use your distribution's package manager to install it and try again."
	exit 2
fi

# Capture current date and store it in the format YYYY-MM-DD
current_date=$(date +%Y-%m-%d)

rsync_options="-avb --backup-dir $2/$current_date --delete --dry-run"
#a=source directory, b=target directory, v is for verbose flag
# here --dry-run is to simulate what will be going to run but is not actually running

$(which rsync) $rsync_options $1 $2/current >> backup_$current_date.log

