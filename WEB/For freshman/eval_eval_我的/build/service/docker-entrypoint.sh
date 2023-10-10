#!/bin/sh

# Get the user
user=$(ls /home)

# Check the environment variables for the flag and assign to INSERT_FLAG
if [ "$GZCTF_FLAG" ]; then
    export GZCTF_FLAG=no_FLAG
    GZCTF_FLAG=no_FLAG
fi

# 将FLAG写入文件 请根据需要修改
echo "XSCTF{YoU_F1NalLy_EvaLLL_m3!!}" | tee /flag

chmod 744 /flag

php-fpm &

nginx &

echo "Running..."

tail -F /dev/null