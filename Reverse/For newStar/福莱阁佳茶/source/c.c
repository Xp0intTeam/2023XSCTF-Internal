#include <stdio.h>
#include <string.h>

// XSCTF{Funny_h1d3_4nd_s33k?}
char flag[] = "]VFQC~Cpkk|Zm4a6Z1kaZv66n:x"; // 全局变量存储flag

void __attribute__((constructor)) init_array() {
    int i;

    // 加密flag
    for (i = 0; flag[i] != '\0'; i++) {
        flag[i] ^= 5;
    }
}

// XSCTF{Funny_h1d3_4nd_HId3!}
void __attribute__((destructor)) cleanup() {
    int i;
    int secret[5] = {0xd5,0x16,0x31,0xc8,0xe2};
    int ii = 0;

    // 修改flag的后半部分
    for (i = strlen(flag) - 6; i < strlen(flag) - 1; i++) {
        flag[i] += secret[ii++];
    }

    const char* encodedStr = "@bm#zlv#ejmg#wkf#eobd<";
    char decodedStr[30];

    int ij = 0;
    while (encodedStr[ij] != '\0') {
        decodedStr[ij] = encodedStr[ij] ^ 3; // 异或操作
        ij++;
    }
    decodedStr[ij] = '\0';

    fputs(decodedStr, stdout); // 输出解密后的字符串
}

int main() {
    printf("Hello!\nThis is the easiest reverse chall in the world!\nAnd, I am the kindest man in the world!\n");
    printf("Just wait for 114514 seconds and I will give you the flag!\n");
    printf("Good luck!\n");
    for (int i = 0; i < 114514; i++) {
        printf("Waiting for %d seconds...\n", 114514 - i);
        sleep(1);
    }
    return 0;
}
