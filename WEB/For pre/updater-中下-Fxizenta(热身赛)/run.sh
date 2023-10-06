#!/bin/bash

docker build . -t web_updater:latest

docker run -d \
   --restart unless-stopped \
   -p 10980:80 \
   --cap-drop all \
   --cap-add NET_BIND_SERVICE \
   --security-opt=no-new-privileges \
   --ulimit nproc=20 \
   --ulimit nofile=50 web_updater:latest

