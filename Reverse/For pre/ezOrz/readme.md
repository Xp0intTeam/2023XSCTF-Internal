# 所属方向:RE

# 题目描述

vaaaarrrry ez re!

Orz Orz Orz

# 附件

ezOrz

# WP

程序有一个加壳,先使用UPX去壳.

使用IDA分析可得,题目中有一个密钥,要用其进行加密.

但是密钥经过了处理,将密钥的每个字节进行了高4位和低4位的交换.然后,将输入的flag从前向后对相邻两个字节进行异或变换.

最后使用处理过的密钥对同样处理过的flag进行循环异或,得到加密的数据.

将得到的数据和程序中的一个数组进行比较,可知这个数组就是密文.

需要注意的是,密文可能是在程序中赋值的,而且不是按字符串进行赋值,需要进行动态调试,然后提取出来.

按顺序反过来编写代码即可,代码如下:

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int swap_bit4(char *a, int len) {
    for (int i = 0; i < len; ++i) {
        char temp = a[i];
        temp = (temp << 4) + (temp >> 4);
        a[i] = temp;
    }
    return 0;
}

int my_xor(char *a, int len) {
    for (int i = len - 2; i >= 0; --i) {
        a[i] ^= a[i + 1];
    }
    return 0;
}

int main() {
    //buf需要动态调试从IDA导出
    char buf[50] = {
            174,  27, 224, 233, 184,  51, 180, 156, 177, 124,
            40, 208, 154, 101, 186, 235,  67, 239, 136,  12,
            46,  86,   0
    };
    for(int i=0;i<19;++i)
        printf("%d ",buf[i]);
    char v[] = "Jan_Ye_yyds_Orz";
    int len = 19;
    swap_bit4(v, 15);

    for (int i = 0; i < 19; i++) {
        buf[i] ^= v[i % strlen(v)];
    }
    my_xor(buf, 19);

    for (int i = 0; i < 19; ++i) {
        putchar(buf[i]);
    }
    return 0;
}
```


flag{V3ry_ez_1sn!t}
