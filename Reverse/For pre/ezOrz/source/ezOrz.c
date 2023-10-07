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

int just_xor(char *a, int len) {
    for (int i = 0; i < len - 1; ++i) {
        a[i] ^= a[i + 1];
    }
    return 0;
}

int main() {
    char buf[50];
    char enc[] = {-82, 27, -32, -23, -72, 51, -76, -100, -79, 124, 40, -48,
                  -102, 101, -70, -21, 67, -17, -120};
    //len == 19
    char v[] = "Jan_Ye_yyds_Orz";
    int v_len = strlen(v);
    printf("input your flag:");
    scanf("%s", buf);
    if (strlen(buf) != 19) {
        puts("sorry!");
        exit(0);
    }
    swap_bit4(v, v_len);
    just_xor(buf, 19);

    for (int i = 0; i < 19; i++) {
        buf[i] ^= v[i % strlen(v)];
    }
    /*for (int i = 0; i < 19; ++i) {
        printf("%d,", buf[i]);
    }*/
    for (int i = 0; i < 19; ++i) {
        if (buf[i] != enc[i]) {
            puts("Oh no!");
            return 0;
        }
    }
    // putchar('\n');
    puts("JAN star yyds!Orz!");
    return 0;
}