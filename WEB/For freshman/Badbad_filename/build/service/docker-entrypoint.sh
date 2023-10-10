#!/bin/sh

# Get the user
user=$(ls /home)

# Check the environment variables for the flag and assign to INSERT_FLAG
if [ "$GZCTF_FLAG" ]; then
    export GZCTF_FLAG=no_FLAG
    GZCTF_FLAG=no_FLAG
fi

php-fpm &

nginx &

echo "Running..."

tail -F /dev/null