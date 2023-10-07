from z3 import *


# for i in range(1, 32):
#     print('x' + str(i) + ',', end='')
# print(' = Ints(\'', end='')
# for i in range(1, 32):
#     print('x'+str(i),end=' ')
# print('\')')
def calculate():
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23 = Ints(
        'x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 x21 x22 x23')
    solver = Solver()
    # for i in range(30):
    #     str = input()
    #     print('solver.add('+str+')')
    solver.add(
        878 * x0 + 676 * x1 + 196 * x2 + 688 * x3 + 254 * x4 + 104 * x5 + 732 * x6 + 164 * x7 + 966 * x8 + 527 * x9 + 387 * x10 + 357 * x11 + 542 * x12 + 895 * x13 + 712 * x14 + 570 * x15 + 736 * x16 + 102 * x17 + 791 * x18 + 241 * x19 + 102 * x20 + 616 * x21 + 255 * x22 + 227 * x23 == 1099469)
    solver.add(
        647 * x0 + 133 * x1 + 235 * x2 + 107 * x3 + 519 * x4 + 588 * x5 + 795 * x6 + 185 * x7 + 424 * x8 + 926 * x9 + 697 * x10 + 599 * x11 + 647 * x12 + 906 * x13 + 779 * x14 + 934 * x15 + 520 * x16 + 674 * x17 + 423 * x18 + 209 * x19 + 285 * x20 + 767 * x21 + 192 * x22 + 305 * x23 == 1159478)
    solver.add(
        755 * x0 + 943 * x1 + 743 * x2 + 997 * x3 + 206 * x4 + 798 * x5 + 897 * x6 + 670 * x7 + 977 * x8 + 849 * x9 + 617 * x10 + 283 * x11 + 620 * x12 + 861 * x13 + 964 * x14 + 806 * x15 + 110 * x16 + 232 * x17 + 674 * x18 + 832 * x19 + 804 * x20 + 621 * x21 + 131 * x22 + 473 * x23 == 1460924)
    solver.add(
        420 * x0 + 794 * x1 + 206 * x2 + 229 * x3 + 334 * x4 + 692 * x5 + 589 * x6 + 129 * x7 + 223 * x8 + 268 * x9 + 182 * x10 + 577 * x11 + 879 * x12 + 590 * x13 + 218 * x14 + 356 * x15 + 744 * x16 + 117 * x17 + 238 * x18 + 375 * x19 + 910 * x20 + 912 * x21 + 578 * x22 + 743 * x23 == 1005282)
    solver.add(
        558 * x0 + 583 * x1 + 425 * x2 + 654 * x3 + 483 * x4 + 582 * x5 + 959 * x6 + 997 * x7 + 233 * x8 + 614 * x9 + 760 * x10 + 356 * x11 + 103 * x12 + 294 * x13 + 234 * x14 + 653 * x15 + 116 * x16 + 206 * x17 + 167 * x18 + 158 * x19 + 528 * x20 + 861 * x21 + 938 * x22 + 870 * x23 == 1082934)
    solver.add(
        434 * x0 + 542 * x1 + 283 * x2 + 971 * x3 + 291 * x4 + 206 * x5 + 859 * x6 + 354 * x7 + 297 * x8 + 910 * x9 + 816 * x10 + 413 * x11 + 296 * x12 + 625 * x13 + 174 * x14 + 862 * x15 + 847 * x16 + 616 * x17 + 591 * x18 + 647 * x19 + 875 * x20 + 784 * x21 + 253 * x22 + 227 * x23 == 1203515)
    solver.add(
        875 * x0 + 149 * x1 + 667 * x2 + 812 * x3 + 757 * x4 + 303 * x5 + 233 * x6 + 269 * x7 + 310 * x8 + 546 * x9 + 646 * x10 + 443 * x11 + 514 * x12 + 372 * x13 + 946 * x14 + 317 * x15 + 143 * x16 + 766 * x17 + 326 * x18 + 934 * x19 + 333 * x20 + 345 * x21 + 766 * x22 + 936 * x23 == 1158205)
    solver.add(
        927 * x0 + 558 * x1 + 270 * x2 + 702 * x3 + 477 * x4 + 244 * x5 + 680 * x6 + 873 * x7 + 148 * x8 + 460 * x9 + 194 * x10 + 771 * x11 + 604 * x12 + 881 * x13 + 191 * x14 + 508 * x15 + 154 * x16 + 105 * x17 + 990 * x18 + 515 * x19 + 353 * x20 + 511 * x21 + 696 * x22 + 184 * x23 == 1162214)
    solver.add(
        218 * x0 + 596 * x1 + 370 * x2 + 639 * x3 + 850 * x4 + 529 * x5 + 619 * x6 + 777 * x7 + 438 * x8 + 530 * x9 + 412 * x10 + 308 * x11 + 984 * x12 + 440 * x13 + 557 * x14 + 588 * x15 + 968 * x16 + 246 * x17 + 842 * x18 + 190 * x19 + 180 * x20 + 558 * x21 + 294 * x22 + 814 * x23 == 1198212)
    solver.add(
        560 * x0 + 963 * x1 + 213 * x2 + 584 * x3 + 413 * x4 + 976 * x5 + 146 * x6 + 890 * x7 + 949 * x8 + 550 * x9 + 697 * x10 + 104 * x11 + 465 * x12 + 299 * x13 + 181 * x14 + 524 * x15 + 508 * x16 + 238 * x17 + 608 * x18 + 724 * x19 + 619 * x20 + 631 * x21 + 681 * x22 + 831 * x23 == 1222667)
    solver.add(
        247 * x0 + 438 * x1 + 986 * x2 + 469 * x3 + 359 * x4 + 451 * x5 + 943 * x6 + 801 * x7 + 218 * x8 + 443 * x9 + 591 * x10 + 786 * x11 + 444 * x12 + 392 * x13 + 743 * x14 + 776 * x15 + 662 * x16 + 660 * x17 + 119 * x18 + 578 * x19 + 770 * x20 + 655 * x21 + 692 * x22 + 743 * x23 == 1271138)
    solver.add(
        330 * x0 + 208 * x1 + 391 * x2 + 428 * x3 + 425 * x4 + 627 * x5 + 869 * x6 + 116 * x7 + 166 * x8 + 569 * x9 + 533 * x10 + 454 * x11 + 126 * x12 + 394 * x13 + 710 * x14 + 951 * x15 + 217 * x16 + 335 * x17 + 369 * x18 + 356 * x19 + 698 * x20 + 995 * x21 + 654 * x22 + 492 * x23 == 1009508)
    solver.add(
        196 * x0 + 267 * x1 + 696 * x2 + 821 * x3 + 520 * x4 + 452 * x5 + 323 * x6 + 364 * x7 + 180 * x8 + 951 * x9 + 804 * x10 + 736 * x11 + 715 * x12 + 501 * x13 + 141 * x14 + 281 * x15 + 539 * x16 + 802 * x17 + 754 * x18 + 646 * x19 + 382 * x20 + 259 * x21 + 934 * x22 + 849 * x23 == 1213525)
    solver.add(
        822 * x0 + 756 * x1 + 945 * x2 + 873 * x3 + 777 * x4 + 784 * x5 + 882 * x6 + 423 * x7 + 138 * x8 + 563 * x9 + 469 * x10 + 762 * x11 + 789 * x12 + 351 * x13 + 882 * x14 + 731 * x15 + 905 * x16 + 243 * x17 + 347 * x18 + 978 * x19 + 623 * x20 + 243 * x21 + 697 * x22 + 874 * x23 == 1493615)
    solver.add(
        940 * x0 + 262 * x1 + 517 * x2 + 306 * x3 + 569 * x4 + 939 * x5 + 429 * x6 + 837 * x7 + 645 * x8 + 307 * x9 + 214 * x10 + 414 * x11 + 205 * x12 + 221 * x13 + 656 * x14 + 969 * x15 + 521 * x16 + 878 * x17 + 406 * x18 + 121 * x19 + 322 * x20 + 603 * x21 + 999 * x22 + 368 * x23 == 1241997)
    solver.add(
        261 * x0 + 132 * x1 + 219 * x2 + 679 * x3 + 994 * x4 + 269 * x5 + 702 * x6 + 113 * x7 + 110 * x8 + 987 * x9 + 375 * x10 + 567 * x11 + 324 * x12 + 192 * x13 + 817 * x14 + 852 * x15 + 607 * x16 + 498 * x17 + 794 * x18 + 634 * x19 + 434 * x20 + 644 * x21 + 191 * x22 + 699 * x23 == 1102107)
    solver.add(
        409 * x0 + 603 * x1 + 430 * x2 + 553 * x3 + 750 * x4 + 837 * x5 + 935 * x6 + 547 * x7 + 591 * x8 + 977 * x9 + 336 * x10 + 933 * x11 + 538 * x12 + 632 * x13 + 135 * x14 + 126 * x15 + 755 * x16 + 479 * x17 + 828 * x18 + 329 * x19 + 444 * x20 + 215 * x21 + 115 * x22 + 142 * x23 == 1239617)
    solver.add(
        657 * x0 + 508 * x1 + 659 * x2 + 808 * x3 + 320 * x4 + 813 * x5 + 965 * x6 + 344 * x7 + 259 * x8 + 670 * x9 + 712 * x10 + 321 * x11 + 567 * x12 + 914 * x13 + 195 * x14 + 534 * x15 + 139 * x16 + 975 * x17 + 136 * x18 + 912 * x19 + 580 * x20 + 727 * x21 + 533 * x22 + 634 * x23 == 1230208)
    solver.add(
        664 * x0 + 958 * x1 + 911 * x2 + 795 * x3 + 880 * x4 + 671 * x5 + 380 * x6 + 362 * x7 + 745 * x8 + 801 * x9 + 221 * x10 + 138 * x11 + 316 * x12 + 359 * x13 + 326 * x14 + 501 * x15 + 541 * x16 + 692 * x17 + 621 * x18 + 252 * x19 + 452 * x20 + 998 * x21 + 932 * x22 + 256 * x23 == 1331440)
    solver.add(
        631 * x0 + 389 * x1 + 179 * x2 + 181 * x3 + 286 * x4 + 841 * x5 + 355 * x6 + 250 * x7 + 589 * x8 + 298 * x9 + 916 * x10 + 554 * x11 + 502 * x12 + 726 * x13 + 255 * x14 + 694 * x15 + 836 * x16 + 574 * x17 + 749 * x18 + 673 * x19 + 649 * x20 + 313 * x21 + 864 * x22 + 439 * x23 == 1195073)
    solver.add(
        887 * x0 + 423 * x1 + 770 * x2 + 505 * x3 + 973 * x4 + 821 * x5 + 931 * x6 + 569 * x7 + 412 * x8 + 660 * x9 + 478 * x10 + 510 * x11 + 728 * x12 + 529 * x13 + 359 * x14 + 351 * x15 + 531 * x16 + 174 * x17 + 117 * x18 + 627 * x19 + 805 * x20 + 553 * x21 + 616 * x22 + 389 * x23 == 1296992)
    solver.add(
        524 * x0 + 533 * x1 + 889 * x2 + 180 * x3 + 196 * x4 + 356 * x5 + 820 * x6 + 812 * x7 + 157 * x8 + 674 * x9 + 571 * x10 + 266 * x11 + 234 * x12 + 352 * x13 + 440 * x14 + 700 * x15 + 194 * x16 + 585 * x17 + 654 * x18 + 204 * x19 + 221 * x20 + 951 * x21 + 238 * x22 + 484 * x23 == 987186)
    solver.add(
        259 * x0 + 897 * x1 + 486 * x2 + 758 * x3 + 863 * x4 + 770 * x5 + 551 * x6 + 863 * x7 + 726 * x8 + 762 * x9 + 133 * x10 + 111 * x11 + 355 * x12 + 267 * x13 + 753 * x14 + 358 * x15 + 575 * x16 + 553 * x17 + 192 * x18 + 436 * x19 + 956 * x20 + 570 * x21 + 822 * x22 + 413 * x23 == 1311757)
    solver.add(
        957 * x0 + 330 * x1 + 670 * x2 + 482 * x3 + 245 * x4 + 539 * x5 + 753 * x6 + 741 * x7 + 217 * x8 + 752 * x9 + 604 * x10 + 370 * x11 + 696 * x12 + 901 * x13 + 195 * x14 + 655 * x15 + 244 * x16 + 974 * x17 + 561 * x18 + 485 * x19 + 779 * x20 + 689 * x21 + 573 * x22 + 812 * x23 == 1273174)
    solver.add(
        335 * x0 + 788 * x1 + 386 * x2 + 355 * x3 + 495 * x4 + 421 * x5 + 784 * x6 + 259 * x7 + 557 * x8 + 502 * x9 + 475 * x10 + 951 * x11 + 705 * x12 + 965 * x13 + 596 * x14 + 290 * x15 + 400 * x16 + 767 * x17 + 120 * x18 + 201 * x19 + 423 * x20 + 172 * x21 + 520 * x22 + 432 * x23 == 1139278)
    solver.add(
        540 * x0 + 289 * x1 + 522 * x2 + 867 * x3 + 499 * x4 + 608 * x5 + 636 * x6 + 657 * x7 + 276 * x8 + 738 * x9 + 235 * x10 + 181 * x11 + 655 * x12 + 879 * x13 + 433 * x14 + 999 * x15 + 144 * x16 + 881 * x17 + 914 * x18 + 972 * x19 + 781 * x20 + 586 * x21 + 976 * x22 + 333 * x23 == 1392314)
    solver.add(
        666 * x0 + 929 * x1 + 430 * x2 + 124 * x3 + 113 * x4 + 945 * x5 + 817 * x6 + 594 * x7 + 799 * x8 + 397 * x9 + 477 * x10 + 747 * x11 + 109 * x12 + 808 * x13 + 297 * x14 + 593 * x15 + 291 * x16 + 122 * x17 + 586 * x18 + 471 * x19 + 207 * x20 + 827 * x21 + 224 * x22 + 476 * x23 == 1087254)
    solver.add(
        939 * x0 + 122 * x1 + 511 * x2 + 650 * x3 + 354 * x4 + 357 * x5 + 930 * x6 + 909 * x7 + 961 * x8 + 845 * x9 + 463 * x10 + 737 * x11 + 209 * x12 + 446 * x13 + 270 * x14 + 212 * x15 + 923 * x16 + 111 * x17 + 375 * x18 + 171 * x19 + 540 * x20 + 888 * x21 + 429 * x22 + 158 * x23 == 1180282)
    solver.add(
        647 * x0 + 547 * x1 + 814 * x2 + 310 * x3 + 434 * x4 + 961 * x5 + 517 * x6 + 441 * x7 + 103 * x8 + 985 * x9 + 966 * x10 + 790 * x11 + 627 * x12 + 566 * x13 + 375 * x14 + 211 * x15 + 649 * x16 + 478 * x17 + 396 * x18 + 111 * x19 + 715 * x20 + 853 * x21 + 920 * x22 + 341 * x23 == 1296161)
    solver.add(
        568 * x0 + 261 * x1 + 572 * x2 + 731 * x3 + 611 * x4 + 343 * x5 + 613 * x6 + 510 * x7 + 685 * x8 + 881 * x9 + 630 * x10 + 261 * x11 + 363 * x12 + 629 * x13 + 145 * x14 + 417 * x15 + 719 * x16 + 885 * x17 + 638 * x18 + 915 * x19 + 480 * x20 + 440 * x21 + 529 * x22 + 110 * x23 == 1236327)
    solver.add(
        548 * x0 + 622 * x1 + 654 * x2 + 966 * x3 + 498 * x4 + 518 * x5 + 321 * x6 + 559 * x7 + 578 * x8 + 694 * x9 + 478 * x10 + 885 * x11 + 856 * x12 + 768 * x13 + 759 * x14 + 613 * x15 + 668 * x16 + 715 * x17 + 952 * x18 + 922 * x19 + 628 * x20 + 349 * x21 + 907 * x22 + 435 * x23 == 1548826)
    solver.add(
        283 * x0 + 639 * x1 + 172 * x2 + 613 * x3 + 831 * x4 + 872 * x5 + 612 * x6 + 279 * x7 + 890 * x8 + 242 * x9 + 975 * x10 + 518 * x11 + 749 * x12 + 220 * x13 + 505 * x14 + 209 * x15 + 385 * x16 + 185 * x17 + 307 * x18 + 873 * x19 + 667 * x20 + 676 * x21 + 102 * x22 + 386 * x23 == 1086172)
    solver.add(
        492 * x0 + 113 * x1 + 517 * x2 + 775 * x3 + 368 * x4 + 222 * x5 + 180 * x6 + 864 * x7 + 262 * x8 + 213 * x9 + 480 * x10 + 486 * x11 + 186 * x12 + 793 * x13 + 502 * x14 + 166 * x15 + 896 * x16 + 765 * x17 + 989 * x18 + 984 * x19 + 244 * x20 + 909 * x21 + 823 * x22 + 701 * x23 == 1176662)
    solver.add(
        320 * x0 + 198 * x1 + 555 * x2 + 531 * x3 + 525 * x4 + 285 * x5 + 418 * x6 + 668 * x7 + 888 * x8 + 550 * x9 + 465 * x10 + 300 * x11 + 517 * x12 + 651 * x13 + 607 * x14 + 992 * x15 + 440 * x16 + 664 * x17 + 223 * x18 + 481 * x19 + 510 * x20 + 351 * x21 + 232 * x22 + 150 * x23 == 1120355)
    solver.add(
        233 * x0 + 505 * x1 + 458 * x2 + 191 * x3 + 695 * x4 + 140 * x5 + 944 * x6 + 248 * x7 + 291 * x8 + 676 * x9 + 550 * x10 + 267 * x11 + 237 * x12 + 590 * x13 + 541 * x14 + 430 * x15 + 827 * x16 + 395 * x17 + 281 * x18 + 217 * x19 + 740 * x20 + 717 * x21 + 957 * x22 + 808 * x23 == 1063668)
    solver.add(
        586 * x0 + 176 * x1 + 252 * x2 + 640 * x3 + 828 * x4 + 274 * x5 + 564 * x6 + 660 * x7 + 567 * x8 + 522 * x9 + 467 * x10 + 484 * x11 + 743 * x12 + 924 * x13 + 512 * x14 + 204 * x15 + 351 * x16 + 365 * x17 + 860 * x18 + 303 * x19 + 729 * x20 + 264 * x21 + 725 * x22 + 507 * x23 == 1188501)
    solver.add(
        276 * x0 + 928 * x1 + 847 * x2 + 628 * x3 + 281 * x4 + 159 * x5 + 247 * x6 + 109 * x7 + 378 * x8 + 750 * x9 + 397 * x10 + 210 * x11 + 942 * x12 + 156 * x13 + 573 * x14 + 425 * x15 + 867 * x16 + 443 * x17 + 375 * x18 + 546 * x19 + 776 * x20 + 898 * x21 + 946 * x22 + 457 * x23 == 1175757)
    solver.add(
        122 * x0 + 920 * x1 + 531 * x2 + 712 * x3 + 773 * x4 + 760 * x5 + 561 * x6 + 182 * x7 + 488 * x8 + 502 * x9 + 296 * x10 + 671 * x11 + 267 * x12 + 673 * x13 + 936 * x14 + 244 * x15 + 974 * x16 + 110 * x17 + 563 * x18 + 393 * x19 + 298 * x20 + 338 * x21 + 238 * x22 + 114 * x23 == 1163928)
    solver.add(
        686 * x0 + 649 * x1 + 691 * x2 + 156 * x3 + 343 * x4 + 337 * x5 + 881 * x6 + 870 * x7 + 765 * x8 + 690 * x9 + 416 * x10 + 917 * x11 + 355 * x12 + 925 * x13 + 485 * x14 + 906 * x15 + 398 * x16 + 141 * x17 + 137 * x18 + 756 * x19 + 770 * x20 + 969 * x21 + 193 * x22 + 613 * x23 == 1275018)
    solver.add(
        749 * x0 + 375 * x1 + 948 * x2 + 329 * x3 + 842 * x4 + 652 * x5 + 976 * x6 + 186 * x7 + 167 * x8 + 653 * x9 + 861 * x10 + 799 * x11 + 863 * x12 + 373 * x13 + 660 * x14 + 479 * x15 + 246 * x16 + 816 * x17 + 273 * x18 + 475 * x19 + 367 * x20 + 131 * x21 + 745 * x22 + 160 * x23 == 1262106)
    solver.add(
        803 * x0 + 771 * x1 + 282 * x2 + 613 * x3 + 683 * x4 + 267 * x5 + 390 * x6 + 196 * x7 + 778 * x8 + 789 * x9 + 690 * x10 + 741 * x11 + 105 * x12 + 581 * x13 + 986 * x14 + 979 * x15 + 612 * x16 + 623 * x17 + 196 * x18 + 308 * x19 + 507 * x20 + 107 * x21 + 449 * x22 + 189 * x23 == 1267142)
    solver.add(
        905 * x0 + 376 * x1 + 447 * x2 + 868 * x3 + 352 * x4 + 278 * x5 + 609 * x6 + 125 * x7 + 276 * x8 + 330 * x9 + 906 * x10 + 830 * x11 + 763 * x12 + 843 * x13 + 201 * x14 + 400 * x15 + 488 * x16 + 439 * x17 + 537 * x18 + 395 * x19 + 414 * x20 + 565 * x21 + 190 * x22 + 792 * x23 == 1075457)
    solver.add(
        536 * x0 + 356 * x1 + 245 * x2 + 191 * x3 + 441 * x4 + 804 * x5 + 335 * x6 + 694 * x7 + 303 * x8 + 129 * x9 + 775 * x10 + 478 * x11 + 210 * x12 + 587 * x13 + 931 * x14 + 378 * x15 + 355 * x16 + 265 * x17 + 391 * x18 + 810 * x19 + 182 * x20 + 908 * x21 + 546 * x22 + 890 * x23 == 1022239)
    solver.add(
        932 * x0 + 793 * x1 + 253 * x2 + 416 * x3 + 906 * x4 + 219 * x5 + 543 * x6 + 113 * x7 + 432 * x8 + 176 * x9 + 940 * x10 + 572 * x11 + 323 * x12 + 647 * x13 + 265 * x14 + 918 * x15 + 707 * x16 + 571 * x17 + 846 * x18 + 255 * x19 + 761 * x20 + 299 * x21 + 318 * x22 + 843 * x23 == 1175751)
    solver.add(
        276 * x0 + 169 * x1 + 852 * x2 + 348 * x3 + 406 * x4 + 381 * x5 + 160 * x6 + 552 * x7 + 874 * x8 + 698 * x9 + 620 * x10 + 233 * x11 + 382 * x12 + 539 * x13 + 651 * x14 + 653 * x15 + 566 * x16 + 555 * x17 + 514 * x18 + 750 * x19 + 497 * x20 + 518 * x21 + 752 * x22 + 543 * x23 == 1171272)
    solver.add(
        439 * x0 + 335 * x1 + 221 * x2 + 103 * x3 + 523 * x4 + 649 * x5 + 616 * x6 + 969 * x7 + 165 * x8 + 814 * x9 + 458 * x10 + 179 * x11 + 257 * x12 + 537 * x13 + 112 * x14 + 912 * x15 + 637 * x16 + 125 * x17 + 389 * x18 + 685 * x19 + 510 * x20 + 211 * x21 + 913 * x22 + 282 * x23 == 1087635)
    solver.add(
        246 * x0 + 257 * x1 + 871 * x2 + 531 * x3 + 754 * x4 + 492 * x5 + 816 * x6 + 398 * x7 + 639 * x8 + 350 * x9 + 717 * x10 + 840 * x11 + 207 * x12 + 608 * x13 + 812 * x14 + 872 * x15 + 632 * x16 + 682 * x17 + 527 * x18 + 528 * x19 + 822 * x20 + 779 * x21 + 918 * x22 + 739 * x23 == 1371830)
    solver.add(
        557 * x0 + 398 * x1 + 470 * x2 + 220 * x3 + 346 * x4 + 674 * x5 + 159 * x6 + 629 * x7 + 384 * x8 + 306 * x9 + 261 * x10 + 747 * x11 + 284 * x12 + 749 * x13 + 408 * x14 + 896 * x15 + 225 * x16 + 798 * x17 + 356 * x18 + 239 * x19 + 880 * x20 + 388 * x21 + 937 * x22 + 144 * x23 == 1151455)
    solver.add(
        217 * x0 + 181 * x1 + 755 * x2 + 517 * x3 + 532 * x4 + 590 * x5 + 538 * x6 + 265 * x7 + 837 * x8 + 533 * x9 + 135 * x10 + 634 * x11 + 173 * x12 + 687 * x13 + 573 * x14 + 676 * x15 + 280 * x16 + 399 * x17 + 698 * x18 + 593 * x19 + 417 * x20 + 794 * x21 + 753 * x22 + 142 * x23 == 1143557)
    solver.add(
        977 * x0 + 616 * x1 + 360 * x2 + 673 * x3 + 244 * x4 + 561 * x5 + 566 * x6 + 947 * x7 + 519 * x8 + 189 * x9 + 557 * x10 + 985 * x11 + 517 * x12 + 154 * x13 + 624 * x14 + 146 * x15 + 269 * x16 + 843 * x17 + 551 * x18 + 175 * x19 + 794 * x20 + 752 * x21 + 287 * x22 + 330 * x23 == 1170092)
    solver.add(
        326 * x0 + 448 * x1 + 171 * x2 + 756 * x3 + 332 * x4 + 451 * x5 + 307 * x6 + 873 * x7 + 495 * x8 + 136 * x9 + 975 * x10 + 863 * x11 + 154 * x12 + 417 * x13 + 208 * x14 + 634 * x15 + 174 * x16 + 993 * x17 + 232 * x18 + 891 * x19 + 191 * x20 + 541 * x21 + 290 * x22 + 217 * x23 == 1025867)
    solver.add(
        119 * x0 + 345 * x1 + 446 * x2 + 305 * x3 + 853 * x4 + 239 * x5 + 635 * x6 + 111 * x7 + 265 * x8 + 172 * x9 + 892 * x10 + 765 * x11 + 302 * x12 + 950 * x13 + 466 * x14 + 365 * x15 + 471 * x16 + 170 * x17 + 933 * x18 + 383 * x19 + 375 * x20 + 245 * x21 + 906 * x22 + 382 * x23 == 1035875)
    solver.add(
        677 * x0 + 987 * x1 + 825 * x2 + 834 * x3 + 298 * x4 + 879 * x5 + 901 * x6 + 161 * x7 + 185 * x8 + 423 * x9 + 209 * x10 + 529 * x11 + 672 * x12 + 655 * x13 + 450 * x14 + 151 * x15 + 656 * x16 + 477 * x17 + 208 * x18 + 458 * x19 + 621 * x20 + 552 * x21 + 292 * x22 + 749 * x23 == 1165260)
    solver.add(
        597 * x0 + 753 * x1 + 261 * x2 + 956 * x3 + 477 * x4 + 251 * x5 + 558 * x6 + 659 * x7 + 613 * x8 + 426 * x9 + 976 * x10 + 130 * x11 + 524 * x12 + 805 * x13 + 331 * x14 + 928 * x15 + 355 * x16 + 484 * x17 + 738 * x18 + 981 * x19 + 947 * x20 + 951 * x21 + 699 * x22 + 940 * x23 == 1336190)
    solver.add(
        125 * x0 + 861 * x1 + 926 * x2 + 616 * x3 + 250 * x4 + 625 * x5 + 123 * x6 + 609 * x7 + 949 * x8 + 607 * x9 + 183 * x10 + 575 * x11 + 500 * x12 + 568 * x13 + 795 * x14 + 883 * x15 + 427 * x16 + 424 * x17 + 883 * x18 + 395 * x19 + 569 * x20 + 575 * x21 + 154 * x22 + 185 * x23 == 1256328)
    solver.add(
        706 * x0 + 481 * x1 + 116 * x2 + 509 * x3 + 747 * x4 + 718 * x5 + 426 * x6 + 174 * x7 + 625 * x8 + 282 * x9 + 265 * x10 + 789 * x11 + 130 * x12 + 868 * x13 + 225 * x14 + 691 * x15 + 882 * x16 + 319 * x17 + 238 * x18 + 704 * x19 + 408 * x20 + 119 * x21 + 183 * x22 + 575 * x23 == 1079380)
    solver.add(
        522 * x0 + 701 * x1 + 131 * x2 + 285 * x3 + 120 * x4 + 621 * x5 + 969 * x6 + 476 * x7 + 782 * x8 + 726 * x9 + 140 * x10 + 438 * x11 + 788 * x12 + 849 * x13 + 271 * x14 + 407 * x15 + 482 * x16 + 124 * x17 + 230 * x18 + 521 * x19 + 128 * x20 + 196 * x21 + 270 * x22 + 353 * x23 == 999882)
    solver.add(
        732 * x0 + 537 * x1 + 255 * x2 + 929 * x3 + 826 * x4 + 742 * x5 + 872 * x6 + 592 * x7 + 305 * x8 + 948 * x9 + 560 * x10 + 167 * x11 + 284 * x12 + 391 * x13 + 686 * x14 + 696 * x15 + 937 * x16 + 603 * x17 + 976 * x18 + 629 * x19 + 457 * x20 + 313 * x21 + 199 * x22 + 953 * x23 == 1337727)
    solver.add(
        308 * x0 + 421 * x1 + 549 * x2 + 180 * x3 + 756 * x4 + 282 * x5 + 450 * x6 + 590 * x7 + 186 * x8 + 523 * x9 + 552 * x10 + 892 * x11 + 634 * x12 + 307 * x13 + 718 * x14 + 563 * x15 + 348 * x16 + 420 * x17 + 829 * x18 + 176 * x19 + 900 * x20 + 756 * x21 + 132 * x22 + 192 * x23 == 1097365)
    solver.add(
        546 * x0 + 891 * x1 + 308 * x2 + 944 * x3 + 386 * x4 + 838 * x5 + 636 * x6 + 159 * x7 + 989 * x8 + 670 * x9 + 862 * x10 + 415 * x11 + 272 * x12 + 368 * x13 + 206 * x14 + 321 * x15 + 941 * x16 + 637 * x17 + 440 * x18 + 321 * x19 + 833 * x20 + 349 * x21 + 766 * x22 + 788 * x23 == 1272743)

    print(solver.check())
    print(solver.model())
    return


def my_print():
    # 调用之前要手动将solver的结果做一个处理,转换成合法的data字典
    data = {
        'x6': 48,
 'x2': 97,
 'x18': 85,
 'x0': 102,
 'x12': 95,
 'x3': 103,
 'x7': 119,
 'x23': 0,
 'x4': 123,
 'x5': 110,
 'x11': 117,
 'x8': 95,
 'x9': 121,
 'x13': 107,
 'x14': 110,
 'x1': 108,
 'x10': 48,
 'x16': 119,
 'x17': 95,
 'x19': 80,
 'x20': 88,
 'x21': 33,
 'x15': 111,
 'x22': 125
    }
    # 按照 x 后的数字进行排序
    sorted_data = sorted(data.items(), key=lambda item: int(item[0][1:]))
    # 重组数据
    end_result = ''.join(chr(value) for key, value in sorted_data)
    # 输出转换好的flag
    print(end_result)

# 先调用该函数,把输出结果手动放入my_print()中
calculate()

# 然后运行该函数,输出flag
my_print()