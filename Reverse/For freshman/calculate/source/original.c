#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
	freopen("out.txt", "w", stdout);
	srand((unsigned int)time(NULL));
	unsigned char flag[] = "flag{n0w_y0u_know_UPX!}";
	int len = sizeof(flag) / sizeof(flag[0]);
	int trans[50];
	for (int line = 0; line < 60; ++line) {
		for (int i = 0; i < len; ++i) {
restart:
			int cnt = rand() % 100 + 5;
			for (int j = 0; j < cnt; ++j) {
				trans[i] = rand() % 1000;
				if (trans[i] > 100)
					break;
			}
			if (trans[i] <= 100)
				goto restart;
		}
		/*printf("solver.add( ");
		int sum = 0;
		for (int i = 0; i < len; ++i) {
			printf(" %d * x%d ", trans[i], i);
			if (i != len - 1)
				putchar('+');
			sum += trans[i]*flag[i];
		}
		printf("== %d", sum);
		printf(" )\n");*/
		printf("if(");
		int sum = 0;
		for (int i = 0; i < len; ++i) {
			printf(" %d * x%d ", trans[i], i);
			if (i != len - 1)
				putchar('+');
			sum += trans[i] * flag[i];
		}
		printf("!= %d", sum);
		printf(")\nprintf(\"wrong!\");\n");
	}
	/*
	if ( 250 * x0 + 215 * x1 + 625 * x2 + 680 * x3 + 335 * x4 + 770 * x5 + 520 * x6 + 271 * x7 + 565 * x8 + 646 * x9 + 495 * x10 + 553 * x11 + 814 * x12 + 993 * x13 + 351 * x14 + 401 * x15 + 709 * x16 + 184 * x17 + 781 * x18 + 814 * x19 + 421 * x20 + 819 * x21 + 212 * x22 + 525 * x23 != 1173434)
	return 0;
	if ( 371 * x0 + 744 * x1 + 795 * x2 + 186 * x3 + 598 * x4 + 815 * x5 + 115 * x6 + 988 * x7 + 279 * x8 + 569 * x9 + 126 * x10 + 363 * x11 + 207 * x12 + 353 * x13 + 781 * x14 + 760 * x15 + 630 * x16 + 625 * x17 + 961 * x18 + 323 * x19 + 404 * x20 + 819 * x21 + 909 * x22 + 354 * x23 != 1290416)
	return 0;
	if ( 276 * x0 + 371 * x1 + 145 * x2 + 663 * x3 + 895 * x4 + 594 * x5 + 503 * x6 + 889 * x7 + 251 * x8 + 998 * x9 + 716 * x10 + 784 * x11 + 888 * x12 + 974 * x13 + 771 * x14 + 655 * x15 + 414 * x16 + 809 * x17 + 726 * x18 + 185 * x19 + 239 * x20 + 482 * x21 + 216 * x22 + 609 * x23 != 1339295)
	return 0;
	if ( 936 * x0 + 697 * x1 + 409 * x2 + 736 * x3 + 538 * x4 + 806 * x5 + 655 * x6 + 928 * x7 + 308 * x8 + 132 * x9 + 590 * x10 + 121 * x11 + 601 * x12 + 310 * x13 + 568 * x14 + 345 * x15 + 138 * x16 + 356 * x17 + 868 * x18 + 449 * x19 + 877 * x20 + 721 * x21 + 361 * x22 + 465 * x23 != 1167720)
	return 0;
	if ( 269 * x0 + 208 * x1 + 391 * x2 + 201 * x3 + 186 * x4 + 155 * x5 + 355 * x6 + 845 * x7 + 757 * x8 + 721 * x9 + 357 * x10 + 990 * x11 + 970 * x12 + 972 * x13 + 930 * x14 + 672 * x15 + 837 * x16 + 939 * x17 + 729 * x18 + 934 * x19 + 707 * x20 + 620 * x21 + 946 * x22 + 979 * x23 != 1457642)
	return 0;
	if ( 652 * x0 + 603 * x1 + 957 * x2 + 333 * x3 + 938 * x4 + 147 * x5 + 620 * x6 + 561 * x7 + 207 * x8 + 400 * x9 + 964 * x10 + 806 * x11 + 840 * x12 + 330 * x13 + 837 * x14 + 176 * x15 + 995 * x16 + 657 * x17 + 518 * x18 + 752 * x19 + 970 * x20 + 243 * x21 + 992 * x22 + 366 * x23 != 1424563)
	return 0;
	if ( 425 * x0 + 842 * x1 + 315 * x2 + 587 * x3 + 898 * x4 + 547 * x5 + 923 * x6 + 369 * x7 + 764 * x8 + 712 * x9 + 955 * x10 + 920 * x11 + 768 * x12 + 313 * x13 + 784 * x14 + 144 * x15 + 174 * x16 + 380 * x17 + 427 * x18 + 634 * x19 + 297 * x20 + 998 * x21 + 650 * x22 + 756 * x23 != 1289169)
	return 0;
	if ( 655 * x0 + 600 * x1 + 510 * x2 + 162 * x3 + 263 * x4 + 922 * x5 + 684 * x6 + 941 * x7 + 978 * x8 + 756 * x9 + 523 * x10 + 986 * x11 + 689 * x12 + 766 * x13 + 168 * x14 + 253 * x15 + 265 * x16 + 366 * x17 + 154 * x18 + 463 * x19 + 629 * x20 + 943 * x21 + 456 * x22 + 488 * x23 != 1255084)
	return 0;
	if ( 788 * x0 + 651 * x1 + 228 * x2 + 732 * x3 + 163 * x4 + 809 * x5 + 149 * x6 + 324 * x7 + 921 * x8 + 946 * x9 + 261 * x10 + 346 * x11 + 475 * x12 + 370 * x13 + 467 * x14 + 178 * x15 + 515 * x16 + 922 * x17 + 937 * x18 + 123 * x19 + 701 * x20 + 560 * x21 + 895 * x22 + 248 * x23 != 1244160)
	return 0;
	if ( 739 * x0 + 388 * x1 + 209 * x2 + 339 * x3 + 226 * x4 + 697 * x5 + 267 * x6 + 208 * x7 + 426 * x8 + 383 * x9 + 275 * x10 + 646 * x11 + 787 * x12 + 180 * x13 + 887 * x14 + 644 * x15 + 361 * x16 + 272 * x17 + 587 * x18 + 430 * x19 + 999 * x20 + 850 * x21 + 174 * x22 + 821 * x23 != 1043988)
	return 0;
	if ( 855 * x0 + 101 * x1 + 890 * x2 + 997 * x3 + 446 * x4 + 518 * x5 + 192 * x6 + 205 * x7 + 733 * x8 + 855 * x9 + 369 * x10 + 499 * x11 + 913 * x12 + 559 * x13 + 350 * x14 + 934 * x15 + 763 * x16 + 984 * x17 + 138 * x18 + 962 * x19 + 249 * x20 + 247 * x21 + 106 * x22 + 751 * x23 != 1286775)
	return 0;
	if ( 363 * x0 + 568 * x1 + 868 * x2 + 378 * x3 + 927 * x4 + 383 * x5 + 989 * x6 + 333 * x7 + 344 * x8 + 352 * x9 + 109 * x10 + 677 * x11 + 624 * x12 + 998 * x13 + 657 * x14 + 629 * x15 + 106 * x16 + 673 * x17 + 676 * x18 + 507 * x19 + 579 * x20 + 169 * x21 + 388 * x22 + 408 * x23 != 1212216)
	return 0;
	if ( 958 * x0 + 223 * x1 + 855 * x2 + 410 * x3 + 368 * x4 + 892 * x5 + 380 * x6 + 641 * x7 + 789 * x8 + 571 * x9 + 312 * x10 + 851 * x11 + 793 * x12 + 322 * x13 + 874 * x14 + 369 * x15 + 992 * x16 + 326 * x17 + 391 * x18 + 167 * x19 + 128 * x20 + 396 * x21 + 919 * x22 + 248 * x23 != 1325165)
	return 0;
	if ( 401 * x0 + 696 * x1 + 518 * x2 + 896 * x3 + 676 * x4 + 923 * x5 + 231 * x6 + 838 * x7 + 876 * x8 + 317 * x9 + 660 * x10 + 400 * x11 + 101 * x12 + 548 * x13 + 939 * x14 + 249 * x15 + 186 * x16 + 264 * x17 + 967 * x18 + 380 * x19 + 264 * x20 + 651 * x21 + 857 * x22 + 684 * x23 != 1264958)
	return 0;
	if ( 248 * x0 + 283 * x1 + 867 * x2 + 530 * x3 + 736 * x4 + 299 * x5 + 653 * x6 + 148 * x7 + 617 * x8 + 817 * x9 + 699 * x10 + 480 * x11 + 706 * x12 + 465 * x13 + 917 * x14 + 981 * x15 + 236 * x16 + 145 * x17 + 613 * x18 + 986 * x19 + 662 * x20 + 434 * x21 + 766 * x22 + 575 * x23 != 1281865)
	return 0;
	if ( 407 * x0 + 400 * x1 + 846 * x2 + 660 * x3 + 508 * x4 + 231 * x5 + 225 * x6 + 878 * x7 + 734 * x8 + 478 * x9 + 238 * x10 + 997 * x11 + 262 * x12 + 167 * x13 + 604 * x14 + 913 * x15 + 198 * x16 + 230 * x17 + 201 * x18 + 282 * x19 + 663 * x20 + 494 * x21 + 924 * x22 + 718 * x23 != 1179318)
	return 0;
	if ( 240 * x0 + 130 * x1 + 318 * x2 + 210 * x3 + 910 * x4 + 803 * x5 + 125 * x6 + 328 * x7 + 792 * x8 + 678 * x9 + 653 * x10 + 357 * x11 + 574 * x12 + 473 * x13 + 272 * x14 + 871 * x15 + 157 * x16 + 798 * x17 + 142 * x18 + 139 * x19 + 569 * x20 + 815 * x21 + 148 * x22 + 723 * x23 != 1011571)
	return 0;
	if ( 782 * x0 + 514 * x1 + 683 * x2 + 716 * x3 + 257 * x4 + 622 * x5 + 720 * x6 + 197 * x7 + 392 * x8 + 421 * x9 + 820 * x10 + 920 * x11 + 678 * x12 + 970 * x13 + 122 * x14 + 658 * x15 + 135 * x16 + 715 * x17 + 811 * x18 + 859 * x19 + 542 * x20 + 156 * x21 + 731 * x22 + 945 * x23 != 1289012)
	return 0;
	if ( 978 * x0 + 451 * x1 + 785 * x2 + 694 * x3 + 973 * x4 + 515 * x5 + 565 * x6 + 691 * x7 + 873 * x8 + 616 * x9 + 369 * x10 + 752 * x11 + 316 * x12 + 854 * x13 + 171 * x14 + 732 * x15 + 247 * x16 + 870 * x17 + 989 * x18 + 650 * x19 + 141 * x20 + 380 * x21 + 157 * x22 + 167 * x23 != 1359077)
	return 0;
	if ( 642 * x0 + 938 * x1 + 107 * x2 + 638 * x3 + 900 * x4 + 345 * x5 + 597 * x6 + 866 * x7 + 955 * x8 + 200 * x9 + 525 * x10 + 503 * x11 + 921 * x12 + 293 * x13 + 888 * x14 + 670 * x15 + 641 * x16 + 424 * x17 + 393 * x18 + 376 * x19 + 302 * x20 + 161 * x21 + 395 * x22 + 983 * x23 != 1274421)
	return 0;
	if ( 609 * x0 + 858 * x1 + 847 * x2 + 192 * x3 + 937 * x4 + 956 * x5 + 463 * x6 + 377 * x7 + 932 * x8 + 701 * x9 + 265 * x10 + 936 * x11 + 751 * x12 + 578 * x13 + 456 * x14 + 230 * x15 + 907 * x16 + 133 * x17 + 212 * x18 + 448 * x19 + 452 * x20 + 146 * x21 + 590 * x22 + 217 * x23 != 1341461)
	return 0;
	if ( 721 * x0 + 231 * x1 + 200 * x2 + 738 * x3 + 521 * x4 + 396 * x5 + 458 * x6 + 484 * x7 + 833 * x8 + 447 * x9 + 781 * x10 + 987 * x11 + 448 * x12 + 814 * x13 + 790 * x14 + 307 * x15 + 998 * x16 + 213 * x17 + 494 * x18 + 603 * x19 + 474 * x20 + 828 * x21 + 654 * x22 + 817 * x23 != 1297964)
	return 0;
	if ( 280 * x0 + 128 * x1 + 868 * x2 + 504 * x3 + 442 * x4 + 774 * x5 + 405 * x6 + 156 * x7 + 106 * x8 + 480 * x9 + 675 * x10 + 346 * x11 + 668 * x12 + 665 * x13 + 477 * x14 + 240 * x15 + 799 * x16 + 704 * x17 + 842 * x18 + 552 * x19 + 849 * x20 + 144 * x21 + 306 * x22 + 122 * x23 != 1106164)
	return 0;
	if ( 504 * x0 + 286 * x1 + 320 * x2 + 360 * x3 + 601 * x4 + 762 * x5 + 213 * x6 + 624 * x7 + 383 * x8 + 741 * x9 + 901 * x10 + 845 * x11 + 479 * x12 + 898 * x13 + 280 * x14 + 803 * x15 + 541 * x16 + 745 * x17 + 372 * x18 + 284 * x19 + 663 * x20 + 374 * x21 + 329 * x22 + 934 * x23 != 1223627)
	return 0;
	if ( 672 * x0 + 584 * x1 + 395 * x2 + 762 * x3 + 438 * x4 + 282 * x5 + 484 * x6 + 726 * x7 + 124 * x8 + 124 * x9 + 851 * x10 + 119 * x11 + 209 * x12 + 505 * x13 + 319 * x14 + 198 * x15 + 994 * x16 + 579 * x17 + 264 * x18 + 759 * x19 + 160 * x20 + 860 * x21 + 770 * x22 + 480 * x23 != 1050611)
	return 0;
	if ( 393 * x0 + 108 * x1 + 936 * x2 + 621 * x3 + 212 * x4 + 262 * x5 + 187 * x6 + 966 * x7 + 494 * x8 + 883 * x9 + 732 * x10 + 198 * x11 + 536 * x12 + 308 * x13 + 939 * x14 + 115 * x15 + 672 * x16 + 421 * x17 + 137 * x18 + 651 * x19 + 464 * x20 + 478 * x21 + 122 * x22 + 290 * x23 != 1052881)
	return 0;
	if ( 369 * x0 + 383 * x1 + 598 * x2 + 127 * x3 + 817 * x4 + 901 * x5 + 482 * x6 + 712 * x7 + 911 * x8 + 181 * x9 + 611 * x10 + 296 * x11 + 425 * x12 + 160 * x13 + 782 * x14 + 320 * x15 + 226 * x16 + 943 * x17 + 224 * x18 + 946 * x19 + 403 * x20 + 984 * x21 + 547 * x22 + 559 * x23 != 1156505)
	return 0;
	if ( 953 * x0 + 461 * x1 + 320 * x2 + 569 * x3 + 940 * x4 + 603 * x5 + 968 * x6 + 482 * x7 + 914 * x8 + 796 * x9 + 241 * x10 + 360 * x11 + 756 * x12 + 275 * x13 + 456 * x14 + 978 * x15 + 178 * x16 + 988 * x17 + 962 * x18 + 901 * x19 + 881 * x20 + 180 * x21 + 118 * x22 + 531 * x23 != 1386320)
	return 0;
	if ( 414 * x0 + 954 * x1 + 451 * x2 + 262 * x3 + 770 * x4 + 125 * x5 + 863 * x6 + 652 * x7 + 609 * x8 + 132 * x9 + 727 * x10 + 226 * x11 + 315 * x12 + 255 * x13 + 974 * x14 + 157 * x15 + 675 * x16 + 112 * x17 + 367 * x18 + 871 * x19 + 628 * x20 + 640 * x21 + 683 * x22 + 169 * x23 != 1114006)
	return 0;
	if ( 851 * x0 + 281 * x1 + 249 * x2 + 195 * x3 + 815 * x4 + 512 * x5 + 526 * x6 + 767 * x7 + 114 * x8 + 832 * x9 + 979 * x10 + 255 * x11 + 375 * x12 + 259 * x13 + 988 * x14 + 914 * x15 + 331 * x16 + 121 * x17 + 845 * x18 + 480 * x19 + 867 * x20 + 474 * x21 + 708 * x22 + 947 * x23 != 1237822)
	return 0;
	if ( 755 * x0 + 238 * x1 + 419 * x2 + 237 * x3 + 840 * x4 + 362 * x5 + 208 * x6 + 134 * x7 + 866 * x8 + 177 * x9 + 381 * x10 + 481 * x11 + 396 * x12 + 990 * x13 + 240 * x14 + 485 * x15 + 839 * x16 + 707 * x17 + 660 * x18 + 806 * x19 + 399 * x20 + 622 * x21 + 895 * x22 + 121 * x23 != 1193974)
	return 0;
	if ( 580 * x0 + 704 * x1 + 998 * x2 + 696 * x3 + 819 * x4 + 460 * x5 + 978 * x6 + 451 * x7 + 796 * x8 + 287 * x9 + 858 * x10 + 504 * x11 + 767 * x12 + 913 * x13 + 297 * x14 + 403 * x15 + 516 * x16 + 644 * x17 + 384 * x18 + 137 * x19 + 158 * x20 + 560 * x21 + 735 * x22 + 112 * x23 != 1304537)
	return 0;
	if ( 994 * x0 + 104 * x1 + 537 * x2 + 332 * x3 + 227 * x4 + 307 * x5 + 878 * x6 + 830 * x7 + 442 * x8 + 172 * x9 + 551 * x10 + 688 * x11 + 734 * x12 + 613 * x13 + 589 * x14 + 645 * x15 + 920 * x16 + 173 * x17 + 436 * x18 + 997 * x19 + 981 * x20 + 704 * x21 + 555 * x22 + 775 * x23 != 1264632)
	return 0;
	if ( 104 * x0 + 282 * x1 + 509 * x2 + 561 * x3 + 958 * x4 + 392 * x5 + 371 * x6 + 398 * x7 + 477 * x8 + 666 * x9 + 221 * x10 + 171 * x11 + 901 * x12 + 435 * x13 + 452 * x14 + 370 * x15 + 821 * x16 + 719 * x17 + 472 * x18 + 827 * x19 + 613 * x20 + 918 * x21 + 379 * x22 + 590 * x23 != 1157687)
	return 0;
	if ( 552 * x0 + 621 * x1 + 601 * x2 + 674 * x3 + 797 * x4 + 623 * x5 + 307 * x6 + 772 * x7 + 450 * x8 + 705 * x9 + 315 * x10 + 619 * x11 + 283 * x12 + 313 * x13 + 319 * x14 + 255 * x15 + 745 * x16 + 941 * x17 + 512 * x18 + 486 * x19 + 261 * x20 + 750 * x21 + 322 * x22 + 242 * x23 != 1212043)
	return 0;
	if ( 263 * x0 + 984 * x1 + 899 * x2 + 345 * x3 + 135 * x4 + 375 * x5 + 756 * x6 + 761 * x7 + 874 * x8 + 837 * x9 + 275 * x10 + 229 * x11 + 343 * x12 + 101 * x13 + 817 * x14 + 499 * x15 + 441 * x16 + 312 * x17 + 468 * x18 + 654 * x19 + 559 * x20 + 589 * x21 + 737 * x22 + 114 * x23 != 1188462)
	return 0;
	if ( 961 * x0 + 684 * x1 + 789 * x2 + 758 * x3 + 878 * x4 + 968 * x5 + 589 * x6 + 111 * x7 + 202 * x8 + 783 * x9 + 990 * x10 + 806 * x11 + 494 * x12 + 571 * x13 + 222 * x14 + 731 * x15 + 122 * x16 + 620 * x17 + 520 * x18 + 177 * x19 + 445 * x20 + 124 * x21 + 911 * x22 + 550 * x23 != 1340704)
	return 0;
	if ( 900 * x0 + 514 * x1 + 101 * x2 + 536 * x3 + 121 * x4 + 881 * x5 + 876 * x6 + 596 * x7 + 465 * x8 + 537 * x9 + 270 * x10 + 508 * x11 + 591 * x12 + 386 * x13 + 335 * x14 + 313 * x15 + 993 * x16 + 598 * x17 + 989 * x18 + 616 * x19 + 828 * x20 + 108 * x21 + 125 * x22 + 188 * x23 != 1188045)
	return 0;
	if ( 931 * x0 + 776 * x1 + 766 * x2 + 627 * x3 + 434 * x4 + 610 * x5 + 933 * x6 + 846 * x7 + 632 * x8 + 549 * x9 + 299 * x10 + 540 * x11 + 989 * x12 + 965 * x13 + 746 * x14 + 315 * x15 + 132 * x16 + 612 * x17 + 721 * x18 + 665 * x19 + 442 * x20 + 971 * x21 + 509 * x22 + 776 * x23 != 1424726)
	return 0;
	if ( 197 * x0 + 644 * x1 + 880 * x2 + 306 * x3 + 983 * x4 + 833 * x5 + 610 * x6 + 144 * x7 + 184 * x8 + 319 * x9 + 853 * x10 + 939 * x11 + 428 * x12 + 239 * x13 + 971 * x14 + 428 * x15 + 143 * x16 + 839 * x17 + 145 * x18 + 290 * x19 + 966 * x20 + 591 * x21 + 991 * x22 + 968 * x23 != 1253549)
	return 0;
	if ( 286 * x0 + 778 * x1 + 425 * x2 + 275 * x3 + 633 * x4 + 468 * x5 + 629 * x6 + 928 * x7 + 144 * x8 + 620 * x9 + 688 * x10 + 534 * x11 + 305 * x12 + 139 * x13 + 353 * x14 + 109 * x15 + 467 * x16 + 218 * x17 + 669 * x18 + 396 * x19 + 756 * x20 + 255 * x21 + 379 * x22 + 296 * x23 != 1018834)
	return 0;
	if ( 833 * x0 + 297 * x1 + 934 * x2 + 309 * x3 + 510 * x4 + 586 * x5 + 227 * x6 + 596 * x7 + 426 * x8 + 933 * x9 + 859 * x10 + 452 * x11 + 650 * x12 + 273 * x13 + 623 * x14 + 886 * x15 + 853 * x16 + 803 * x17 + 336 * x18 + 651 * x19 + 122 * x20 + 749 * x21 + 281 * x22 + 817 * x23 != 1282803)
	return 0;
	if ( 162 * x0 + 750 * x1 + 405 * x2 + 131 * x3 + 781 * x4 + 168 * x5 + 302 * x6 + 414 * x7 + 632 * x8 + 924 * x9 + 297 * x10 + 364 * x11 + 651 * x12 + 765 * x13 + 878 * x14 + 426 * x15 + 717 * x16 + 391 * x17 + 778 * x18 + 609 * x19 + 361 * x20 + 969 * x21 + 179 * x22 + 888 * x23 != 1168299)
	return 0;
	if ( 752 * x0 + 658 * x1 + 144 * x2 + 155 * x3 + 900 * x4 + 745 * x5 + 526 * x6 + 233 * x7 + 421 * x8 + 382 * x9 + 813 * x10 + 266 * x11 + 199 * x12 + 593 * x13 + 905 * x14 + 167 * x15 + 188 * x16 + 367 * x17 + 217 * x18 + 733 * x19 + 660 * x20 + 895 * x21 + 349 * x22 + 651 * x23 != 1045694)
	return 0;
	if ( 580 * x0 + 611 * x1 + 642 * x2 + 794 * x3 + 206 * x4 + 650 * x5 + 510 * x6 + 317 * x7 + 136 * x8 + 751 * x9 + 395 * x10 + 216 * x11 + 172 * x12 + 583 * x13 + 271 * x14 + 202 * x15 + 339 * x16 + 767 * x17 + 396 * x18 + 301 * x19 + 526 * x20 + 125 * x21 + 319 * x22 + 439 * x23 != 968455)
	return 0;
	if ( 875 * x0 + 330 * x1 + 996 * x2 + 416 * x3 + 852 * x4 + 448 * x5 + 378 * x6 + 259 * x7 + 532 * x8 + 530 * x9 + 308 * x10 + 216 * x11 + 230 * x12 + 109 * x13 + 369 * x14 + 418 * x15 + 286 * x16 + 562 * x17 + 508 * x18 + 891 * x19 + 356 * x20 + 811 * x21 + 652 * x22 + 492 * x23 != 1084093)
	return 0;
	if ( 740 * x0 + 363 * x1 + 317 * x2 + 785 * x3 + 540 * x4 + 355 * x5 + 411 * x6 + 946 * x7 + 624 * x8 + 571 * x9 + 413 * x10 + 333 * x11 + 184 * x12 + 761 * x13 + 822 * x14 + 651 * x15 + 836 * x16 + 464 * x17 + 454 * x18 + 936 * x19 + 411 * x20 + 897 * x21 + 484 * x22 + 931 * x23 != 1296107)
	return 0;
	if ( 627 * x0 + 814 * x1 + 121 * x2 + 853 * x3 + 200 * x4 + 457 * x5 + 747 * x6 + 472 * x7 + 575 * x8 + 896 * x9 + 178 * x10 + 326 * x11 + 756 * x12 + 248 * x13 + 174 * x14 + 207 * x15 + 415 * x16 + 926 * x17 + 861 * x18 + 109 * x19 + 663 * x20 + 227 * x21 + 959 * x22 + 958 * x23 != 1173526)
	return 0;
	if ( 334 * x0 + 486 * x1 + 906 * x2 + 254 * x3 + 610 * x4 + 958 * x5 + 604 * x6 + 828 * x7 + 764 * x8 + 724 * x9 + 976 * x10 + 725 * x11 + 569 * x12 + 687 * x13 + 375 * x14 + 603 * x15 + 200 * x16 + 582 * x17 + 237 * x18 + 950 * x19 + 182 * x20 + 219 * x21 + 761 * x22 + 571 * x23 != 1329741)
	return 0;
	if ( 262 * x0 + 167 * x1 + 544 * x2 + 973 * x3 + 440 * x4 + 250 * x5 + 694 * x6 + 919 * x7 + 210 * x8 + 564 * x9 + 726 * x10 + 312 * x11 + 599 * x12 + 969 * x13 + 251 * x14 + 373 * x15 + 663 * x16 + 160 * x17 + 864 * x18 + 512 * x19 + 254 * x20 + 177 * x21 + 939 * x22 + 533 * x23 != 1165252)
	return 0;
	if ( 168 * x0 + 648 * x1 + 916 * x2 + 822 * x3 + 995 * x4 + 629 * x5 + 379 * x6 + 517 * x7 + 541 * x8 + 432 * x9 + 682 * x10 + 642 * x11 + 493 * x12 + 977 * x13 + 669 * x14 + 389 * x15 + 827 * x16 + 218 * x17 + 410 * x18 + 641 * x19 + 966 * x20 + 758 * x21 + 342 * x22 + 123 * x23 != 1369613)
	return 0;
	if ( 333 * x0 + 298 * x1 + 781 * x2 + 936 * x3 + 172 * x4 + 468 * x5 + 980 * x6 + 261 * x7 + 968 * x8 + 513 * x9 + 431 * x10 + 301 * x11 + 350 * x12 + 712 * x13 + 190 * x14 + 574 * x15 + 834 * x16 + 366 * x17 + 612 * x18 + 578 * x19 + 616 * x20 + 862 * x21 + 315 * x22 + 197 * x23 != 1147341)
	return 0;
	if ( 413 * x0 + 977 * x1 + 749 * x2 + 311 * x3 + 992 * x4 + 312 * x5 + 225 * x6 + 192 * x7 + 249 * x8 + 423 * x9 + 398 * x10 + 191 * x11 + 289 * x12 + 185 * x13 + 238 * x14 + 121 * x15 + 435 * x16 + 435 * x17 + 275 * x18 + 379 * x19 + 143 * x20 + 988 * x21 + 729 * x22 + 788 * x23 != 928560)
	return 0;
	if ( 444 * x0 + 531 * x1 + 114 * x2 + 416 * x3 + 549 * x4 + 104 * x5 + 204 * x6 + 727 * x7 + 670 * x8 + 342 * x9 + 650 * x10 + 950 * x11 + 945 * x12 + 487 * x13 + 556 * x14 + 167 * x15 + 848 * x16 + 288 * x17 + 735 * x18 + 597 * x19 + 274 * x20 + 307 * x21 + 529 * x22 + 453 * x23 != 1139652)
	return 0;
	if ( 449 * x0 + 348 * x1 + 610 * x2 + 712 * x3 + 680 * x4 + 664 * x5 + 101 * x6 + 193 * x7 + 976 * x8 + 577 * x9 + 344 * x10 + 305 * x11 + 250 * x12 + 211 * x13 + 499 * x14 + 620 * x15 + 346 * x16 + 507 * x17 + 728 * x18 + 808 * x19 + 741 * x20 + 975 * x21 + 513 * x22 + 491 * x23 != 1162521)
	return 0;
	if ( 479 * x0 + 613 * x1 + 770 * x2 + 878 * x3 + 176 * x4 + 737 * x5 + 419 * x6 + 979 * x7 + 819 * x8 + 811 * x9 + 722 * x10 + 739 * x11 + 113 * x12 + 271 * x13 + 377 * x14 + 574 * x15 + 180 * x16 + 351 * x17 + 580 * x18 + 777 * x19 + 134 * x20 + 861 * x21 + 974 * x22 + 543 * x23 != 1289668)
	return 0;
	if ( 404 * x0 + 712 * x1 + 767 * x2 + 492 * x3 + 193 * x4 + 968 * x5 + 804 * x6 + 731 * x7 + 557 * x8 + 145 * x9 + 383 * x10 + 873 * x11 + 633 * x12 + 652 * x13 + 728 * x14 + 474 * x15 + 937 * x16 + 264 * x17 + 223 * x18 + 969 * x19 + 407 * x20 + 122 * x21 + 435 * x22 + 410 * x23 != 1279832)
	return 0;
	if ( 396 * x0 + 290 * x1 + 331 * x2 + 122 * x3 + 665 * x4 + 636 * x5 + 166 * x6 + 732 * x7 + 511 * x8 + 656 * x9 + 123 * x10 + 557 * x11 + 113 * x12 + 475 * x13 + 538 * x14 + 217 * x15 + 988 * x16 + 555 * x17 + 514 * x18 + 515 * x19 + 398 * x20 + 271 * x21 + 712 * x22 + 577 * x23 != 1095191)
	return 0;
	if ( 858 * x0 + 861 * x1 + 254 * x2 + 322 * x3 + 200 * x4 + 969 * x5 + 126 * x6 + 403 * x7 + 861 * x8 + 499 * x9 + 513 * x10 + 316 * x11 + 808 * x12 + 264 * x13 + 634 * x14 + 254 * x15 + 501 * x16 + 529 * x17 + 493 * x18 + 602 * x19 + 854 * x20 + 635 * x21 + 268 * x22 + 291 * x23 != 1159761)
	return 0;
	if ( 598 * x0 + 396 * x1 + 564 * x2 + 590 * x3 + 560 * x4 + 609 * x5 + 798 * x6 + 962 * x7 + 585 * x8 + 649 * x9 + 747 * x10 + 585 * x11 + 125 * x12 + 441 * x13 + 496 * x14 + 392 * x15 + 391 * x16 + 808 * x17 + 761 * x18 + 108 * x19 + 109 * x20 + 645 * x21 + 140 * x22 + 747 * x23 != 1148424)
	return 0;

	 */
	return 0;
}