- **题目名称：** Mommy_Kafka
- **题目类型：** MISC（23）
- **题目难度：** 容易
- **出题人：** itSssm3
- **考点：**

1. 伪加密 + steghide

- **描述：** 卡芙卡妈妈又给我传东西啦❤ 但是这怎么打不开？
- **flag：** XSCTF{M0mmy_L0v3_Me_th3_mo5t}
- **Writeup：** 


```
先是zip伪加密 改09为00
图片尾部有base64转化后是提示用steghide
图片exif信息有十六进制转化后是passwd
steghide解密后就是flag
```