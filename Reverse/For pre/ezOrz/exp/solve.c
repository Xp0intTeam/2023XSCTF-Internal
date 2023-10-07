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