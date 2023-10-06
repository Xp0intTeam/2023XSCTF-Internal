#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <iostream>
#include <ctime>
#include <random>
#include <cstdlib>
using namespace std;

void banner(char* a, char* b, char* c, char* d, char* e, char* f, char* g, char* h, char* i, int& result, int& number, long long all[]) {
	char v1;
	char v2;
	char v3;
	char v4;
	char v5;
	char v6;
	char v7;
	char v8;
	char v9;
	char v10;
	char v11;
	char v12;
	char v13;
	char v14;
	char* v = new char[14];

	int MIN = 10000000;
	int MAX = 99999999;
	int RANGE = MAX - MIN + 1;

	puts(a);
	puts(b);

	v[9] = e[0];
	v[2] = v[9];
	v[1] = char(int(a[10] - 12));
	v[10] = char(int(c[5]) - 56);
	v[7] = char(int(f[15]) - 10);
	v[13] = toupper(char(int(h[3]) + 3));
	v[3] = char(int(b[1]) + 4);
	v[11] = toupper(char(int(g[7]) - 14));
	v[4] = v[7];
	v[0] = tolower(char(int(i[0]) + 31));
	v[8] = toupper(h[27]);
	v[5] = toupper(char(int(d[13]) - 16));
	v[6] = v[3];
	v[12] = char(int(e[6]) - 39);

	//cout << v[0] << v[1] << v[2] << v[3] << v[4] << v[5] << v[6] << v[7] << v[8] << v[9] << v[10] << v[11] << v[12] << v[13] << endl;
	//th1s_Is_F14G:D

	srand((unsigned)time(NULL));

	int index = 1;

	for (int i = 0; i < 8; i++) {
		int temp = (rand() % 10);
		if (i == 7) {
			if (temp == 0) {
				i--;
				continue;
			}
		}
		result += index * temp;

		index *= 10;
	}

	index = 1;

	for (int i = 0; i < 8; i++) {

		long long temp = (rand() % 10);

		if (i == 7) {
			if (temp == 0) {
				i--;
				continue;
			}
		}
		
		if (i == 0) all[number] = temp;
		else all[number] += index * temp;

		index *= 10;
	}

	number++;
	printf("%s %d\n", c, all[number - 1]);
}

void buy(int& number, long long all[]) {

	srand((unsigned)time(NULL));

	int index = 1;

	if (number < 10) {

		int MIN = 10000000;
		int MAX = 99999999;
		int RANGE = MAX - MIN + 1;

		for (int i = 0; i < 8; i++) {

			long long temp = (rand() % 10);

			if (i == 7) {
				if (temp == 0) {
					i--;
					continue;
				}
			}

			if (i == 0) {
				all[number] = temp;
			}

			else 
			all[number] += index * temp;

			index *= 10;
		}

		printf("%s %d\n", "Purchase successful, your number is ", all[number]);
		number++;
	}
	else {
		puts("The number of tickets you bought has reached the limit, please come again next time");
	}
}

void check(int& number, long long all[], int result) {
	for (int i = 0; i < number; i++) {
		if (all[i] == result) {
			puts("Congratulations on your win! But we don't seem to have anything for you");
			return;
		}
	}
	puts("I'm sorry you didn't win");
}

void join() {
	puts("Don't come and do business with us");
}

void flag() {
	puts("Nice try. It's not that easy");
}

void meau(char* a, char* b, char* c, char* d, char* e, char* f) {
	puts(a);
	puts(b);
	puts(c);
	puts(d);
	puts(e);
	puts(f);
}

void wait() {
	printf("Please enter any character to jump to the menu: ");
	string temp;
	cin >> temp;
	system("cls");
}

int main()
{
	char v1[50];
	char v2[50];
	char v3[60];
	char v4[50];
	char v5[50];
	char v6[50];
	char v7[50];
	char v8[50];
	char v9[50];
	int select;
	int result = 0;
	int money = 10;
	long long all[20];
	memset(all, 0, 30);
	int number = 0;
	strcpy(v1, "Sloth's lottery shop is open!");
	strcpy(v2, "You're our first customer!");
	strcpy(v3, "We will give you a free lottery ticket, the number is: ");
	strcpy(v4, "Please enter your choice {1-5}");
	strcpy(v5, "1.buy a lottery ticket");
	strcpy(v6, "2.Check to see if you won");
	strcpy(v7, "3.join us");
	strcpy(v8, "4.Take a sneak peek at the flag");
	strcpy(v9, "5.exit");

	banner(v1, v2, v3, v4, v5, v6, v7, v8, v9, result, number, all);
	while (1) {
		meau(v5, v6, v7, v8, v9, v4);
		scanf("%d", &select);
		switch (select) {
		case 1:
			system("cls");
			buy(number, all);
			wait();
			break;
		case 2:
			system("cls");
			check(number, all, result);
			wait();
			break;
		case 3:
			system("cls");
			join();
			wait();
			break;
		case 4:
			system("cls");
			flag();
			wait();
			break;
		case 5:
			system("cls");
			puts("Welcome again");
			wait();
			exit(1);
		default:
			puts("input error");
			wait();
			continue;
		}
		continue;
	}

	return 0;
}
