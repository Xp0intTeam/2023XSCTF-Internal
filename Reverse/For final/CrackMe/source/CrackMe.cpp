#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

// 反调试，异常过滤器中调用此函数
VOID DisableDebugEvent(VOID)
{
    BOOL isDebuggerPresent = FALSE;
    if (CheckRemoteDebuggerPresent(GetCurrentProcess(), &isDebuggerPresent ))
    {
        if (isDebuggerPresent )
        {
            exit(-1);
        }
    }
}

// 异常过滤器
int FilterFuncofDBZ(int dwExceptionCode){
    if (dwExceptionCode == EXCEPTION_INT_DIVIDE_BY_ZERO){
		DisableDebugEvent();
        return EXCEPTION_EXECUTE_HANDLER;
    }
        return EXCEPTION_CONTINUE_SEARCH;
}

unsigned int handle(char *s, int len) {
    unsigned int res = 0;
    for (int i = len - 1; i >= 0; i--) {
        res <<= 4;
        char c = s[i];
        if (c >= 'A' && c <= 'F') {
            res += ('F' - c);
        } else if (c >= '0' && c <= '9') {
            res += 0xF - (c - '0');
        } else {
            return -1;
        }
    }
    return res;
}

unsigned int CRC32_like(unsigned long long int n) {
    unsigned long long int res = 0;
    for (int i = 0; i < 8; i++) {
        unsigned int v2 = ((n >> (8 * i)) & 0xFF) << 24;
        if (i > 0) {
            res ^= v2;
        } else {
            res = (~v2) & 0xFFFFFFFF;
        }
        for (int j = 0; j < 8; j++) {
            res *= 2;
            if (res >= 0xFFFFFFFF) {
                res &= 0xFFFFFFFF;
                res ^= 0x4C11DB7;
            }
        }
    }
    return (unsigned int)res;
}

int main() {
//    flag{5D04AF1BD2565F3}
//    input table : "1234567890ABCDEF";
//    char key[] = "5D04AF1BD2565F38";
	char key[64] = {};
    puts("请输入flag:"); 
	scanf("%s",key);

	if (strlen(key) != 16) exit(0);
	
    unsigned int v1 = handle(key, 6);
    unsigned int v2 = handle(key + 6, 2);
    unsigned int v3 = handle(key + 8, 4);
    unsigned int v4 = handle(key + 12, 4);
    
    if (v1 == -1 || v2 == -1 || v3 == -1 || v4 == -1) exit(0); 
    
    unsigned int low_4B = ((v2 << 24) + v1) ^ 0x12345678;
    unsigned int high_4B = ((v4 << 16) + v3) ^ 0x87654321;

	__try {
	    __asm{
			xor eax, eax
			div eax
		};	
    }
    __except (FilterFuncofDBZ(GetExceptionCode())){}

    unsigned long long int combined = ((unsigned long long int)high_4B << 32) + (unsigned long long int)low_4B;
    if ( ( (combined & 0xFFFFFFFFFF000000) != 0xFB6FD9F35C000000) || (0x5D477780 != (CRC32_like(combined) & 0xFFFFFFFF) ) ){
		printf("验证失败\n");
		exit(-1);
	}
    
	printf("验证成功。flag格式为flag{(your input)}\n");
    
    return 0;
}
