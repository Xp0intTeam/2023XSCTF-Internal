- **题目名称：** Oursecret_for_zero
- **题目类型：** MISC（23）
- **题目难度：** 中等
- **出题人：** itSssm3
- **考点：**

1. 零宽隐写 + oursecret隐写

- **描述：** Why the width is ZERO? It's OURSECRET
- **flag：** XSCTF{WeLc0m3_to_s7eg_w0rld}
- **Writeup：** 


```
先是zip伪加密 改09为00
图片尾部有base64转化后是提示用steghide
图片exif信息有十六进制转化后是passwd
steghide解密后就是flag
```