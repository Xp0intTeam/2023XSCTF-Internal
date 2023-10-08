#!/bin/sh

echo $GZCTF_FLAG > /flag
export GZCTF_FLAG=""
#echo "flag{xxxxxx}" > /flag

cd /app && su www-data -c "node app.js"
