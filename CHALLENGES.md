# 初赛题目列表

* 序号从 0 开始
* 名称和描述在平台上展示给选手
* 至少一个 Hint

## 1. MISC:

| 序号 | 名称 | 难度 | 考点 | 描述 | flag | 出题人 | Hint | 备注 |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|0|word心|中等|word隐写|啊~有东西跑进来了|xsctf{Y0u_g07_h@lf_my_h3ar7_g1v3_y0u_an0ther_h@lf}|pANz0e|word隐写||
|1| Set-uid | 中等 | suid提权 | ssh noweb/123456 IP:10722(替换成实际IP)，flag in /root/flag | flag{sCnu8t@ixin9s10thx1ng} | Fxizenta | 1.only zsh 2.noweb  ALL=(root) /bin/rm, /bin/ln ||


## 2. WEB:

| 序号 | 名称 | 难度 | 考点 | 描述 | flag | 出题人 | Hint | 备注 |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|  0   |    ez_game     | 简单 |    |           听说ctfer打到-1000分就能通关游戏了！            |       flag{D0_w311_ctfer\_!\_1s_it_a_g00d_g@me\_?}       |  pANz0e  |                    | 热身赛 |
|   1  |     ez_RCE     | 简单 |  命令执行    |                 哎呀，空格都没了，呜呜呜~                 | falg{Rc3_15_th3_m0st_Intere5t1ng_vu1nerability\_!\_!} |  pANz0e  |      替代空格      | 热身赛 |
|   2  |     ezphp      | 简单 |  php伪协议  |                 我得想想怎么才能取而代之                  |            flag{phP_lS_th9_be5T_l4ngUa9e}             | Fxizenta |    php://input     | 热身赛 |
|   3  |    easy_sql    | 中等 |  bool盲注   | 嘉然，为了你我要打ctf！！！咦？这里这么注入不进去呢？奇怪 |         flag{Gu@ng2hU_j1arAn_Dundun_ji3Chan9}         | Fxizenta | 登录功能不是注入点 | 热身赛 |
|4|隐秘的backdoor|中等|php版本后门|后门给你了，来吧|flag{B@ck_do0r\_!\_B4ck_d0or_!}|pANz0e|php8.1||
|  5  |  canyoupassit  | 中等 |   md5碰撞   |               Do you really know about md5?               |                       flag{y0\|nDeedReA11yk$nwAb0uTMD5!~_~^_^} |                    | md5碰撞 ||
|6| Hacker | 容易 | JavaScript | Admin的站点被挂黑页了怎么办，重要的东西都被删了TuT | xsctf{Y0u_can_no7_f1nd_m3\_?} | pANz0e | 得想个办法让代码停止 ||
|7| reallyExpensive | 简单 |  | 签到题，flag真的不贵 | flag{^==^Y0uG@t$(t]$[r)^u^(e)-F10g!^\<>^} |  | flag不仅白送还倒贴 ||
|8| kk园区审核员 | 简单 | xss | ... | xsctf{Y0u_succ3s5ful1y_x55_m3} | pANz0e | 你能不能拿到我的美味曲奇的？ ||
|9| java_checkin | 困难 | java反序列化 | 听说如今Web是Java的天下，于是菜鸡写了个非常简单的java程序，结果漏洞百出，估计要被打烂了。 | XSCTF{J@va_1s_v@3y_Imp03tAnt!!!!!!!!} | ABU |  ||
|10|ezgame|容易|f12|是男人就拿到1000000分！|flag{basju_D0G006706_iajdisaia}|Fxizenta|改分数||
|11| shabby_website | 中等 | 原型链污染 ssti | 快来尝试一下简单的代码审计，代码量很少，毕竟出题人连前端都懒得写。 | dynamic flag | Rieß | 可以尝试在本地对源码npm install一下看看有什么漏洞 ||
|12| upload_quick | 中等 | 文件上传 条件竞争 | newnew的逻辑总是颠三倒四，令人困惑，milktea经常以飞快的速度在不经意间看到newnew的秘密 | dynamic flag | fru1ts |  ||

## 3. Reverse:

| 序号 | 名称 | 难度 | 考点 | 描述 | flag | 出题人 | Hint | 备注 |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|0|ezAPK|简单|随机数模拟|你懂KT吗？|flag{43648c93-bb042eb50bb4-a73a-3b5e-aa52}|y9nhjy|随机数模拟||

## 4. Crypto:

| 序号 | 名称 | 难度 | 考点 | 描述 | flag | 出题人 | Hint | 备注 |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|0| ezDES | 简单 | des | 简化化化化化化化化的DES加密 | XSCTF{6b2d76d8-a09c-1f80-15c5-039a8f1c361c} | LTZ | 1）对称密码的特点  2）UUID格式 ||
|1| Fermat | 简单 | 费马小定理 | 简单的RSA加密 | XSCTF{F3rm4t_15_b453_0f_numb3r_th30ry} | LTZ | 注意类型一致 ||
|2| logging | 简单 | DLP | 载入中。。 | xsctf{Eiden_rLn9_m@ke_m3_hap1xiA} | modi | 1）sagemath解DLP  2）discrete_log ||
|3| RSA | 简单 | rsa | 小明掌握了RSA加密算法，但不知道如何获取关键秘钥，你能帮帮他吗？ | XSCTF{yafu_is_strong!} | LTZ | 1）直接分解大素数  2）yafu ||


## 5. PWN:

| 序号 | 名称 | 难度 | 考点 | 描述 | flag | 出题人 | Hint | 备注 |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|0|ret2text|简单|ret2text|checkin|XSCTF{Check1n_xv6_pwn_sooooo_easy}|133NSON||热身赛|
