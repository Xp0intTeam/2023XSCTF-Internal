- 题目名称:rereyours

- 题目类型:Reverse

- 题目难度:容易

- 出题人:bag

- 考点:

  1. enigma virtual box 解包

  2. upx标识符的修改

  3. 简单的xor

- 描述:

- flag:

  XSCTF{U_f0un4_th3_$5c7et_0f_c#!}

- Writeup:

  ```python
  key = ['T', 'F', 'C', 'S', 'X', 'Q', 'W', 'Q', 'C', 'c']
  a1 = [12, 61, 37, 99, 27, 63, 99, 14, 5, 60, 1, 21, 54, 7]
  a2 = [11, 25, 32, 12, 62, 114, 52, 37, 55, 83, 112, 115, 98, 100, 61, 44, 100, 57]
  s1 = []
  s2 = []
  #xxxx
  for i in range(0,14):
      a1[i] = a1[i]^ord(key[i%len(key)])
  for i in range(0,18):
      a2[i] = a2[i]^ord(key[i%len(key)])
  
  for i in range(0,14):
      s1.append(chr(a1[i]))
  for i in range(0,18):
      s2.append(chr(a2[i]))
  #exchange
  for i in range(13,-1,-1):
      temp = s1[i]
      s1[i] = s1[(i*3)%len(s1)]
      s1[(i * 3) % len(s1)] = temp
  for i in range(17,-1,-1):
      temp = s2[i]
      s2[i] = s2[(i*3)%len(s2)]
      s2[(i * 3) % len(s2)] = temp
  ans = "".join(s1+s2)
  print(ans)
  ```
  
  