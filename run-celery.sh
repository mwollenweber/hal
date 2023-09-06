#!/bin/bash

set -e

# For OSX development
if [[ `uname` == "Darwin" ]]; then
    script_directory=$(dirname "$0")
fi

# For Linux production deployment
if [[ `uname` == "Linux" ]]; then
    script_directory=$(dirname $(readlink -f $BASH_SOURCE))
fi

if [ -e $script_directory/hal.rc ]
then
	source $script_directory/hal.rc
else
	echo "WARN: $script_directory/hal.rc does not exist."
fi

exec $script_directory/env/bin/celery -A tasks worker  -Ofair  --purge  --max-tasks-per-child=16 --pidfile=/tmp/hal-celery.pid  --loglevel=INFO -n hal_engine_workers
