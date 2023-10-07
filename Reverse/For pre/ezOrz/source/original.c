#include <stdio.h>
#include <string.h>

int main() {
    char buf[] = "flag{V3ry_ez_1sn!t}";
    int len = strlen(buf);
    char v[] = "Jan_Ye_yyds_Orz";
    printf("%d\n",len);
    for (int i = 0; i < strlen(v); ++i) {
        char temp = v[i];
        temp = (temp << 4) + (temp >> 4);
        v[i] = temp;
    }
    for (int i = 0; i < len - 1; ++i) {
        buf[i] ^= buf[i + 1];
    }
    for (int i = 0; i < len; i++) {
        buf[i] ^= v[i % strlen(v)];
    }
    for(int i=0;i<len;++i){
        printf("%d,",buf[i]);
    }
    return 0;
}