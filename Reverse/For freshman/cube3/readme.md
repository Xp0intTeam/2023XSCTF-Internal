# 所属方向:RE

# 题目描述

1.你玩过三阶魔方吗,你能看懂R U R' U'这样的公式吗,这里有4个魔方等你来还原

2.公式(步骤)格式例如R U' R U R U R U' R' U' R2' <回车>,每步操作用空格分开,逆时针加上'字符

3.flag格式为`xsctf{formula}`,其中`formula`为4个魔方的还原步骤依次连在一起,去掉空格,取其md5

4.本题在Ubuntu22下编译,请不要使用ubuntu18

5.hint:

​	上1,下2,前3,后4,左5,右6

<img src="https://typora-blogs-pic.oss-cn-beijing.aliyuncs.com/img/image-20231004151716407.png" alt="image-20231004151716407" style="zoom:33%;" />	

<img src="https://typora-blogs-pic.oss-cn-beijing.aliyuncs.com/img/image-20231004151928030.png" alt="image-20231004151928030" style="zoom:33%;" />	

​	<img src="https://typora-blogs-pic.oss-cn-beijing.aliyuncs.com/img/image-20231004151939895.png" alt="image-20231004151939895" style="zoom:33%;" />

# 附件

cube3

# WP

分析代码可知该函数中的v4数组存有4个魔方的打乱公式,题目要求按照打乱公式反向转动来还原魔方,所以要将该数组的有效部分提取出来

![image-20230914170502688](https://typora-blogs-pic.oss-cn-beijing.aliyuncs.com/img/image-20230914170502688.png)

根据分析可得6*4==24种转动操作映射到以下enum:

```c
enum rotary {
    U, U_, U2, U2_,
    D, D_, D2, D2_,
    F, F_, F2, F2_,
    B, B_, B2, B2_,
    L, L_, L2, L2_,
    R, R_, R2, R2_,
    END
};
```

四个公式也就是:

```c
23 3 4 8 18 9 12 18 13 7 20 11 13 22 14 6 8 18 4 14
6 22 7 13 1 4 2 8 22 19 6 10 19 21 19 7 17 8 7 12
5 15 19 2 5 17 12 9 7 12 18 5 12 3 11 14 5 18 6 22
20 12 7 21 14 23 19 13 3 18 7 3 22 0 8 1 18 7 18 11
```

那么想要做一个逆序,就要先转换到实际的公式,转换脚本如下:

```c
#include <stdio.h>
#include <string.h>
int main() {
    char rot[][4] {
        "U", "U'", "U2", "U2'",
        "D", "D'", "D2", "D2'",
        "F", "F'", "F2", "F2'",
        "B", "B'", "B2", "B2'",
        "L", "L'", "L2", "L2'",
        "R", "R'", "R2", "R2'",
    };
    int nums[100], idx = 0;
    while (1) {
        scanf("%d", &nums[idx++]);
        if (nums[idx - 1] == -100)
            break;
    }
    idx--;
    for (int i = 0; i < idx; ++i) {
        printf("%s ", rot[nums[i]]);
        if ((i + 1) % 20 == 0)
            putchar('\n');
    }
    return 0;
}
```

输入即为:

```c
23 3 4 8 18 9 12 18 13 7 20 11 13 22 14 6 8 18 4 14
6 22 7 13 1 4 2 8 22 19 6 10 19 21 19 7 17 8 7 12
5 15 19 2 5 17 12 9 7 12 18 5 12 3 11 14 5 18 6 22
20 12 7 21 14 23 19 13 3 18 7 3 22 0 8 1 18 7 18 11
-100
```

输出的结果就是4个打乱公式,如下:

```c
R2' U2' D F L2 F' B L2 B' D2' R F2' B' R2 B2 D2 F L2 D B2
D2 R2 D2' B' U' D U2 F R2 L2' D2 F2 L2' R' L2' D2' L' F D2' B
D' B2' L2' U2 D' L' B F' D2' B L2 D' B U2' F2' B2 D' L2 D2 R2
R B D2' R' B2 R2' L2' B' U2' L2 D2' U2' R2 U F U' L2 D2' L2 F2'
```

根据常识我们把他们依次反过来转,也就是:

`R ---> R'    U' --->U    D2 ---> D2'    F2' ---> F2`

以此类推,因为公式不长,就直接肉眼一个个转换,结果为:

```c
B2' D' L2' F' D2' B2' R2' B F2 R' D2 B L2' B' F L2' F' D' U2 R2
B' D2 F' L D2 L2 R L2 F2' D2' L2 R2' F' U2' D' U B D2 R2' D2'
R2' D2' L2' D B2' F2 U2 B' D L2' B' D2 F B' L D U2' L2 B2 D
F2 L2' D2 L2' U F' U' R2' U2 D2 L2' U2 B L2 R2 B2' R D2 B' R'
```

去掉空格和换行,然后进行md5即得flag:

```c
// B2'D'L2'F'D2'B2'R2'BF2R'D2BL2'B'FL2'F'D'U2R2B'D2F'LD2L2RL2F2'D2'L2R2'F'U2'D'UBD2R2'D2'R2'D2'L2'DB2'F2U2B'DL2'B'D2FB'LDU2'L2B2DF2L2'D2L2'UF'U'R2'U2D2L2'U2BL2R2B2'RD2B'R'
    
//md5结果
//0a15a3168e6bf08df8178186312b0396

//flag即为
// xsctf{0a15a3168e6bf08df8178186312b0396}
```

