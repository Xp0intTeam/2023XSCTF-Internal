#include<stdio.h>
#include<string.h>

// flag{r3411y_646y_r3v3rs3@}

int main(){
	char flag[26] = {};
	char an[] = "\x66\x07\x2c\x3b\x7b\x19\x66\xa1\x31\x5a\x2f\xfa\x36\x5f\xc6\xcb\x5f\x19\x66\xb3\x33\x19\x6e\x99\x40\x16";
	puts("Please input flag:");
	scanf("%s",flag);
	if(strlen(flag)!=26){
		puts("Wrong length!");
		return 0;
	}
	__asm(
      ".byte 0xEB\n\t"//EB FF jmp -1
      ".byte 0xFF\n\t"//FF C0 inc eax
      ".byte 0xC0\n\t"
//      "dec eax\n\t"
    );
	for(int i = 0;i<strlen(flag);i++){
		if(i % 4 == 0) flag[i] = ((flag[i])&0xE7)^(flag[i]&0x10>>1)^(flag[i]&0x08<<1);
		else if(i % 4 == 1) flag[i] ^= 107;
		else if(i % 4 == 2) flag[i] = (flag[i]>>3)|((flag[i]<<5)&0xff);
		else if(i % 4 == 3) flag[i] = (flag[i]>>5)|((flag[i]<<3)&0xff);
	}
	for(int i = 0;i<strlen(flag);i++){
		if(flag[i]!=an[i]){
			puts("Wrong flag!");
			return 0;
		}
	}
	puts("Right flag!");
	
	return 0;
}
