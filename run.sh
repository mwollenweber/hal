#!/usr/bin/env bash

set -e
os=$(uname -s)

if [[ $os == "Darwin" ]]; then
    readlink_path=$(which greadlink)
else
    readlink_path=$(which readlink)
fi

script_directory=$(dirname $(${readlink_path} -f $BASH_SOURCE))

# Source all environment variables
environment="${script_directory}/hal.rc"
if [ -f $environment ]; then
    source $environment
fi


python="${script_directory}/env/bin/python"
hal="${script_directory}/hal.py"
exec $python $hal