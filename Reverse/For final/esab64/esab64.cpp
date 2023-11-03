#include "stdafx.h"
int index = 1000;
std::string s;
std::string res = "UYP7wQcTBee0Z6V3t66TAbJK+YCKWZPhVpf3R5P4ZHcEWVP5yiXFXHr4W4OBmT==";
int b[1] = { 0 };
int checkdebug()
{
	int result = IsDebuggerPresent();
	if (result)
	{
		index = 1;
	}
	return result;
}
void base64(std::string &s, std::string &res)
{
	int i, j;
	std::string alphabet_map = "m2jrJbkftp1KoBFNZhwE56OysH0z473T8VRW9l/PGixgdM+UeQCaDucXIYSnLvqA";
	int len = s.size();
	for (i = 0, j = 0; i + 3 <= len; i += 3)
	{
		res.push_back(alphabet_map[s[i + 2] & 0x3f]);
		res.push_back(alphabet_map[((s[i + 1] << 2) & 0x3c) | (s[i + 2] >> 6)]);
		res.push_back(alphabet_map[((s[i] << 4) & 0x30) | (s[i + 1] >> 4)]);
		res.push_back(alphabet_map[s[i] >> 2]);
	}
	if (i < len)
	{
		int tail = len - i;
		if (tail == 1)
		{
			res.push_back(alphabet_map[((s[i] << 4) & 0x30) | (s[i + 1] >> 4)]);
			res.push_back(alphabet_map[s[i] >> 2]);
			res.push_back('=');
			res.push_back('=');
		}
		else
		{
			res.push_back(alphabet_map[s[i + 2] & 0x3f]);
			res.push_back(alphabet_map[((s[i + 1] << 2) & 0x3c) | (s[i + 2] >> 6)]);
			res.push_back(alphabet_map[((s[i] << 4) & 0x30) | (s[i + 1] >> 4)]);
			res.push_back('=');
		}
	}
}
void Xor (std::string& s)
{
	int size = s.size();
	for (int i = 0; i < size; i++)
	{
		s[i] ^= (size - i);
	}
}
void Exception()
{
	__try {
		b[index] = 0;
	}
	__except (1)
	{
		Xor(s);
	}
}
int main()
{
	checkdebug();
	std::string s1;
	std::string wel = "欢迎来到这里！你能猜到我藏着什么秘密嘛？\n";
	std::string input = "请给我你的答案：";
	std::cout << wel << input;
	std::cin >> s;
	Exception();
	base64(s, s1);
	int sz = s.size();
	int i;
	for (i = 0; i < sz; i++)
	{
		if (s1[i] != res[i])
		{
			std::cout << "可惜，你并没有得到我的秘密:(\n";
			break;
		}
	}
	if (i == sz)
	{
		std::cout << "恭喜！你得到我的秘密了！^_^\n";
	}
	return 0;
}
