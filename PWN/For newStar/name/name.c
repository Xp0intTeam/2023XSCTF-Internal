#include<stdio.h>
#include <string.h>
#include <stdlib.h>

void shuffle(char *s){
    int length = strlen(s);
    for(int i = 0; i <= 100; ++i) {
        int a = rand() % length;
        int b = rand() % length;
        if(a == b) continue;
        s[a] = s[a] ^ s[b];
        s[b] = s[a] ^ s[b];
        s[a] = s[a] ^ s[b];
    }
}

int main() {
    setbuf(stdin, 0);    
    setbuf(stderr, 0);    
    setbuf(stdout, 0);
    int fd = open("./flag");
    size_t tt = time(0);
    srand(tt);
    int tmp = rand() % 0x100;
    char *p = malloc(tmp);
    read(fd, p, 0x20);
    int len = strlen(p);
    shuffle(p);
    free(p);
    printf("Flag(%d) was FREE!!!\n", len);
    int name_length;
    printf("Name length: ");
    scanf("%d", &name_length);
    p = malloc(name_length);
    printf("Name: ");
    read(0, p, name_length);
    printf("Hi %s, Did you see the Flag?\n", p);
    return 0;
}