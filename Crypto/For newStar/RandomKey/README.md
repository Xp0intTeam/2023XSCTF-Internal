* **题目名称：**RandomKey
* **题目类型：** Crypto
* **题目难度：**中等
* **出题人：**k1rit0
* **考点：**  维吉尼亚密码分析中的分析方法
* **描述：**  

​		维吉尼亚你重合植树吗？

​		明文是一段有意义的文段，如果你完全解密了它，你会看到flagisxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

​		把这个xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx包上XSCTF{}提交

* **flag：**XSCTF{haveyoureadthebookonehundredyearsofsolitude}

* **Writeup：**可以把整个加密看成是
  $$
  A_im_i + K_i = c_i \mod 26
  $$
  这样会存在一个周期，确定了周期以后按周期分组然后拟重合指数搞定

  ```python
  from math import gcd
  from gmpy2 import invert
  Letters = 'abcdefghijklmnopqrstuvwxyz'
  dic_freq = 'etaoinshrdlcumwfgypbvkjxqz'
  freq = {
      'a':.08167,
      'b':.01492,
      'c':.02782,
      'd':.04253,
      'e':.12702,
      'f':.02228,
      'g':.02015,
      'h':.06094,
      'i':.06966,
      'j':.00153,
      'k':.00772,
      'l':.04025,
      'm':.02406,
      'n':.06749,
      'o':.07507,
      'p':.01929,
      'q':.00095,
      'r':.05987,
      's':.06327,
      't':.09056,
      'u':.02758,
      'v':.00978,
      'w':.02360,
      'x':.00150,
      'y':.01974,
      'z':.00074
  }
  Oa = ord('a')
  cipher = '...'
  
  
  def decrypt(C,As,Ks):
      i = 0
      m = ''
      LEN = len(As)
      while i < len(C):
          y = ord(C[i]) - ord('a')
          A = As[i % LEN]
          K = Ks[i % LEN]
          x = ((y - K) * invert(A,26) ) % 26
          m += chr(x + ord('a'))
          i += 1
      return m
  
  def CHITEST(Str):
      DICT = {}
      StrLen = len(Str)
      for letter in Letters:
              DICT[letter] = 0
          
      for s in Str:
          DICT[s] += 1
  
      Kai = sum([freq[i[0]]  * i[1] / StrLen for i in list(DICT.items())])
      
      return Kai
  LENS = []
  for shift in range(1,201):
      s = 0
      for i,j in zip(cipher,cipher[shift:]):
          if i == j:
              s += 1
      if s > (len(cipher) // 16):
          LENS.append(shift)
  GCD = LENS[0]
  for l in LENS[1:]:
      GCD = gcd(l,GCD)
  
  print(LENS)
  print(GCD)
  LEN = GCD
  DICT_C = ['' for _ in range(LEN)]
  Index = 0
  for c in cipher:
      DICT_C[Index] += c
      Index = (Index + 1) % LEN 
  
  As = []
  Ks = []
  for CB in DICT_C:
      DICT = {}
      for letter in Letters:
              DICT[letter] = 0
          
      for c in CB:
          DICT[c] += 1
      DICT = dict(sorted(DICT.items(),key = lambda x:x[1],reverse = True))
      d = list(DICT.items())
  
      y1,y2 = ord(d[0][0]) - Oa,ord(d[1][0]) - Oa
      i = 2
      while (y2 - y1) % 2 == 0:
          y2 =  ord(d[i][0]) - Oa
          i += 1
      Score = []
      for y1 in d[:9]:
          y1 = ord(y1[0]) - Oa
          for y2 in d[:9]:
              y2 = ord(y2[0]) - Oa
              if y1 != y2:
                  for x1 in dic_freq[:9]:
                      x1 = ord(x1) - Oa
                      for x2 in dic_freq[:9]:
                          x2 = ord(x2) - Oa
                          if x1 != x2:
                              try:
                                  A = ((y2 - y1) * invert(x2 - x1,26)) % 26
                                  IA = invert(A,26)
                              except:
                                  continue
                              K = (y1 - A * x1) % 26
                              _M = ''.join([chr(((((ord(c) - Oa) - K) * IA) % 26) + Oa) for c in CB])
                              Score.append((A,K,CHITEST(_M)))
      
      Score = sorted(Score,key = lambda x:x[2],reverse = True)
      As.append(int(Score[0][0]))
      Ks.append(int(Score[0][1]))
  
  M = decrypt(cipher,As,Ks)
  print(As,Ks)
  print(M,CHITEST(M))
  ```

  

  

  