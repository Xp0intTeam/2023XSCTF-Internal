- **题目名称：** babyWechat
- **题目类型：** Misc
- **题目难度：**困难
- **出题人：** =w=, i_corner
- **考点：**

1. 微信取证

- **描述：** 狗遛狗舞和狗食之前在微信讨论该如何出这次决赛的题目。某天夜里，狗食在冰天1V1后忘记开电脑锁屏就去找女人了，他的舍友拉菲趁机偷看了狗食的电脑，遗憾的是狗食并没有登陆微信，拉菲只好把微信目录拷了一份出来，你能帮助拉菲拿到flag嘛？
- **flag：** XSCTF{plz_give_me_star_in_https://github.com/i-Corner/WX-forensics}
- **Writeup：**

还原FileStorage/MsgAttach里的聊天图片，从图片里获取AES key，并用其解开MSG0.db获得聊天记录

利用聊天记录中拿到的口令解开FileStorage/file中的flag.rar，得到flag.txt