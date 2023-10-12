real_flag = "flag{I_M_the_f1ag}"
flag = "vbqw{Y_C_jxu_v1qw}"
# 将字符串转换为7位二进制表示
binary_text = " ".join(format(ord(char), "07b") for char in flag)
print(binary_text)
flag_list = list(binary_text.split(" "))
