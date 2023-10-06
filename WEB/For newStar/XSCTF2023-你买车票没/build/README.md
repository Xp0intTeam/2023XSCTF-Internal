# 如何启动?
## 方式一
* cd build
* docker build -t "doubuyticket:Dockerfile" .
* docker run -d -p 40188:8080 doubuyticket:Dockerfile
## 方式二
* cd build
* docker-compose up -d
