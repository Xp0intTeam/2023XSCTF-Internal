#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

char key[0x16];

void zheshishenme(){
    system(key);
    exit(0);
}

int read_num(){
    char input[32];
    int v2;
    memset(input,0,sizeof(input));
    read(0,input,0xf);
    return strtoul(input,0,0);
}

int main(){
    int num;
    int v4;
    size_t v5;
    unsigned int index;
    char *m;
    char *m_array[4];
    int v9;

    setvbuf(stdout,0,2,0);
    sbrk(0x603000);

    
    puts("===============");
    puts("   easy heap   ");
    puts("===============\n");
    m = malloc(0x88);
    printf("gift :D %p\n",m);
    free(m);

    memset(m_array,0,sizeof(m_array));
    index=0;
    while(1){
        while(1){
            printf("\n1) malloc %u/%u\n", index, 4LL);
            puts("2) quit");
            printf("> ");
            num=read_num();

            if(num==1){
                if(index>3){
                    puts("maximum requests reached");
                }
                printf("size: ");
                v4=read_num();
                m_array[index]=malloc(v4);
                if(m_array[index]){
                    printf("data: ");
                    v5=malloc_usable_size(m_array[index]);
                    read(0,m_array[index++]+8,v5);
                }
                else{
                    puts("request failed");
                }
            }
            if(num==2){
                // printf("gift :D %p\n",m_array[2]);
                zheshishenme();
            }
        }//第二个循环
    }//第一个循环

    return 0;
}